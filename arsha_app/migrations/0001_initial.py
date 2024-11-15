# Generated by Django 5.1.3 on 2024-11-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to='media/')),
            ],
        ),
    ]