var name = prompt("what's your name?");
var age = prompt("how old are you?");
var height = prompt("how tall are you?");
var pname = prompt("what's your pet's name?");

if (
    name.split()[0][0] == name.split()[1][0]
    && age >20 && age < 30
    && height >= 170
    && pname[pname.length - 1] == "y") {
    console.log("spy");
}
