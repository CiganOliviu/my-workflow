from django.http import Http404
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import *

from projects.serializers import DevelopmentStackSerializer, PersonalProjectsSerializer, \
    CurrentReadingBooksSerializer, OrganizationsSerializer


def index(request):
    return redirect('restapi/personal-projects/')


class DevelopmentStackLister(APIView):

    def get(self, request, format=None):
        stack = DevelopmentStack.objects.all()
        serializer = DevelopmentStackSerializer(stack, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DevelopmentStackSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DevelopmentStackDetails(APIView):

    def get_post(self, pk):
        try:
            return DevelopmentStack.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = DevelopmentStackSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stack = self.get_post(pk)
        serializer = DevelopmentStackSerializer(stack, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stack = self.get_post(pk)
        stack.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PersonalProjectsLister(APIView):

    def get(self, request, format=None):
        projects = PersonalProject.objects.all()
        serializer = PersonalProjectsSerializer(projects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalProjectsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalProjectsDetails(APIView):

    def get_post(self, pk):
        try:
            return PersonalProject.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = PersonalProjectsSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_post(pk)
        serializer = PersonalProjectsSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_post(pk)
        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentReadingBooksLister(APIView):

    def get(self, request, format=None):
        books = CurrentReadingBook.objects.all()
        serializer = CurrentReadingBooksSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CurrentReadingBooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentReadingBooksDetails(APIView):

    def get_post(self, pk):
        try:
            return CurrentReadingBook.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = CurrentReadingBooksSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_post(pk)
        serializer = CurrentReadingBooksSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_post(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


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
