from django.contrib import admin
from blog.models import Category,Tag,Post
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_nav','create_time','post_count') #查询展示的字段
    fields = ('name','status','is_nav','owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin,self).save_model(request,obj,form,change)

    def post_count(self,obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','create_time')
    fields = ('name','status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin,self).save_model(request,obj,form,change)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title','category','status','create_time','operator',
    ]                            #查询展示的字段，operator为自定义字段---》对应楼下的自定义函数
    list_display_links = []      #链接的字段
    list_filter = ['category']   #配置页面过滤器
    search_fields = ['title','category__name']  #配置搜素字段

    actions_on_top = True   #展示在顶部
    actions_on_bottom = True   #展示在底部

    #编辑页面
    save_on_top = True    #保存，编辑按钮是否在顶部
    fields = (
        ('category','title'),
        'desc',
        'status',
        'content',
        'tag',
    )          #新增时候的字段

    def operator(self,obj):           #为自定义函数
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change',args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin,self).save_model(request,obj,form,change)