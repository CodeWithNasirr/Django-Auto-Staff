# Generated by Django 5.1.3 on 2024-11-25 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='email_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Email.list'),
        ),
        migrations.AddField(
            model_name='subsciber',
            name='email_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Email.list'),
        ),
    ]
