# Generated by Django 4.2.14 on 2024-07-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sentimentdata",
            name="graph",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]