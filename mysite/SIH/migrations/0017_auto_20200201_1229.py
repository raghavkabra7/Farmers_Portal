# Generated by Django 2.2.4 on 2020-02-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIH', '0016_auto_20200201_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pestsolution',
            name='Preventing',
        ),
        migrations.RemoveField(
            model_name='pestsolution',
            name='Tips',
        ),
        migrations.RemoveField(
            model_name='pestsolution',
            name='demage',
        ),
        migrations.RemoveField(
            model_name='pestsolution',
            name='long_disc',
        ),
        migrations.AddField(
            model_name='pest',
            name='Preventing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pest',
            name='Tips',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pest',
            name='demage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pest',
            name='long_disc',
            field=models.TextField(null=True),
        ),
    ]
