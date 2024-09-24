# Generated by Django 4.2.15 on 2024-09-22 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_discipline_profiledisciplines_alter_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='parent_discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_discipline', to='account.discipline'),
        ),
    ]