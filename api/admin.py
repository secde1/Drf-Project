# from django.contrib import admin
# from .models import Hashtag, Blog
#
#
# admin.site.register(Hashtag, Blog)
from django.contrib import admin
from .models import Hashtag, Blog

admin.site.register(Hashtag)
admin.site.register(Blog)
# from django.contrib import admin
#
# from api.models import Blog, Hashtag
#
#
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#
# admin.site.register(Blog, BlogAdmin)
