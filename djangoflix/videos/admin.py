from django.contrib import admin
from django.db import models

# Register your models here.
from .models import VideoAllProxy,VideoPublishedProxy

class VideoAllAdmin(admin.ModelAdmin):
    list_display =['title','id','video_id','active','is_published']
    search_fields=['title']
    list_filter = ['active']
    readonly_fields = ['id','is_published','publish_timestamp']
    class Meta:
        model = VideoAllProxy 
    # def published(self,obj,*args, **kwargs):
    #     return obj.active


admin.site.register(VideoAllProxy,VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display =['title','video_id']
    search_fields=['title']
    list_filter = ['video_id']
    class Meta:
        model = VideoPublishedProxy
    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)
        # return super().get_queryset(request)

admin.site.register(VideoPublishedProxy,VideoPublishedProxyAdmin)