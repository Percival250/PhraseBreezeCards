# Generated by Django 5.0 on 2023-12-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='developers/')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
            ],
        ),
    ]