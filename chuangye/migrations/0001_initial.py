# Generated by Django 2.2.8 on 2020-01-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cygsdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='公司名')),
                ('lianjie', models.CharField(max_length=300, verbose_name='公司名链接')),
                ('cltime', models.CharField(max_length=50, verbose_name='成立时间')),
                ('place', models.CharField(max_length=50, verbose_name='地点')),
                ('industry', models.CharField(max_length=50, verbose_name='行业')),
                ('lunci', models.CharField(max_length=100, verbose_name='轮次')),
                ('rzsum', models.CharField(max_length=10, verbose_name='融资总额')),
            ],
            options={
                'verbose_name': '公司详情',
                'verbose_name_plural': '公司详情',
            },
        ),
    ]
