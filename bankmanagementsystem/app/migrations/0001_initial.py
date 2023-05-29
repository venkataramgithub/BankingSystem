# Generated by Django 3.0.14 on 2023-05-12 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_info',
            fields=[
                ('AccountNumber', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('AccountTitle', models.CharField(max_length=250)),
                ('AccountType', models.CharField(max_length=250)),
                ('Balance', models.CharField(max_length=250)),
                ('AccountStatus', models.CharField(default='Active', max_length=250)),
                ('ActivationDate', models.DateField(auto_now_add=True, max_length=250)),
                ('initialDeposit', models.IntegerField()),
                ('ProfilePicture', models.ImageField(max_length=250, upload_to='')),
                ('SignaturPicture', models.ImageField(max_length=250, upload_to='')),
            ],
            options={
                'db_table': 'AccountsTable',
            },
        ),
        migrations.CreateModel(
            name='Customer_info',
            fields=[
                ('Customer_id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=250)),
                ('DOB', models.DateField(max_length=8)),
                ('Gender', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=250)),
                ('Phone', models.BigIntegerField()),
                ('Street', models.CharField(max_length=250)),
                ('City', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
                ('PinCode', models.CharField(max_length=250)),
                ('AadharNumber', models.CharField(max_length=250)),
                ('PostalAddress', models.TextField(max_length=250)),
                ('Nationality', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'CustomersTable',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=250)),
                ('Phone', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=250)),
                ('Password', models.CharField(max_length=250)),
                ('JobDescription', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='WithdrawDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.CharField(max_length=250)),
                ('TransactionType', models.CharField(max_length=250)),
                ('Date', models.DateField(auto_now_add=True, max_length=250)),
                ('Time', models.TimeField(auto_now_add=True, max_length=250)),
                ('AccountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account_info')),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer_info')),
            ],
            options={
                'db_table': 'WidthDrawDeposit',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToNumber', models.CharField(max_length=250)),
                ('Amount', models.CharField(max_length=250)),
                ('Date', models.DateField(auto_now_add=True, max_length=250)),
                ('Time', models.TimeField(auto_now_add=True, max_length=250)),
                ('FromNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account_info')),
            ],
            options={
                'db_table': 'Transfer',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('LoanType', models.CharField(max_length=250)),
                ('Amount', models.CharField(max_length=250)),
                ('File1', models.FileField(blank=True, max_length=250, upload_to='')),
                ('File2', models.FileField(blank=True, max_length=250, upload_to='')),
                ('Date', models.DateField(auto_now_add=True, max_length=250)),
                ('Time', models.TimeField(auto_now_add=True, max_length=250)),
                ('AccountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account_info')),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer_info')),
            ],
            options={
                'db_table': 'Loan',
            },
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField(max_length=8)),
                ('PanNumber', models.CharField(max_length=250)),
                ('Mobile', models.CharField(max_length=250)),
                ('DateTime', models.DateTimeField(auto_now_add=True, max_length=250)),
                ('AccountNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Account_info')),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer_info')),
            ],
            options={
                'db_table': 'DebitCard',
            },
        ),
        migrations.AddField(
            model_name='account_info',
            name='Customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer_info'),
        ),
    ]
