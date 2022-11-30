# Generated by Django 4.1.3 on 2022-11-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_moviecategory_options_alter_moviefile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviefile',
            name='video_format',
            field=models.CharField(choices=[('480', 'Mobile HD(480)'), ('720', 'HD(720)'), ('1080', 'Full HD(1080)')], default=0, max_length=25, verbose_name='Movie format'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moviefile',
            name='video',
            field=models.FileField(upload_to='files/', verbose_name='Movie video'),
        ),
    ]