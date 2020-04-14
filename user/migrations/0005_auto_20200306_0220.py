# Generated by Django 2.0.8 on 2020-03-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200302_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_parent',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_principal',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_teacher',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(choices=[('1', 'Under 18'), ('18', '18-24'), ('25', '25-34'), ('35', '35-44'), ('45', '45-49'), ('50', '50-55'), ('56', '56+')], default='', max_length=4),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M'), ('N/A', 'N/A')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(choices=[('0:', 'other'), ('1:', 'academic/educator'), ('2:', 'artist'), ('3:', 'clerical/admin'), ('4:', 'N'), ('5:', 'N'), ('6:', 'N'), ('7:', 'N'), ('8:', 'N'), ('9:', 'N'), ('10', 'N'), ('11', 'N'), ('12', 'N'), ('13', 'N'), ('14', 'N'), ('15', 'N'), ('16', 'N'), ('17', 'N'), ('18', 'N'), ('19', 'N'), ('20', 'N')], default='', max_length=100),
        ),
    ]