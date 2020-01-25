from django.shortcuts import render
from .permissions import IsAuthorUpdateOrReadonly
from .serializers import PostSerializer
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post
from django.core.signals import request_started, request_finished
import time
import json
from django.http import HttpResponse

from rest_framework.negotiation import BaseContentNegotiation
from rest_framework.renderers import JSONRenderer


class IgnoreClientContentNegotiation(BaseContentNegotiation):
    def select_parser(self, request, parsers):

        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):

        return (renderers[0], renderers[0].media_type)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorUpdateOrReadonly]
    authentication_classes = []
    renderer_classes = [JSONRenderer]
    content_negotiation_class = IgnoreClientContentNegotiation

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR']
        )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR'])

    def dispatch(self, request, *args, **kwargs):
        global cbv
        cbv = self

        dispatch_start = time.time()
        response = super().dispatch(request, *args, **kwargs)

        render_start = time.time()
        # response.render()
        self.render_time = time.time() - render_start

        self.dispatch_time = time.time() - dispatch_start
        self.api_view_time = self.dispatch_time - (self.render_time + self.serializer_time + self.db_time)

        return response

    def list(self, request, *args, **kwargs):
        db_start = time.time()
        # post_list = list(self.queryset)

        data = cache.get('post_list_cache')

        if data is None:
            data = list(self.queryset.values('author__username', 'message'))
            cache.set('post_list_cache', data)

        data = list(self.queryset.values('author__username', 'message'))
        self.db_time = time.time() - db_start

        # serializer_start = time.time()
        # serializer = self.get_serializer(self.queryset, many=True)
        # data = serializer.data
        # self.serializer_time = time.time() - serializer_start
        self.serializer_time=0

        return HttpResponse(json.dumps(data), content_type='application/json; charset=utf8')


def started_fn(sender, **kwargs):
    global started
    started = time.time()


def finished_fn(sender, **kwargs):
    request_response_time = (time.time() - started) - cbv.dispatch_time

    total = cbv.db_time + cbv.serializer_time + cbv.api_view_time + cbv.render_time + request_response_time

    print(total)

    print('Database Lookup    - db_time         : {:.6f}s, {:>4.1f}%'.format(cbv.db_time, 100 * (cbv.db_time / total)))
    print('Serialization      - serializer_time : {:.6f}s, {:>4.1f}%'.format(cbv.serializer_time,
                                                                             100 * (cbv.serializer_time / total)))
    print('API View           - api_view_time   : {:.6f}s, {:>4.1f}%'.format(cbv.api_view_time,
                                                                             100 * (cbv.api_view_time / total)))
    print('Response rendering - render_time     : {:.6f}s, {:>4.1f}%'.format(cbv.render_time,
                                                                             100 * (cbv.render_time / total)))
    print('Django request/response              : {:.6f}s, {:>4.1f}%'.format(request_response_time,
                                                                             100 * (request_response_time / total)))


request_started.connect(started_fn)  # 요청 처리 시작
request_finished.connect(finished_fn)  # 요청 처리 끝




# Create your views here.
