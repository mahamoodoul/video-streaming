# Generated by Django 3.1.5 on 2021-01-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=264, verbose_name='Mention your Category'),
        ),
    ]
