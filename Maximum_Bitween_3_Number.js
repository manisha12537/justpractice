// Write a python program to find a maximum between three numbers

var redline=require("readline-sync")
var a=redline.questionInt("enter number")
var b=redline.questionInt("enter number")
var c=redline.questionInt("enter number")
if(a>b & a>c){
    console.log(a,"is maximum number")
}else if(b>a & b>c){
    console.log(b,"is maximum number")
}else if(c>a & c>b){
    console.log(c,"is maximum number")
}else{
    console.log("not have maximum number all have same number")
}