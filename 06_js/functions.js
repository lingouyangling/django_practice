function hello(){
    console.log("hello world!");
}

function helloYou(name){
    console.log("hello" + name);
}

function addNum(num1, num2){
    console.log(num1 + num2);
}

function helloSomeone(name="zhu"){
    console.log("hello" + name);
}

function formal(name="Sam", title="Sir") {
    return title + " " + name;
}

function timesFive(num) {
    var result = num * 5;
    return result;
}

var v = "global v";
var stuff = "global stuff";

function fun(stuff) {
    console.log(v);
    stuff = "reassign stuff inside func";
    console.log(stuff);
}
