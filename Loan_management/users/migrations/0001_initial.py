# Generated by Django 5.0.2 on 2024-03-30 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.roles')),
            ],
        ),
        migrations.CreateModel(
            name='User_Activity_Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('activity_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
