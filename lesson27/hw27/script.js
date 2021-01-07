var clickBtn = document.getElementById('btn_click')
var div1 = document.getElementById('div1')

function add() {
    var newInput = document.createElement("input");
    var newBr = document.createElement("br");
    document.body.insertBefore(newBr, div1);
    document.body.insertBefore(newInput, div1);
}

clickBtn.addEventListener('click', add)