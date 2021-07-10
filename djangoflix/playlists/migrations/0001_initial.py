# Generated by Django 3.2.5 on 2021-07-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2)),
                ('publish_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'playlist',
            },
        ),
    ]
