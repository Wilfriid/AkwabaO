# Generated by Django 5.0.6 on 2024-06-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('mot_de_passe', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
    ]
