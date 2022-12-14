# Generated by Django 4.1.3 on 2023-01-02 13:33

from django.db import migrations, models
import django_jalali.db.models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='selected_blog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogs',
            name='show_on_slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=utils.upload_video_path, verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created',
            field=django_jalali.db.models.jDateField(auto_now_add=True),
        ),
    ]
