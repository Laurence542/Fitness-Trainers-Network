# Generated by Django 5.0.1 on 2024-01-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0003_trainersignup_accredited_certification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainersignup',
            old_name='accredited_certification',
            new_name='experence',
        ),
        migrations.RenameField(
            model_name='trainersignup',
            old_name='additional_certifications',
            new_name='language',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='calendar_type',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='education_background',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='event_preparation_specialties',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='languages_spoken',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='preferred_training_environment',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='speciality_populations',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='specialization_fitness_training',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='training_equipment_utilized',
        ),
        migrations.RemoveField(
            model_name='trainersignup',
            name='training_type',
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='age',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
