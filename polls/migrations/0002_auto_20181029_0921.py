# Generated by Django 2.1.2 on 2018-10-29 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choidce_text',
            new_name='choice_text',
        ),
    ]
