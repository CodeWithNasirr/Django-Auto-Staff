# Generated by Django 5.1.3 on 2024-11-28 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email', '0002_email_email_list_subsciber_email_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default='99a49a44', editable=False, max_length=100, unique=True)),
                ('open_at', models.DateTimeField(blank=True, null=True)),
                ('click_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Email.email')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Email.subsciber')),
            ],
        ),
    ]