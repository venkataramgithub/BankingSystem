function display(){
	var dom=document.getElementById("sub-list").style;
	if(dom.display=="block"){
		dom.display="none";
	}
	else{
		dom.display="block";
	}
}

function showfunction(){
	var dom=document.getElementById("user-details").style;
	if(dom.display=="block"){
		dom.display="none";
	}
	else{
		dom.display="block";
	}
}
function showpassword(){
	var dom=document.getElementById("password");
	var eyeopen=document.getElementById("eyeopen").style;
	var eyeclose=document.getElementById("eyeclose").style;
	if(dom.type=="password"){
		dom.type="text";
		eyeclose.display="none";
		eyeopen.display="block";
	}
	else{
		dom.type="password";
		eyeclose.display="block";
		eyeopen.display="none";
	}
}
function hidemessage(){
	var message=document.getElementById("message-box").style;
	message.display="none";
}

function debitfunction(){
	deposit=document.getElementById("debit-table").style;
	loan=document.getElementById("loan-table").style;
	withdrawl=document.getElementById("credit-table").style;
	transfer=document.getElementById("transfer-table").style;
	withdrawl.display="block";
	deposit.display="none";
	transfer.display="none";
	loan.display="none";
}

function creditfunction() {
	deposit=document.getElementById("debit-table").style;
	loan=document.getElementById("loan-table").style;
	withdrawl=document.getElementById("credit-table").style;
	transfer=document.getElementById("transfer-table").style;
	withdrawl.display="none";
	deposit.display="block";
	transfer.display="none";
	loan.display="none";
}

function transferfunction(){
	deposit=document.getElementById("debit-table").style;
	loan=document.getElementById("loan-table").style;
	withdrawl=document.getElementById("credit-table").style;
	transfer=document.getElementById("transfer-table").style;
	withdrawl.display="none";
	deposit.display="none";
	transfer.display="block";
	loan.display="none";
}

function loanfunction(){
	deposit=document.getElementById("debit-table").style;
	loan=document.getElementById("loan-table").style;
	withdrawl=document.getElementById("credit-table").style;
	transfer=document.getElementById("transfer-table").style;
	withdrawl.display="none";
	deposit.display="none";
	transfer.display="none";
	loan.display="block";
}
function showform(){
	alert("working");
}