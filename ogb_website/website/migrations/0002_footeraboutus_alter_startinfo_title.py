# Generated by Django 4.0.4 on 2022-05-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='startinfo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]