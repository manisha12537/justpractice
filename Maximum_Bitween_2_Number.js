// Write a python program to find the maximum between two numbers.
var a=require("readline-sync")
var b=a.questionInt("enter the number")
var c=a.questionInt("enter the number")
if(b>c){
    console.log(b,"b is greter")
}else if(c>b){
    console.log(c,"c is greter")
}else{
    console.log("not have any maximam number")
}