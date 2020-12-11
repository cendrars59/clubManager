# Generated by Django 3.1.3 on 2020-12-11 11:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0010_auto_20201124_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practice',
            options={},
        ),
        migrations.RemoveField(
            model_name='practice',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='photo4',
        ),
        migrations.AlterField(
            model_name='practice',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
