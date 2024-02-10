from django.contrib import admin
from .models import Category,Area,Photo
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    list_display	= [ "id" ,"category" ]


class AreaAdmin(admin.ModelAdmin):
    list_display	= [ "id" ,"area" ]


class PhotoAdmin(admin.ModelAdmin):
    list_display	= [ "id", "image","name","date","detail","created_at", "updated_at" ]
    filter_horizontal   = [ "category", "area" ]

    def format_category(self, obj):
        content  = ""

        for category in obj.category.all():
            content += category.category + ","

            return format_html('{}', content)
    
    def format_area(self, obj):
        
        content  = ""

        for area in obj.area.all():
            content += area.area + ","

            return format_html('{}', content)
       
        
    


admin.site.register(Category,CategoryAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Photo,PhotoAdmin)


