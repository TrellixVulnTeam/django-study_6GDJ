from django.contrib import admin
from config.models import Link,SideBar
from typeidea.base_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title','href','status','weight','create_time')
    fields = ('title','href','status','weight')

    # def save_model(self, request, obj, form, change):
    #     obj_owner = request.user
    #     return super(LinkAdmin,self).save_model(request,obj,form,change)

@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title','display_type','content','create_time')
    fields = ('title','display_type','content')

    # def save_model(self, request, obj, form, change):
    #     obj_owner = request.user
    #     return super(SideBarAdmin,self).save_model(request,obj,form,change)