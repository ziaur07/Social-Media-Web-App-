# Generated by Django 4.2.6 on 2024-02-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_pub_date_post_post_date_post_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
