# Generated by Django 4.0 on 2022-01-07 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraison', '0003_livraison_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livraison',
            name='commande',
        ),
    ]
