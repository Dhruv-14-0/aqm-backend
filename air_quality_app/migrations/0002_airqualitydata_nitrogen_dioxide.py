# Generated by Django 5.0.2 on 2024-03-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_quality_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airqualitydata',
            name='nitrogen_dioxide',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]