from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from learning.models import CurrentReadingBook
from learning.serializers import CurrentReadingBooksSerializer


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
