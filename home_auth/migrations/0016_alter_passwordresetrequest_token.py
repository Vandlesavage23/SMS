# Generated by Django 5.1.7 on 2025-03-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0015_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='WpNebey2gbSY9cV8F0eJ7y7aXGpAX0QF', editable=False, max_length=32, unique=True),
        ),
    ]
