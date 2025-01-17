# Generated by Django 5.0.6 on 2024-06-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pays', models.CharField(max_length=100)),
                ('Budget_Jour', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Duree_Jour', models.IntegerField()),
                ('Preferences', models.CharField(max_length=100)),
                ('Activites', models.CharField(max_length=100)),
                ('Hotel_3', models.IntegerField()),
                ('Hotel_4', models.IntegerField()),
                ('Hotel_5', models.IntegerField()),
            ],
        ),
    ]
