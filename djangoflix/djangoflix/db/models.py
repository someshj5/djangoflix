from django.db import models


class PublishStateOptions(models.TextChoices):
    PUBLISH = 'PU','Publish'
    DRAFT = 'DR','Draft'
    # UNLISTED = 'UN','Unlisted'
    # PRIVATE = 'PR','Private'
# Create your models here.