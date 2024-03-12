# Generated by Django 4.1.12 on 2024-01-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='promptmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('prompt', models.TextField()),
                ('title', models.CharField(default='default', max_length=30)),
            ],
        ),
    ]