# Generated by Django 3.1.3 on 2020-11-07 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizs',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_ans', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
