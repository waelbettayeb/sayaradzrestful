# Generated by Django 2.1.7 on 2019-03-10 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modele',
            fields=[
                ('Code_Modele', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nom_Modele', models.CharField(max_length=100)),
                ('Id_Marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Model_set', to='marque.Marque')),
            ],
        ),
    ]