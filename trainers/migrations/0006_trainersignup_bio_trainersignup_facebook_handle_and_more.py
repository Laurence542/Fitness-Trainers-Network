# Generated by Django 5.0.1 on 2024-01-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0005_rename_experence_trainersignup_accredited_certification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainersignup',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='facebook_handle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='personal_website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]