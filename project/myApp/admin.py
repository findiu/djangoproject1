from django.contrib import admin

# Register your models here.
from .models import Grades,Students
class StudentsInfo(admin.TabularInline):#StackedInline
    model = Students
    extra = 2
class GraderAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #列表页属性
    #显示字段
    list_display =['pk','gname','gdata','ggirlnum','gboynum','isDelete']
    #过滤器
    list_filter =['gname']
    #搜索查找
    search_fields =['gname']
    #分页
    list_per_page =3
    #添加修改也属性(fields和fieldsets不能同时使用)
    #属性的先后顺序
    #fields =['gname','ggirlnum','gboynum','gdata','isDelete']
    #设置分组
    fieldsets =[
        ("人数",{"fields":['ggirlnum','gboynum']}),
        ("属性", {"fields":['gname', 'gdata','isDelete']})
    ]
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    #列表页属性
    #显示字段
    list_display =['pk','sname',gender,'sage','scontend','isDelete','sgrade']
    #过滤器
    list_filter =['sname']
    #搜索查找
    search_fields =['sname']
    #分页
    list_per_page =3
    #添加修改也属性(fields和fieldsets不能同时使用)
    #属性的先后顺序
    #fields =['sname','sgender','sage','scontend','isDelete','sgrade']
    #设置分组
    fieldsets =[
        ("信息",{"fields":['sname','sage']}),
        ("分数", {"fields":['sgrade', 'sgender','scontend','isDelete']})
    ]
    actions_on_bottom = True
    actions_on_top = False

admin.site.register(Grades,GraderAdmin)
#admin.site.register(Students,StudentsAdmin)