# Generated by Django 2.1.1 on 2019-11-27 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default='', max_length=20)),
                ('nickname', models.CharField(blank=True, default='', max_length=10)),
                ('phone', models.CharField(blank=True, default='', max_length=15)),
                ('zip_code', models.CharField(blank=True, default='', max_length=10)),
                ('address', models.CharField(blank=True, default='', max_length=20)),
                ('address_detail', models.CharField(blank=True, default='', max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('following', jsonfield.fields.JSONField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
