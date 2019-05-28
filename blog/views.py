from django.shortcuts import render
#from django.http import HttpResponse
from blog.models import Post,Tag,Category

# Create your views here.
def post_list(request,category_id=None,tag_id=None):
    tag = None
    category = None
    if tag_id:
        post_list,tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list,category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
    }
    return render(request,'blog/list.html',context=context)
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
