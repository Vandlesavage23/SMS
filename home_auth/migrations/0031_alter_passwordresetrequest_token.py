# Generated by Django 5.1.7 on 2025-03-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0030_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='yfzk3iBLSPETPclcRE5HrOtoCbdPsFdg', editable=False, max_length=32, unique=True),
        ),
    ]
