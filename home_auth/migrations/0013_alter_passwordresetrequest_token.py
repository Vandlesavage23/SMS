# Generated by Django 5.1.7 on 2025-03-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0012_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='XGQ0FlcU1kQdT8QUNEIXbBb1nrAojL9P', editable=False, max_length=32, unique=True),
        ),
    ]
