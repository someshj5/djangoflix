# Generated by Django 3.2.5 on 2021-07-10 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videoproxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('videos.video',),
        ),
    ]
