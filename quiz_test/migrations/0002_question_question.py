# Generated by Django 2.2 on 2020-11-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.CharField(default='question1', max_length=250),
            preserve_default=False,
        ),
    ]
