# Generated by Django 5.2.4 on 2025-07-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Meal')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of Meal')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price ($)')),
                ('available', models.BooleanField(default=False, verbose_name='Available')),
            ],
        ),
    ]
