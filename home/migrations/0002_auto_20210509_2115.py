# Generated by Django 3.1.2 on 2021-05-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainbody',
            name='img',
        ),
        migrations.RemoveField(
            model_name='mainbody',
            name='slug',
        ),
        migrations.AddField(
            model_name='mainbody',
            name='Genre1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='Genre2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='Genre3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='Genre4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='desc',
            field=models.CharField(default=0, max_length=20000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='imdb',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='language1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='language2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mainbody',
            name='link_1080',
            field=models.CharField(default=0, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='link_480',
            field=models.CharField(default=0, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='link_720',
            field=models.CharField(default=0, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='main_img',
            field=models.ImageField(default=0, upload_to='upload/main_img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='online',
            field=models.CharField(default=0, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='screenshot1',
            field=models.ImageField(default=0, upload_to='upload/screenshots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='screenshot2',
            field=models.ImageField(default=0, upload_to='upload/screenshots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='screenshot3',
            field=models.ImageField(default=0, upload_to='upload/screenshots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='screenshot4',
            field=models.ImageField(default=0, upload_to='upload/screenshots'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainbody',
            name='yt_link',
            field=models.CharField(default=0, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainbody',
            name='title',
            field=models.CharField(max_length=1500),
        ),
    ]