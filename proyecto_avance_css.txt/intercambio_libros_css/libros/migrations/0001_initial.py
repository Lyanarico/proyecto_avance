# Generated by Django 5.2.2 on 2025-06-07 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('disponible', models.BooleanField(default=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
