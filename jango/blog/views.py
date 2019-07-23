# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models , serializers

class Blog(APIView):
    def get(self, request, format=None):
        all_post = models.Post.objects.all()
        serializer = serializers.BlogSerializer(all_post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self ,request , format=None):
        serializer = serializers.BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



class Post(APIView) :
    def get_Post(self,id):
        try:
            return models.Post.objects.get(id=id)
        except models.Post.DoesNotExist :
            raise status.HTTP_404_NOT_FOUND

    def get(self,request , id) :
        post = self.get_Post(id)
        serializer = serializers.BlogSerializer(post)
        return Response(serializer.data , status=status.HTTP_202_ACCEPTED)

    def put(self,request , id , format=None):
        post = self.get_Post(id)
        serializer = serializers.BlogSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request , id , format=None):
        post = self.get_Post(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
