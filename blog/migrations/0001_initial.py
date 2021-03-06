# Generated by Django 3.0.6 on 2020-05-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('author', models.CharField(max_length=300, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uppdated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
