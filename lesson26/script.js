let text = []
for(var i = 0; i < 3; i++){
    text[i] = document.getElementsByTagName('p')[i]
    text[i].innerHTML = prompt('p').toString()
}

