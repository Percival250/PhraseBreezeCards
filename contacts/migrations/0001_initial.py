# Generated by Django 5.0 on 2023-12-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(default='+996', max_length=14)),
                ('telegram_media_link', models.URLField()),
                ('instagram_media_link', models.URLField()),
            ],
        ),
    ]
