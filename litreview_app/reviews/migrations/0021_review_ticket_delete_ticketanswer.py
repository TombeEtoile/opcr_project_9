# Generated by Django 5.0.6 on 2024-07-08 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_remove_review_ticket_alter_review_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.ticket'),
        ),
        migrations.DeleteModel(
            name='TicketAnswer',
        ),
    ]
