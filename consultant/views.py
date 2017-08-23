from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Consultant
from .serializers import ConsultantSerializer


class ConsultantList(APIView):
    """
    List all Consultants, or create a new Consultants.
    """
    def get(self, request, format = None):
        consultants = Consultant.objects.all()
        serializer = ConsultantSerializer(consultants, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = ConsultantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsultantDetail(APIView):
    """
        Retrieve, update or delete a vendor instance.
        """

    def get_object(self, pk):
        try:
            return Consultant.objects.get(pk=pk)
        except Consultant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        consultant = self.get_object(pk)
        serializer = ConsultantSerializer(consultant)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        consultant = self.get_object(pk)
        serializer = ConsultantSerializer(consultant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        consultant = self.get_object(pk)
        consultant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)