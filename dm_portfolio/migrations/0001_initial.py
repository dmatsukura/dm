# Generated by Django 4.2.5 on 2023-10-17 17:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog Profiles',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('url', models.URLField(blank=True, null=True)),
                ('is_image', models.BooleanField(default=True)),
                ('ts_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media Files',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ts_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio Profiles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('score', models.IntegerField(blank=True, default=80, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='skills')),
                ('is_key_skill', models.BooleanField(default=False)),
                ('ts_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='testimonials')),
                ('role', models.CharField(blank=True, max_length=250, null=True)),
                ('quote', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ts_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('ts_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('skills', models.ManyToManyField(blank=True, to='dm_portfolio.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]