"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
from typeidea.custom_site import custom_site

from blog.views import  (IndexView,CategoryView,TagView,
                          PostDetailView,SearchView,AuthorView
                         )
from config.views import LinkListView
from typeidea.custom_site import custom_site
from comment.views import CommentView
#from config.views import links

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category-list'),    #将category_id作为参数传递给post_list函数
    url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag-list'),
    #url(r'^post/(?P<post_id>\d+).html$',post_detail,name='post-detail'),
    url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post-detail'),
    url(r'^links/$',LinkListView.as_view(),name='links'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^author/(?P<owner_id>\d+)/$',AuthorView.as_view(),name='author'),
    url(r'^super_admin/', admin.site.urls,name='super-admin'),
    url(r'admin/',custom_site.urls,name='admin'),
    url(r'^comment/$',CommentView.as_view(),name='comment'),
]
