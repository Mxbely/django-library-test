# Generated by Django 5.1.2 on 2024-10-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="pseudonym",
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]