# Generated by Django 5.0.3 on 2024-03-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='promptpermissionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
