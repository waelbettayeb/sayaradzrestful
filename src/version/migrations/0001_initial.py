# Generated by Django 2.1.7 on 2019-03-10 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modele', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('Code_Version', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nom_Version', models.CharField(max_length=200)),
                ('Id_Modele', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Version_set', to='modele.Modele')),
            ],
        ),
    ]
