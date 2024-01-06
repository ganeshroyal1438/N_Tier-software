# Generated by Django 4.2.6 on 2023-12-08 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='Tapic_name',
            new_name='Topic_name',
        ),
        migrations.DeleteModel(
            name='accesscode',
        ),
    ]