# Generated by Django 4.0.5 on 2022-06-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('media', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
