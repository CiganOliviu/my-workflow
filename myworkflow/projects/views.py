from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import DevelopmentStack
from projects.serializers import DevelopmentStackSerializer


def index(request):
    template = 'views/index.html'

    return render(request, template_name=template)


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