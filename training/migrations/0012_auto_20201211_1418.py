# Generated by Django 3.1.3 on 2020-12-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_auto_20201211_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='practice',
            options={'verbose_name': 'practice', 'verbose_name_plural': 'practices'},
        ),
        migrations.RemoveField(
            model_name='practice',
            name='material',
        ),
    ]