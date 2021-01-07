var clickBtn = document.getElementById('btn_click')

function changeColor() {
    var colorBtn = prompt('Enter color')
    clickBtn.style.color = colorBtn.toString()
}

clickBtn.addEventListener('click', changeColor)