# Generated by Django 3.2.3 on 2021-05-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
    ]
