# Generated by Django 4.0.2 on 2022-02-14 07:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='convertedVideo',
            fields=[
                ('video_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('video', models.FileField(upload_to='video/temp')),
                ('audio', models.FileField(upload_to='video/temp')),
                ('output_video', models.FileField(upload_to='video')),
            ],
        ),
    ]
