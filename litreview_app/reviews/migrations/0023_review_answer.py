# Generated by Django 5.0.6 on 2024-07-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0022_ticket_has_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='answer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
