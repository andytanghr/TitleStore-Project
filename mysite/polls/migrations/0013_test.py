# Generated by Django 2.0.5 on 2018-05-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180518_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Nancy', max_length=200)),
            ],
        ),
    ]