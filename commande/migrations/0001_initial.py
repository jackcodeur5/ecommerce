# Generated by Django 4.0 on 2021-12-11 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produit', '0001_initial'),
        ('livraison', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField()),
                ('date_reglement', models.DateTimeField()),
                ('mode_paiement', models.CharField(max_length=200, null=True)),
                ('total_commande', models.IntegerField(null=True)),
                ('etat_commande', models.CharField(choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('livraison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livraison.livraison')),
            ],
        ),
        migrations.CreateModel(
            name='Constituer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_produit', models.CharField(max_length=200, null=True)),
                ('qte_produit', models.IntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commande.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='produits',
            field=models.ManyToManyField(through='commande.Constituer', to='produit.Produit'),
        ),
    ]
