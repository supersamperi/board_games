# Generated by Django 3.2.9 on 2021-12-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game', '0004_game_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rented',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]