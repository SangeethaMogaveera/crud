from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Po
from .serializers import PoSerializer


class PoList(APIView):
    """
    List all vendors, or creapythte a new vendors.
    """
    def get(self, request, format = None):
        pos = Po.objects.all()
        serializer = PoSerializer(pos, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = PoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PoDetail(APIView):
    """
        Retrieve, update or delete a vendor instance.
        """

    def get_object(self, pk):
        try:
            return Po.objects.get(pk=pk)
        except Po.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        po = self.get_object(pk)
        serializer = PoSerializer(po)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        po = self.get_object(pk)
        serializer = PoSerializer(po, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        po = self.get_object(pk)
        po.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


