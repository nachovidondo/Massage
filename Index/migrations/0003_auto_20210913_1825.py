# Generated by Django 3.1.3 on 2021-09-13 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0002_therapy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitulo')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Terapeuta',
                'verbose_name_plural': 'Terapeutas',
            },
        ),
        migrations.AlterField(
            model_name='therapy',
            name='therapist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.therapist'),
        ),
    ]