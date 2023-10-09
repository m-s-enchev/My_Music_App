# Generated by Django 4.2.2 on 2023-10-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_album_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30),
        ),
    ]
