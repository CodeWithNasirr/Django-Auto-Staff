# Generated by Django 5.1.3 on 2024-11-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0005_alter_email_tracking_unique_id_alter_sent_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_tracking',
            name='unique_id',
            field=models.CharField(default='5560fdb7', max_length=100, unique=True),
        ),
    ]
