# Generated by Django 4.2.6 on 2023-12-14 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_accessrecord_rename_tapic_name_topic_topic_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='Topic_name',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]