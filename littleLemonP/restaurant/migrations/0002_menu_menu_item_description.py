# Generated by Django 4.1.4 on 2022-12-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='Tell us what you feel!', max_length=1000),
        ),
    ]
