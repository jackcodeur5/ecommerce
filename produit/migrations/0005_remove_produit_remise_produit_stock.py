# Generated by Django 4.0 on 2022-03-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_remove_produit_prix_livraison_produit_date_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='remise',
        ),
        migrations.AddField(
            model_name='produit',
            name='Stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
