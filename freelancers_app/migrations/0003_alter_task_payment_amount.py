# Generated by Django 5.0.2 on 2024-11-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0002_task_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='payment_amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]