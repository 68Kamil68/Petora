# Generated by Django 3.0.6 on 2020-05-09 01:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


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
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateField(default=datetime.datetime(2020, 5, 9, 1, 29, 11, 958785, tzinfo=utc))),
                ('is_private', models.BooleanField(default=False)),
                ('is_enabled', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followed_by', to='users.Profile')),
                ('followed_profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followed', to='users.Profile')),
            ],
        ),
    ]