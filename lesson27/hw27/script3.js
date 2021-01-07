var clickBtn = document.getElementById('btn_click')

function deleteElem() {
    clickBtn.remove()
}

clickBtn.addEventListener('click', deleteElem)