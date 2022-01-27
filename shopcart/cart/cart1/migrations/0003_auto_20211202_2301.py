# Generated by Django 3.2.8 on 2021-12-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart1', '0002_rename_people_peop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peop',
            name='email',
        ),
        migrations.RemoveField(
            model_name='peop',
            name='pwd',
        ),
        migrations.AddField(
            model_name='peop',
            name='price',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='peop',
            name='product',
            field=models.CharField(max_length=30, null=True),
        ),
    ]