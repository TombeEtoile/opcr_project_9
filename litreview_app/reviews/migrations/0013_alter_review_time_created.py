# Generated by Django 5.0.6 on 2024-06-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_review_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
