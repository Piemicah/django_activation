# Generated by Django 5.1.4 on 2024-12-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=200, unique=True)),
                ('account', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]