# Generated by Django 5.0.7 on 2024-08-29 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0002_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Startdate', models.DateField()),
                ('duration', models.CharField(max_length=100)),
                ('activitys', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demo', to='Trip.demo')),
            ],
        ),
        migrations.DeleteModel(
            name='ActivityPlan',
        ),
    ]
