from django.db import models

class Customer_info(models.Model):
	Customer_id=models.CharField(max_length=250,primary_key=True)
	CustomerName=models.CharField(max_length=250)
	DOB=models.DateField(max_length=8)
	Gender=models.CharField(max_length=250)
	Email=models.EmailField(max_length=250)
	Phone=models.BigIntegerField()
	Street=models.CharField(max_length=250)
	City=models.CharField(max_length=250)
	State=models.CharField(max_length=250)
	PinCode=models.CharField(max_length=250)
	AadharNumber=models.CharField(max_length=250)
	PostalAddress=models.TextField(max_length=250)
	Nationality=models.CharField(max_length=250)
	class Meta:
		db_table="CustomersTable"
	def __str__(self):
		return str(self.Customer_id)

class Account_info(models.Model):
	AccountNumber=models.CharField(max_length=250,primary_key=True)
	AccountTitle=models.CharField(max_length=250)
	AccountType=models.CharField(max_length=250)
	Customer_id=models.ForeignKey(Customer_info,on_delete=models.CASCADE)
	Balance=models.CharField(max_length=250)
	AccountStatus=models.CharField(default="Active",max_length=250)
	ActivationDate=models.DateField(max_length=250,auto_now_add=True)
	initialDeposit=models.IntegerField()
	ProfilePicture=models.ImageField(max_length=250)
	SignaturPicture=models.ImageField(max_length=250,null=True)
	class Meta:
		db_table="AccountsTable"
	def __str__(self):
		return str(self.AccountNumber)

class WithdrawDeposit(models.Model):
	AccountNumber=models.ForeignKey(Account_info,on_delete=models.CASCADE)
	Customer_id=models.ForeignKey(Customer_info,on_delete=models.CASCADE)
	Amount=models.CharField(max_length=250)
	TransactionType=models.CharField(max_length=250)
	Date=models.DateField(auto_now_add=True,max_length=250)
	Time=models.TimeField(max_length=250,auto_now_add=True)
	Status=models.CharField(default="incomplete",max_length=250)
	class Meta:
		db_table="WidthDrawDeposit"
	def __str__(self):
		return str(self.AccountNumber)

class Transfer(models.Model):
	FromNumber=models.ForeignKey(Account_info,on_delete=models.CASCADE)
	ToNumber=models.CharField(max_length=250)
	Amount=models.CharField(max_length=250)
	Date=models.DateField(auto_now_add=True,max_length=250)
	Time=models.TimeField(max_length=250,auto_now_add=True)
	status=models.CharField(max_length=250,default="incomplete")
	class Meta:
		db_table="Transfer"
	def __str__(self):
		return str(self.FromNumber)

class DebitCard(models.Model):
	Customer_id=models.ForeignKey(Customer_info,on_delete=models.CASCADE)
	AccountNumber=models.ForeignKey(Account_info,on_delete=models.CASCADE)
	DOB=models.DateField(max_length=8)
	PanNumber=models.CharField(max_length=250)
	Mobile=models.CharField(max_length=250)
	DateTime=models.DateTimeField(auto_now_add=True,max_length=250)
	class Meta:
		db_table="DebitCard"
	def __str__(self):
		return str(self.AccountNumber)

class Loan(models.Model):
	Customer_id=models.ForeignKey(Customer_info,on_delete=models.CASCADE)
	AccountNumber=models.ForeignKey(Account_info,on_delete=models.CASCADE)
	Name=models.CharField(max_length=250)
	LoanType=models.CharField(max_length=250)
	Amount=models.CharField(max_length=250)
	File1=models.FileField(max_length=250,blank=True)
	File2=models.FileField(max_length=250,blank=True)
	Date=models.DateField(max_length=250,auto_now_add=True)
	Time=models.TimeField(max_length=250,auto_now_add=True)
	status=models.CharField(max_length=250,default="incomplete")
	class Meta:
		db_table="Loan"
	def __str__(self):
		return str(self.AccountNumber)

class Employee(models.Model):
	UserId=models.CharField(max_length=250)
	Name=models.CharField(max_length=250)
	Phone=models.CharField(max_length=250)
	Email=models.EmailField(max_length=250)
	Password=models.CharField(max_length=250)
	JobDescription=models.CharField(max_length=250)
	class Meta:
		db_table="Employee"
	def __str__(self):
		return str(self.UserId)
