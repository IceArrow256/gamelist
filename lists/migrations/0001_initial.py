# Generated by Django 3.1.2 on 2020-10-28 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0003_auto_20201026_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameListType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='GameInList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='Score')),
                ('finished', models.DateField(blank=True, null=True, verbose_name='Finished')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('game_list_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.gamelisttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]