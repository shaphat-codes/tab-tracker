# Generated by Django 4.0 on 2023-02-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtab',
            name='time_opened',
            field=models.CharField(blank=True, default='2023-02-05 19:19:44', max_length=1000),
        ),
    ]
