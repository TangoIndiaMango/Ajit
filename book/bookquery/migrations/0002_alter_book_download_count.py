# Generated by Django 4.1.7 on 2023-02-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookquery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="download_count",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]