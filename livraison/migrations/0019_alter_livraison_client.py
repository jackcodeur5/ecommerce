# Generated by Django 4.0 on 2022-03-01 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('livraison', '0018_alter_livraison_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livraison',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
