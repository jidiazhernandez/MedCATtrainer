# Generated by Django 2.2.9 on 2020-01-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_metatask_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='opcs4',
            field=models.TextField(blank=True, default=''),
        ),
    ]