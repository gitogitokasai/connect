# Generated by Django 2.0.1 on 2019-06-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20190605_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(default='マヌケ', max_length=30),
        ),
    ]
