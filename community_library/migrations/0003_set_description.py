# Generated by Django 5.0 on 2023-12-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_library', '0002_setcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]