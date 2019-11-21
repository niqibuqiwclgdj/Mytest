/* var checklist = document.getElementById("checklist")

var items = checklist.querySelectorAll("li");
var inputs = checklist.querySelectorAll("input");

for(var i = 0 ; i < items.length ; i++){
	items[i].addEventListener("click" , editItem);
	inputs[i].addEventListener("blur" , updateItem);
	inputs[i].addEventListener("keypress" , itemKeypress);
}

function editItem(){
	this.className = "edit";
	var input = this.querySelector("input");
	input.focus();
	console.log(input.value.length)
	input.setSelectionRange(0 , input.value.length)
}

function updateItem(){
	this.previousElementSibling.innerHTML = this.value;
	this.parentNode.className = "";
}

function itemKeypress(event){
	if(event.keyCode == 13){
		updateItem.call(this);
	}
}  */
//文本全部加载完后获取checklist并为其赋值
var checklist = document.getElementById("checklist")

//取出所有在checklist里的li和input属性
var items = checklist.querySelectorAll("li")
var inputs = checklist.querySelectorAll("input")

//循环，为每个都添加各自的函数操作
for (var i = 0 ; i < items.length ; i ++){
	items[i].addEventListener("click" , editItem)
	inputs[i].addEventListener("blur" , updateItem)
	inputs[i].addEventListener("keypress" , itemKeypress)
}

function editItem(){
	this.className = "edit";
	var input = this .querySelector("input");
	//鼠标聚焦
	input.focus();
	input.setSelectionRange(0 , input.value.length)
}

//文本被修改时的函数
function updateItem(){
	this.previousElementSibling.innerHTML = this.value;
	this.parentNode.className = "";
}

//鼠标按下时的函数
function itemKeypress(){
	if(event.keyCode == 13){
		updateItem.call(this);
	}
}
