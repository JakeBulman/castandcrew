# Generated by Django 4.2.15 on 2024-09-25 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_discipline_parent_discipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledisciplines',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline_profiles', to='account.discipline'),
        ),
    ]