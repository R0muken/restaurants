# Generated by Django 4.1 on 2022-09-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_rename_address_restaurant_address_alter_menu_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='title',
        ),
        migrations.AddField(
            model_name='menu',
            name='dishes',
            field=models.CharField(max_length=200, null=True),
        ),
    ]