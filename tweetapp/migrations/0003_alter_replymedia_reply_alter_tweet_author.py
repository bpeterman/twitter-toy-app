# Generated by Django 4.1.7 on 2024-08-28 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweetapp', '0002_reply_replymedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replymedia',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_media', to='tweetapp.reply'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweet', to=settings.AUTH_USER_MODEL),
        ),
    ]
