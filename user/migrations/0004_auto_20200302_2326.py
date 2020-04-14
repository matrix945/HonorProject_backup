# Generated by Django 2.0.8 on 2020-03-03 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parent', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_principal', models.BooleanField(default=False)),
                ('phone', models.CharField(default='', max_length=60)),
                ('description', models.TextField(default='')),
                ('full_name', models.CharField(default='', max_length=60)),
            ],
            options={
                'verbose_name': '帐户管理',
                'verbose_name_plural': '帐户管理',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]