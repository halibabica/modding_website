# Generated by Django 2.2 on 2019-12-17 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0021_modedit_modapproved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modedit',
            name='modApproved',
        ),
    ]
