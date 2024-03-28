from django.urls import path , include

from . import views

urlpatterns = [
	path('blogpost/' , views.BlogpostListCreate.as_view() , name='blogpost_list_create'),
	path('blogpost/<int:pk>/' , views.BlogPostRetriveanddestroy.as_view() , name='blogpost_retrive_destroy'),
	path('blogpost/<int:pk>/delete/' , views.BlogPostandDelete.as_view() , name='blogpost_delete'),
	path('blogpostlist/' , views.BlogpostList.as_view() , name='blogpost_list'),
]