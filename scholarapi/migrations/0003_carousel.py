# Generated by Django 3.2.12 on 2022-04-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarapi', '0002_college_college_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_image', models.FileField(null=True, upload_to='carousels/', verbose_name='Carousel Image')),
                ('carousel_heading', models.CharField(max_length=500, verbose_name='Heading')),
                ('carousel_description', models.CharField(max_length=500, verbose_name='Description')),
            ],
        ),
    ]
