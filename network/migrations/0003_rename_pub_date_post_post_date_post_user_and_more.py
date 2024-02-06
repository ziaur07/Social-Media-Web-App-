# Generated by Django 4.2.6 on 2024-02-05 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='post_date',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=150),
        ),
    ]
