# Generated by Django 3.2.5 on 2021-07-10 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_alter_video_video_id'),
        ('playlists', '0005_alter_playlist_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlist_feature', to='videos.video'),
        ),
    ]
