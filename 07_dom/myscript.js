var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

console.log("connected!");

headOne.addEventListener("mouseover", function(){
    headOne.textContent = "mouse currently over";
    headOne.style.color = "red";
})

headOne.addEventListener("mouseout", function(){
    headOne.textContent = "hover over me";
    headOne.style.color = "black";
})

headTwo.addEventListener("click", function(){
    headTwo.textContent = "clicked on";
    headTwo.style.color = 'blue';
})

headThree.addEventListener("dblclick", function(){
    headThree.textContent = "double clicked";
    headThree.style.color = 'green';
})
