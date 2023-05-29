from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
from app.functions.functions import handle_uploaded_file

def login(request):
	if request.method=="POST":
		userid=request.POST['username']
		Password=request.POST['password']
		form=Employee.objects.filter(UserId=userid) & Employee.objects.filter(Password=Password)
		if(len(form)==1):
			request.session['userid']=userid
			return redirect("home/")
		else:
			messages.success(request,"Username and password are incorrect")
			return redirect("/")
	else:	
		return render(request,'login.html')
def CustomerInfo(request):
	if request.method=="POST":
		customerid=request.POST['customerid']
		customername=request.POST['customername']
		dateofbirth=request.POST['dateofbirth']
		gender=request.POST['gender']
		email=request.POST['email']
		phone=request.POST['phone']
		street=request.POST['street']
		city=request.POST['city']
		state=request.POST['State']
		pincode=request.POST['pincode']
		aadharnumber=request.POST['aadharnumber']
		postaladdress=request.POST['postaladdress']
		nationality=request.POST['nationality']
		if(len(Customer_info.objects.filter(AadharNumber__iexact=aadharnumber))==0):
			form=Customer_info(Customer_id=customerid,CustomerName=customername,DOB=dateofbirth,Gender=gender,Email=email,Phone=phone,Street=street,City=city,State=state,PinCode=pincode,AadharNumber=aadharnumber,PostalAddress=postaladdress,Nationality=nationality)
			try:
				form.save()
				messages.success(request,'Form Submitted')
				print("form submitted")
				return redirect("/customerinfo/")
			except:
				messages.error(request,'Data Not Submitted')
				print("Form Not Submitted")
				return redirect("/customerinfo/")
		else:
			messages.warning(request,"AadharNumber Already Exist")
			return redirect("/customerinfo/")
	else:
		return render(request,'customer.html')

def createaccount(request):
	if request.method=="POST":
		accountnumber=request.POST['accountnumber']
		accounttitle=request.POST['accounttitle']
		accounttype=request.POST['accounttype']
		customerid=request.POST['customerid']
		balance=request.POST['balance']
		initialdeposit=request.POST['initialdeposit']
		ppicture=request.FILES['ppicture']
		spicture=request.FILES['spicture']
		if(Account_info.objects.filter(AccountNumber=accountnumber).count()==0):
			form=Customer_info.objects.get(Customer_id=customerid)
			if(Account_info.objects.filter(Customer_id=customerid).count()==0):
				createform=Account_info(AccountNumber=accountnumber,AccountTitle=accounttitle,AccountType=accounttype,Customer_id=form,Balance=balance,initialDeposit=initialdeposit,ProfilePicture=ppicture,SignaturPicture=spicture)
				try:
					createform.save()
					handle_uploaded_file(ppicture)
					handle_uploaded_file(spicture)
					messages.success(request,'Form Submitted')
					return redirect("/createaccount/")
				except:
					messages.error(request,'Data Not Submitted')
					return redirect("/createaccount/")
			else:
				messages.error(request,'CustomerId Not Matched')
				return redirect("/createaccount/")
		else:
			messages.error(request,'Account Number Already Exist')
			return redirect("/createaccount/")
	else:
		lastaccount=Account_info.objects.all()[::-1]
		return render(request,"createaccount.html",{'lastaccount':lastaccount})

def home(request):
	return render(request,'home.html')

def balancecheck(request):
	if request.method=="POST":
		accountno=request.POST['accountno']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		return render(request,'balancecheck.html',{'form':form,'customerform':customerform})
	else:
		return render(request,'balancecheck.html')


def updateaccount(request):
	if request.method=="POST":
		search=request.POST['search']
		form=Account_info.objects.get(AccountNumber__iexact=search)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		return render(request,'updateaccount.html',{'form':form,'customerform':customerform})
	else:
		return render(request,'updateaccount.html')


def withdrawl(request):
	if request.method=="POST":
		accountno=request.POST['accountno']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		return render(request,'withdrawl.html',{'form':form,'customerform':customerform})
	return render(request,'withdrawl.html')

def completewithdrawl(request):
	if request.method=="POST":
		accountno=request.POST['accountno']
		amount=request.POST['amount']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		form=WithdrawDeposit(AccountNumber=form,Customer_id=customerform,Amount=amount,TransactionType="Withdrawl")
		try:
			form.save()
			messages.success(request,'form submitted')
			return redirect("/withdrawl/")
		except:
			messages.error(request,'data not submitted')
			return redirect("/withdrawl/")
	else:
		return redirect("/withdrawl/")

def deposit(request):
	if request.method=="POST":
		accountno=request.POST['accountno']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		return render(request,'deposit.html',{'form':form,'customerform':customerform})
	return render(request,'deposit.html')

def completedeposit(request):
	if request.method=="POST":
		accountno=request.POST['accountno']
		amount=request.POST['amount']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		form=WithdrawDeposit(AccountNumber=form,Customer_id=customerform,Amount=amount,TransactionType="Deposit")
		try:
			form.save()
			messages.success(request,'form submitted')
			return redirect("/deposit/")
		except:
			messages.error(request,'data not submitted')
			return redirect("/deposit/")
	else:
		return redirect("/deposit/")

def transfer(request):
	if request.method=="POST":
		fromnumber=request.POST['fromnumber']
		tonumber=request.POST['tonumber']
		amount=request.POST['amount']
		fromaccount=Account_info.objects.get(AccountNumber__iexact=fromnumber)
		toaccount=Account_info.objects.get(AccountNumber__iexact=tonumber)
		form=Transfer(FromNumber=fromaccount,ToNumber=toaccount,Amount=amount)
		try:
			form.save()
			messages.success(request,'Form Submitted')
			return redirect('/transfer/')
		except:
			messages.error(request,'Form Not Submitted')
			return redirect('/transfer/')
	else:
		return render(request,'transfer.html')

def alltransactions(request):
	if request.method=="POST":
		searchname=request.POST['search']
		form=WithdrawDeposit.objects.filter(AccountNumber=searchname)
		return render(request,'alltransactions.html',{'form':form})

	else:
		form=WithdrawDeposit.objects.all()
		return render(request,'alltransactions.html',{'form':form})

def viewapprovedtransaction(request):
	form=WithdrawDeposit.objects.filter(Status__iexact="incomplete") & WithdrawDeposit.objects.filter(TransactionType__iexact="Deposit")
	form1=Loan.objects.filter(status__iexact="incomplete")
	form2=WithdrawDeposit.objects.filter(Status__iexact="incomplete") & WithdrawDeposit.objects.filter(TransactionType__iexact="Withdrawl")
	form3=Transfer.objects.filter(status__iexact="incomplete")
	return render(request,'viewapprovedtransaction.html',{'form':form,"form1":form1,"form2":form2,"form3":form3})

def debitcard(request):
	if request.method=="POST":
		accountno=request.POST['accountnumber']
		datoofbirth=request.POST['dateofbirth']
		pannumber=request.POST['pancardnumber']
		mobile=request.POST['mobile']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		debitcard=DebitCard(Customer_id=customerform,AccountNumber=form,DOB=datoofbirth,PanNumber=pannumber,Mobile=mobile)
		try:
			debitcard.save()
			messages.success(request,'form submitted')
			return redirect("/debitcard/")
		except:
			messages.error(request,'data not submitted')
			return redirect("/debitcard/")
	else:	
		return render(request,'debitcard.html')

def applyloan(request):
	if request.method=="POST":
		accountno=request.POST['accountnumber']
		name=request.POST['name']
		loantype=request.POST['loantype']
		amount=request.POST['amount']
		document1=request.FILES['file1']
		document2=request.FILES['file2']
		form=Account_info.objects.get(AccountNumber__iexact=accountno)
		customerform=Customer_info.objects.get(Customer_id__iexact=form.Customer_id)
		loanform=Loan(Customer_id=customerform,AccountNumber=form,Name=name,LoanType=loantype,Amount=amount,File1=document1,File2=document2)
		try:
			loanform.save()
			messages.success(request,'form submitted')
			return redirect("/applyloan/")
		except:
			messages.error(request,'data not submitted')
			return redirect("/applyloan/")
	else:
		return render(request,'applyloan.html')

def allcustomers(request):
	form=Customer_info.objects.all()
	customerform=Account_info.objects.all()
	return render(request,'allcustomers.html',{'form':form,"customerform":customerform})

def depositclear(request,AccountNumber,Amount,id):
	form=Account_info.objects.get(AccountNumber__iexact=AccountNumber)
	depositform=WithdrawDeposit.objects.get(id=id)
	amount=form.Balance
	Amount=Amount+int(amount)
	form.Balance=Amount
	depositform.Status="Complete"
	try:
		form.save()
		depositform.save()
	except:
		print("form not saved")
	return redirect("/viewapprovedtransaction/")

def withdrawclear(request,AccountNumber,Amount,id):
	form=Account_info.objects.get(AccountNumber__iexact=AccountNumber)
	withdrawform=WithdrawDeposit.objects.get(id=id)
	amount=form.Balance
	Amount=int(amount)-Amount
	form.Balance=Amount
	withdrawform.Status="Complete"
	try:
		form.save()
		withdrawform.save()
	except:
		print("Form Not Saved")
	return redirect("/viewapprovedtransaction/")

def clearloan(request,AccountNumber,Amount,id):
	form=Account_info.objects.get(AccountNumber__iexact=AccountNumber)
	loanform=Loan.objects.get(id=id)
	amount=form.Balance
	Amount=int(amount)+Amount
	form.Balance=Amount
	loanform.status="Complete"
	try:
		form.save()
		loanform.save()
	except:
		print("Form Not Saved")
	return redirect("/viewapprovedtransaction/")

def cleartransfer(request,FromNumber,ToNumber,Amount,id):
	Fromform=Account_info.objects.get(AccountNumber__iexact=FromNumber)
	Toform=Account_info.objects.get(AccountNumber__iexact=ToNumber)
	transferform=Transfer.objects.get(id=id)
	fromamount=Fromform.Balance
	toamount=Toform.Balance
	FromAmount=int(fromamount)-Amount
	ToAmount=int(toamount)+Amount
	Fromform.Balance=FromAmount
	Toform.Balance=ToAmount
	transferform.status="Complete"
	try:
		Fromform.save()
		Toform.save()
		transferform.save()
	except:
		print("Form Not Saved")
	return redirect("/viewapprovedtransaction/")

def logout(request):
	del request.session['userid']
	return redirect("/")