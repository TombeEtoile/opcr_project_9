# Generated by Django 5.0.6 on 2024-07-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0021_review_ticket_delete_ticketanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='has_review',
            field=models.BooleanField(default=False),
        ),
    ]
