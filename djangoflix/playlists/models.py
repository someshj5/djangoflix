from django.contrib.admin.decorators import action
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from djangoflix.db.models import PublishStateOptions
from videos.models import Video
from djangoflix.db.receivers import publish_state_pre_save,slugify_pre_save


class PlaylistQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(state=PublishStateOptions.PUBLISH,publish_timestamp__lte=now)

class PlaylistManager(models.Manager):
    def get_queryset(self):
        return PlaylistQuerySet(self.model,using=self._db)

class Playlist(models.Model):

    title = models.CharField( max_length=220)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    video = models.ForeignKey(Video,null=True,on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    state = models.CharField(max_length=2,choices=PublishStateOptions.choices,default=PublishStateOptions.DRAFT)
    publish_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True)
    objects = PlaylistManager()

    class Meta:
        db_table = 'playlist'

    def __str__(self):
        return repr(self.title)

    @property
    def is_published(self):
        return self.active


pre_save.connect(publish_state_pre_save,sender=Playlist)

pre_save.connect(slugify_pre_save,sender=Playlist)
