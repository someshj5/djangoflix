
from .models import PublishStateOptions
from django.utils import timezone
from django.utils.text import slugify


def publish_state_pre_save(sender,instance,*args, **kwargs):
    is_published = instance.state == PublishStateOptions.PUBLISH
    is_draft = instance.state == PublishStateOptions.DRAFT
    if is_published and instance.publish_timestamp is None:
        instance.publish_timestamp = timezone.now()
        print('save as Published')
    elif is_draft:
        instance.publish_timestamp = None

# pre_save.connect(publish_state_pre_save,sender=Video)

def slugify_pre_save(sender,instance,*args, **kwargs):
            if instance.slug is None:
             instance.slug = slugify(instance.title)
# 
# pre_save.connect(slugify_pre_save,sender=Video)