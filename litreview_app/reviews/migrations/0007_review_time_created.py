# Generated by Django 5.0.6 on 2024-06-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_review_body_alter_review_headline_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]