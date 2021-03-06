# Generated by Django 3.0.6 on 2020-05-11 21:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='breed',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='followed_by',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_photos/default_profile_pic.jpg', upload_to='profile_photos'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='follows',
            name='followed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followedby', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='follows',
            name='followed_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_profile', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
