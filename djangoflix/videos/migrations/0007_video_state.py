# Generated by Django 3.2.5 on 2021-07-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20210710_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
