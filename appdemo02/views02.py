from appdemo02.models import Defect
from appdemo02.serializers import DefectSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)