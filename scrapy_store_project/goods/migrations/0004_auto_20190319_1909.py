# Generated by Django 2.1.7 on 2019-03-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190319_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bags/'),
        ),
    ]
