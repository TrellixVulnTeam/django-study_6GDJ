from django.contrib import admin
from blog.models import Category,Tag,Post
from django.urls import reverse
from django.utils.html import format_html
from blog.adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry

class PostInline(admin.TabularInline):   #可选择继承自admin.StackedInline以获取不同的展示样式
    fields = ('title','desc')
    extra = 1    #控制额外多几个
    model = Post

# Register your models here.

@admin.register(Category,site=custom_site)
#class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ('name','status','is_nav','create_time','post_count') #查询展示的字段
    fields = ('name','status','is_nav','owner')
    #这部分代码使用了继承了BaseOwnerAdmin这个基类。
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin,self).save_model(request,obj,form,change)

    def post_count(self,obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

@admin.register(Tag,site=custom_site)
#class TagAdmin(admin.ModelAdmin):
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name','status','create_time')
    fields = ('name','status')
    #这部分代码使用了继承了BaseOwnerAdmin这个基类。
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin,self).save_model(request,obj,form,change)

class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器，只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id','name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset

#@admin.register(Post)
@admin.register(Post,site=custom_site)  #指定site显示，
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title','category','status',
        'create_time','operator',
    ]                            #查询展示的字段，operator为自定义字段---》对应楼下的自定义函数
    list_display_links = []      #链接的字段

    list_filter = ['category',CategoryOwnerFilter]   #配置页面过滤器
    search_fields = ['title','category__name']  #配置搜素字段
    actions_on_top = True   #展示在顶部
    actions_on_bottom = True   #展示在底部
    save_on_top = True  # 保存，编辑按钮是否在顶部

    #编辑页面
    save_on_top = True    #保存，编辑按钮是否在顶部
    exclude = ('owner',)
    # fields = (
    #     ('category','title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )          #新增时候的字段

    fieldsets = (
        ('基础配置',{                           #当前板块的名称string
            'description': '基础配置描述',    #当前板块的描述dict
            'fields':(
                ('title','category'),
                ('status'),
            ),
        }),
        ('内容',{
            'fields':(
                'desc',
                'content',
            ),
        }),

        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        }),
    )
    filter_vertical = ('tag',)

    def operator(self,obj):           #为自定义函数
        return format_html(
            '<a href="{}">编辑</a>',
            #reverse('admin:blog_post_change',args=(obj.id,))
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    # 这部分代码使用了继承了BaseOwnerAdmin这个基类。
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin,self).save_model(request,obj,form,change)
    #
    # def get_queryset(self, request):
    #     qs = super(PostAdmin,self).get_queryset(request)
    #     return qs.filter(owner=request.user)

    class Medis:
        css = {    #配置静态的css文件
            'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)

@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user','change_message']
