# Generated by Django 4.2.4 on 2023-09-09 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_content', '0008_distances'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distances',
            old_name='model',
            new_name='mode',
        ),
    ]