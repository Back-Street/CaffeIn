# Generated by Django 3.1.1 on 2020-11-14 17:46

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaffeInUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='유저 UID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('user_phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('cafeloca', models.CharField(max_length=20, verbose_name='카페주소')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_owner', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': '카페인 유저',
                'verbose_name_plural': '카페인 유저들',
                'db_table': 'users',
            },
            managers=[
                ('objects', user.models.CaffeInUserManager()),
            ],
        ),
    ]
