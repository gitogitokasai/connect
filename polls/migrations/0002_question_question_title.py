# Generated by Django 2.0.1 on 2019-06-04 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]