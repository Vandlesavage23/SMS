# Generated by Django 5.1.7 on 2025-03-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0014_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='e8q5Qk7EzhyfHLKl4jon8dUhKRliyT3p', editable=False, max_length=32, unique=True),
        ),
    ]
