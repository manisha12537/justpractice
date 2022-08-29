// Write a python program to input any alphabet and check whether it is vowel or consonant.


var redline=require("readline-sync")
var data=redline.question("enter the data")
if(data=="a"|| data=="e"|| data=="i"|| data==="o"|| data=="u"){
    console.log("it is vowel")
}else if(data=="b"|| data=="c"& data!="d"& data!="f"& data!="j","k","l","m","n","o","p","q","r","s","t"){
    console.log("it is consonant")
}
else{
    console.log("enter only alphabet")
}