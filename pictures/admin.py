from django.contrib import admin
from .models import Profile, Post, Location,FollowersCount
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['profile']
    ordering = ['profile']
    search_fields = ['foreignkeyfield__name']

admin.site.register(Post)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(FollowersCount)
