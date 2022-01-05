# Generated by Django 3.2.5 on 2022-01-05 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0007_remove_package_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning_history',
            name='hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='learning_history',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
