# Generated by Django 2.0.5 on 2018-06-07 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proscenium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proscenium.Country'),
        ),
        migrations.AddField(
            model_name='plot',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proscenium.System'),
        ),
    ]
