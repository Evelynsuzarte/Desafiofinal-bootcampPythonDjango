# Generated by Django 5.1.2 on 2024-10-28 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_noticia_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='status',
            field=models.CharField(choices=[('AN', 'Em análise'), ('PU', 'Publicado'), ('RM', 'Removido')], default='AN', max_length=2),
        ),
    ]
