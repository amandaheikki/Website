# Generated by Django 4.0.4 on 2022-05-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_startpage_delete_startinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='startpage',
            name='about_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='startpage',
            name='contact_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='startpage',
            name='services_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
