# Generated by Django 3.1.2 on 2021-05-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210509_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainbody',
            name='name',
            field=models.CharField(default=0, max_length=20000000),
            preserve_default=False,
        ),
    ]
