# Generated by Django 3.2.6 on 2021-08-31 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0002_rename_user_message_customuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
    ]
