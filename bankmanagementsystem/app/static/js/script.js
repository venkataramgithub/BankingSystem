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
	document.getElementById("debit-table").style.display="none";
	document.getElementById("loan-table").style.display="none";
	document.getElementById("credit-table").style.display="block";
	document.getElementById("transfer-table").style.display="none";
	document.getElementById("1").style.color="orange";
	document.getElementById("2").style.color="black";
	document.getElementById("3").style.color="black";
	document.getElementById("4").style.color="black";
}

function creditfunction() {
	document.getElementById("debit-table").style.display="block";
	document.getElementById("loan-table").style.display="none";
	document.getElementById("credit-table").style.display="none";
	document.getElementById("transfer-table").style.display="none";
	document.getElementById("1").style.color="black";
	document.getElementById("2").style.color="orange";
	document.getElementById("3").style.color="black";
	document.getElementById("4").style.color="black";
}

function transferfunction(){
	document.getElementById("debit-table").style.display="none";
	document.getElementById("loan-table").style.display="none";
	document.getElementById("credit-table").style.display="none";
	document.getElementById("transfer-table").style.display="block";
	document.getElementById("1").style.color="black";
	document.getElementById("2").style.color="black";
	document.getElementById("3").style.color="orange";
	document.getElementById("4").style.color="black";
}

function loanfunction(){
	document.getElementById("debit-table").style.display="none";
	document.getElementById("loan-table").style.display="block";
	document.getElementById("credit-table").style.display="none";
	document.getElementById("transfer-table").style.display="none";
	document.getElementById("1").style.color="black";
	document.getElementById("2").style.color="black";
	document.getElementById("3").style.color="black";
	document.getElementById("4").style.color="orange";
}
function showform(){
	document.getElementById("alert-box").style.display="none";
}
