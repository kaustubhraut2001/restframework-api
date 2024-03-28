from django.urls import path , include

from . import views

urlpatterns = [
	path('blogpost/' , views.BlogpostListCreate.as_view() , name='blogpost_list_create'),
]