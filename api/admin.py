# from django.contrib import admin
# from .models import Hashtag, Blog
#
#
# admin.site.register(Hashtag, Blog)
from django.contrib import admin
from .models import Hashtag, Blog

admin.site.register(Hashtag)
admin.site.register(Blog)
