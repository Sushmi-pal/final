# Generated by Django 2.2.3 on 2021-02-15 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='UserReview',
        ),
    ]
