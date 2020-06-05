# Generated by Django 3.0.7 on 2020-06-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refferal_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddIndex(
            model_name='referrallinks',
            index=models.Index(fields=['refferal_id'], name='user_referr_reffera_1730a2_idx'),
        ),
    ]
