from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from blog.views import CommonViewMixin
from config.models import Link
#from blog.models import Post
# Create your views here.
#def links(request):
#    return HttpResponse('links')

class LinkListView(CommonViewMixin,ListView):
 #   model = Post
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    context_object_name = 'link_list'
    template_name = 'config/links.html'
