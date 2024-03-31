# Generated by Django 5.0.3 on 2024-03-31 09:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityhubapp', '0002_remove_complaintlike_complaint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('event', 'Δράση'), ('complaint', 'Παράπονο')], max_length=20),
        ),
    ]
