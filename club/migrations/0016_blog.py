# Generated by Django 3.2.5 on 2021-10-12 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0015_alter_emploi_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('vie_club', 'Vie du club'), ('evenement', 'Événement'), ('sortie', 'Sortie')], default='vie_club', max_length=30)),
                ('titre', models.CharField(max_length=40)),
                ('contenu', models.CharField(max_length=4000)),
                ('photo', models.ImageField(blank=True, upload_to='club/images/blog/')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.profil')),
            ],
        ),
    ]