# Generated by Django 5.0.2 on 2024-02-09 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ['date'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
