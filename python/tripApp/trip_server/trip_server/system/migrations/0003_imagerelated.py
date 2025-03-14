# Generated by Django 4.2.16 on 2024-11-01 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0001_initial'),
        ('system', '0002_alter_slider_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('img', models.ImageField(max_length=256, upload_to='%Y%m/file/', verbose_name='图片')),
                ('summary', models.CharField(blank=True, max_length=32, null=True, verbose_name='图片说明')),
                ('object_id', models.IntegerField(verbose_name='关联模型')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(null=True, on_delete=models.SET(None), related_name='upload_image', to='accounts.user', verbose_name='上传的用户')),
            ],
            options={
                'db_table': 'system_image_related',
            },
        ),
    ]
