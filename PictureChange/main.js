/*var time = 0
while(time < 10){
  console.log("Once: " , time)
  time = time + 1
}

do{
  console.log("This is " + time);
  time = time + 1;
}while(time < 10);
name = [" ww" , 123 , "trle"]
for (i = 0 ; i<name.length() ; i++){
    console.log("www")*/

var checklist = document.getElementById("checklist")

var items = checklist.querySelectorAll("li")

for(var i = 0 ; i < items.length ; i++){
  items.addEventListener("click" , editItem);
}

function editItem(){
  console.log(this)
}