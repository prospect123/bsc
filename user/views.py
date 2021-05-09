from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView,ListCreateAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)
from .serializers import *

class USERCreateView(CreateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class USERListView(ListAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class USERRetrieveView(RetrieveAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class USERDeleteView(DestroyAPIView):
    queryset = user.objects.all()


class USERUpdateView(UpdateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

class userListCreateView(ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class userRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class userRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer


class userRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer
