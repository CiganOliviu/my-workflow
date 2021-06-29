from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from organizations.models import Organization
from organizations.serializers import OrganizationsSerializer


class OrganizationsLister(APIView):

    def get(self, request, format=None):
        organization = Organization.objects.all()
        serializer = OrganizationsSerializer(organization, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrganizationsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationsDetails(APIView):

    def get_post(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = OrganizationsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        organization = self.get_post(pk)
        serializer = OrganizationsSerializer(organization, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        organization = self.get_post(pk)
        organization.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



