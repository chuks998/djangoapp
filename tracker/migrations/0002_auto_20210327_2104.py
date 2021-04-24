# Generated by Django 3.1.5 on 2021-03-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='order_content',
            field=models.CharField(default='empty', max_length=100),
        ),
        migrations.AddField(
            model_name='tracker',
            name='order_progress',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='order_status',
            field=models.CharField(choices=[('active', 'active'), ('delayed', 'delayed'), ('pending', 'pending'), ('delivered', 'delivered')], default=1, max_length=100),
        ),
    ]