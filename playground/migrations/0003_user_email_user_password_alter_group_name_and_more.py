# Generated by Django 4.2.1 on 2023-05-26 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_group_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='LoginSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(default='', max_length=100)),
                ('expire_time', models.DateTimeField(verbose_name='expire time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.user')),
            ],
        ),
    ]
