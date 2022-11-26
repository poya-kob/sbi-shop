# Generated by Django 4.1.3 on 2022-11-26 13:07

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='body')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('video', models.FileField(upload_to='', verbose_name='video')),
                ('created_date', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('modified_date', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('category', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.categories', verbose_name='category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
