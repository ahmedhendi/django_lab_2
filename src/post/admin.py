from django.contrib import admin

from .models import post

# Register your models here .
 
class PostAdmin(admin.ModelAdmin):
    list_filter=['active','Created']
    list_display=['title','Created','active']
    search_fields=['title','content']



admin.site.register(post,PostAdmin)