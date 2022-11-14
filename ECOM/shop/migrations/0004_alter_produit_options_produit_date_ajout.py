# Generated by Django 4.1.2 on 2022-11-05 06:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_produit_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ['-date_ajout']},
        ),
        migrations.AddField(
            model_name='produit',
            name='date_ajout',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]