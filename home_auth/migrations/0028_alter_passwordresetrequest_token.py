# Generated by Django 5.1.7 on 2025-03-31 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0027_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='7tF5AmDzXQOzspqCArGZp7t5nwzeranq', editable=False, max_length=32, unique=True),
        ),
    ]
