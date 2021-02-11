# Generated by Django 3.1.5 on 2021-02-07 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logistic',
            fields=[
                ('trackId', models.CharField(default='AD65598ED4', max_length=20, primary_key=True, serialize=False)),
                ('sender', models.CharField(max_length=50, verbose_name='Sender Full name')),
                ('sender_email', models.EmailField(max_length=225, verbose_name='Sender Email')),
                ('sender_contact', models.CharField(max_length=30, verbose_name='Sender contact')),
                ('origin', models.CharField(default='none', max_length=225, verbose_name='Origin')),
                ('Paid', models.CharField(max_length=30, verbose_name='sender paid')),
                ('recipient', models.CharField(max_length=50, verbose_name='Recipient Full name')),
                ('recipient_email', models.EmailField(max_length=225, verbose_name='Recipient Email')),
                ('recipient_contact', models.CharField(max_length=30, verbose_name='Recipient contact')),
                ('destination', models.CharField(default='none', max_length=225, verbose_name='Destination')),
                ('volume', models.CharField(max_length=50, verbose_name='Weight Volume')),
                ('weight', models.CharField(max_length=50, verbose_name='Physical Weight')),
                ('date', models.DateField(auto_now_add=True, max_length=50, verbose_name='Issued Date')),
                ('timestap', models.TimeField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
            ],
            options={
                'ordering': ['timestap'],
            },
        ),
        migrations.CreateModel(
            name='PaymentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acc_name', models.CharField(max_length=50, verbose_name='Account Name')),
                ('Acc_number', models.CharField(max_length=30, verbose_name='Account Number')),
                ('bank', models.CharField(max_length=50, verbose_name='Bank')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=225, verbose_name='Clearance Event')),
                ('Location', models.CharField(max_length=225, verbose_name='Location')),
                ('timestap', models.TimeField(auto_now_add=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('logistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.logistic')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]