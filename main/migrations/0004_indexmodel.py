# Generated by Django 4.2.7 on 2024-02-20 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_buffermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
