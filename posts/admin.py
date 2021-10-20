from django.contrib import admin
from posts.models import Posts,Category

# Register your models here.
admin.site.register([Posts, Category])