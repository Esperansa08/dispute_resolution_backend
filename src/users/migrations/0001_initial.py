# Generated by Django 4.1 on 2023-10-19 13:31

import django.core.validators
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Адрес электронной почты')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона может состоять только из цифр', regex='^\\d+$')])),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('mediator', 'Медиатор'), ('admin', 'Администратор')], default='user', max_length=100, verbose_name='Роль')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Участник сообщества',
                'verbose_name_plural': 'Участники сообщества',
                'ordering': ('email',),
            },
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]