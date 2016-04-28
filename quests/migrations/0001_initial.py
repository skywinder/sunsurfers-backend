# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('minimum_should_after', models.IntegerField()),
                ('must_after', models.ManyToManyField(related_name='_quest_must_after_+', to='quests.Quest')),
                ('should_after', models.ManyToManyField(related_name='_quest_should_after_+', to='quests.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='QuestMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('PHOTO', 'Photo'), ('VIDEO', 'Video'), ('SOUND', 'Sound'), ('TEXT', 'Text'), ('URL', 'Url')], max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_opened', models.DateTimeField()),
                ('date_start', models.DateTimeField()),
                ('date_finish', models.DateTimeField()),
                ('state', models.CharField(choices=[('NEW', 'New quest'), ('DECLINED', 'Declined'), ('OUTDATED', 'Outdated'), ('OPENED', 'User has seen this quest'), ('STARTED', 'User accepted the quest'), ('FINISHED', 'Finished')], max_length=255)),
                ('confirmed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confirmed_quests', to=settings.AUTH_USER_MODEL)),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issued_quests', to=settings.AUTH_USER_MODEL)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quests.Quest')),
                ('surfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questmedia',
            name='surfer_quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quests.UserQuest'),
        ),
    ]
