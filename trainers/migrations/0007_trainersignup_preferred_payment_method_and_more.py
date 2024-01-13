# Generated by Django 5.0.1 on 2024-01-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0006_trainersignup_bio_trainersignup_facebook_handle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainersignup',
            name='preferred_payment_method',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('CAD', 'CAD')], max_length=10),
        ),
        migrations.AddField(
            model_name='trainersignup',
            name='pricing_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]