# Generated by Django 3.2.1 on 2024-05-07 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recipient', '0011_alter_recipient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
