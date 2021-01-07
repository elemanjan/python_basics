let text = []
for(var i = 0; i < 3; i++){
    text[i] = document.getElementsByTagName('p')[i]
    console.log(text[i].innerHTML)
}

text[0].style.fontSize = "150%"
let col = ['red', 'green', 'yellow']

for(let i = 0; i < col.length; i++){
    text[i].style.color = col[i].toString()
}
