# Generated by Django 2.1.7 on 2019-03-17 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarif', '0002_auto_20190314_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='Modele',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='modele.Modele'),
        ),
    ]
