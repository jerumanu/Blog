# Generated by Django 4.0.5 on 2022-06-07 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_remove_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='blog_posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.TextField(),
        ),
    ]