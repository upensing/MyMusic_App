# Generated by Django 4.0.5 on 2022-09-13 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_songs_albumsname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='albumsName',
            new_name='albumName',
        ),
    ]
