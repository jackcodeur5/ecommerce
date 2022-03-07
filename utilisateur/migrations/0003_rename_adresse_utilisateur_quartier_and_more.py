# Generated by Django 4.0 on 2022-01-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_utilisateur_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='adresse',
            new_name='quartier',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='pass_word',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='date_creation',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='no_de_maison',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='rue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]