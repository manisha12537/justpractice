// Write a python program to check whether a number is negative, positive or zero.

var redline=require("readline-sync")
var number=redline.questionInt("enter the number")
if(number>0){
    console.log(number,"is positive number")
}else if(number<0){
    console.log(number,"is nagative number")
}else if(number==0){
    console.log(number,"is zero")
}
else{
    console.log("please enter the valid number")
}