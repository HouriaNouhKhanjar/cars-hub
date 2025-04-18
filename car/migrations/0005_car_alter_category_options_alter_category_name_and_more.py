# Generated by Django 4.2.20 on 2025-04-18 13:31

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('approved', models.IntegerField(choices=[(0, 'Not Approved'), (1, 'Approved')], default=0)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='car.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_cars', to='car.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
