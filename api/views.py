from django.shortcuts import render
from rest_framework import generics
from .models import Blogpost
from .serializers import BlogpostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class BlogpostListCreate(generics.ListCreateAPIView):
	queryset = Blogpost.objects.all()
	serializer_class = BlogpostSerializer



class BlogPostRetriveanddestroy(generics.RetrieveDestroyAPIView ):
	queryset = Blogpost.objects.all()
	serializer_class = BlogpostSerializer

class BlogPostandDelete(generics.DestroyAPIView):
	queryset = Blogpost.objects.all()
	serializer_class = BlogpostSerializer




class BlogpostList(APIView):
	def get(self , request):
		title = request.query_params.get('title')
		if title:
			blogpost = Blogpost.objects.filter(title=title)
		else:
			blogpost = Blogpost.objects.all()

		serializer = BlogpostSerializer(blogpost , many=True)
		return Response(serializer.data , status=200)