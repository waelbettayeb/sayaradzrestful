# Generated by Django 2.1.7 on 2019-06-21 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('option', '0012_auto_20190318_1154'),
        ('modele', '0002_modele_image'),
        ('couleur', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compose_Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule_Compose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prix_Total', models.FloatField(default=0.0)),
                ('Automobiliste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Automobiliste')),
                ('Couleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='couleur.Couleur')),
                ('Modele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modele.Modele')),
                ('Options', models.ManyToManyField(to='option.Option')),
            ],
        ),
        migrations.AddField(
            model_name='compose_option',
            name='vehicule_compose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompositionVehicule.Vehicule_Compose'),
        ),
    ]
