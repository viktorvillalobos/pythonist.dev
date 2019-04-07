# Generated by Django 2.1 on 2019-04-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], max_length=9, verbose_name='Status')),
                ('slug', models.CharField(max_length=255, null=True, verbose_name='Slug')),
                ('published', models.DateTimeField(null=True, verbose_name='Published Timestamp')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Created')),
            ],
        ),
    ]