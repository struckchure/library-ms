# Generated by Django 4.0.1 on 2022-01-28 07:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('649c6fa8-d349-4f50-b751-4fabc5a64024'), primary_key=True, serialize=False),
        ),
    ]
