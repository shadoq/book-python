# Generated by Django 2.1.1 on 2018-12-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook', '0003_auto_20181205_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(db_index=True, max_length=30, verbose_name='Last Name'),
        ),
    ]