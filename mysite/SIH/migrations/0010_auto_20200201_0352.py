# Generated by Django 2.2.4 on 2020-02-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIH', '0009_user_detail_aadhar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pestsolution',
            name='demage',
        ),
        migrations.AddField(
            model_name='pest',
            name='demage',
            field=models.TextField(blank=True, null=True),
        ),
    ]
