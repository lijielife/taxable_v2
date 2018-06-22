# Generated by Django 2.0.5 on 2018-06-07 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='所在区域')),
            ],
            options={
                'verbose_name_plural': '所在区域',
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='所在区县')),
            ],
            options={
                'verbose_name_plural': '所在区县',
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='房型')),
            ],
            options={
                'verbose_name_plural': '房型',
                'db_table': 'House',
            },
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='小区名称')),
                ('orientation', models.CharField(max_length=64, verbose_name='朝向')),
                ('design', models.CharField(max_length=32, verbose_name='户型')),
                ('acreage', models.IntegerField(verbose_name='面积')),
                ('price', models.IntegerField(verbose_name='成交价格')),
                ('total_floor', models.IntegerField(verbose_name='总楼层')),
                ('floor', models.IntegerField(verbose_name='所在楼层')),
                ('element', models.IntegerField(verbose_name='楼栋号')),
                ('vouch_price', models.IntegerField(verbose_name='核定评估价')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proscenium.Area')),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proscenium.House')),
            ],
            options={
                'verbose_name_plural': '小区',
                'db_table': 'Plot',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='评估价体系')),
                ('country', models.ManyToManyField(to='proscenium.Country')),
            ],
            options={
                'verbose_name_plural': '评估价体系',
                'db_table': 'System',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=64, verbose_name='建成年代')),
            ],
            options={
                'verbose_name_plural': '建成年代',
                'db_table': 'Time',
            },
        ),
        migrations.AddField(
            model_name='plot',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proscenium.Time'),
        ),
        migrations.AddField(
            model_name='area',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proscenium.Country'),
        ),
    ]
