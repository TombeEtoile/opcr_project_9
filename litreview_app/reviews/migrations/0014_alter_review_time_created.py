# Generated by Django 5.0.6 on 2024-06-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_alter_review_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
