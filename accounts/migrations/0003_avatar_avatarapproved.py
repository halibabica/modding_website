# Generated by Django 2.2.2 on 2019-09-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190924_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='avatarApproved',
            field=models.BooleanField(default=False, verbose_name='avatar moderation approval'),
        ),
    ]
