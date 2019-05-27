from django.contrib import admin

#定义基类，用于其他模块需要使用时可以直接调用，减少不必要的代码
class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1.用来自动补充文章，分类，标签，侧边友链这些Model的owner字段
    2.用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin,self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin,self).save_model(request,obj,form,change)