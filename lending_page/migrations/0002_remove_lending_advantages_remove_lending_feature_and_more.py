# Generated by Django 5.0 on 2023-12-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lending_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lending',
            name='advantages',
        ),
        migrations.RemoveField(
            model_name='lending',
            name='feature',
        ),
        migrations.AddField(
            model_name='description',
            name='advantages',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='description',
            name='feature',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
