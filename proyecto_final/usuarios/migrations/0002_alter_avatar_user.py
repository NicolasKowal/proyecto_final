# Generated by Django 4.2.1 on 2023-06-20 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]