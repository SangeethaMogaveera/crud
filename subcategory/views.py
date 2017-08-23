from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subcategory
from .serializers import SubCategorySerializer
from django.contrib.auth.models import User


class SubCategoryList(APIView):
    """
    List all projects, or create a new project.
    """
    def get(self, request, format = None):
        subcategory = Subcategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryDetail(APIView):
    """
        Retrieve, update or delete a project instance.
        """

    def get_object(self, pk):
        try:
            return Subcategory.objects.get(pk=pk)
        except Subcategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SubCategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subcategory = self.get_object(pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from django.shortcuts import render

# Create your views here.
