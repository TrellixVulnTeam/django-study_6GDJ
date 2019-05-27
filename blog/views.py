from django.shortcuts import render
#from django.http import HttpResponse
from blog.models import Post,Tag

# Create your views here.
def post_list(request,category_id=None,tag_id=None):
    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)

    return render(request,'blog/list.html',context={'post_list': post_list})
    #render(http的请求，模板名称，数据字典，页面编码类型，状态码，模板引擎解析)
    # content = 'post_list category_id={category_id},tag_id={tag_id}'.format(
    #     category_id = category_id,
    #     tag_id = tag_id,
    # )
    # return HttpResponse(content)

def post_detail(request,post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    #return HttpResponse('detail')
    return render(request,'blog/detail.html',context={'post': post})
