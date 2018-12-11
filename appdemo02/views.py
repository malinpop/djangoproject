from appdemo02.models import Defect
from appdemo02.serializers import DefectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class DefectList(APIView):
    def get(self, request):
        defects = Defect.objects.all()
        serializer = DefectSerializer(defects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DefectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DefectDetail(APIView):
    def get_object(self, request, bug_code):
        try:
            return Defect.objects.get(bug_code=bug_code)
        except Defect.DoesNotExist:
            raise Http404

    def get(self, request, bug_code):
        defect = self.get_object(self, bug_code)
        serializer = DefectSerializer(defect)
        return Response(serializer.data)

    def put(self, request, bug_code):
        defect = self.get_object(self, bug_code)
        serializer = DefectSerializer(defect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bug_code):
        defect = self.get_object(self, bug_code)
        defect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)