var clickBtn = document.getElementById('btn_click')
var textInput = document.getElementById('text')
var pText = document.getElementById('pText')
let msg = ''

document.addEventListener('keydown', function(event){
    if(event.keyCode === 13){
        btnClick()
    }
})

function btnClick(){
    // alert(msg)
    pText.innerHTML = msg
}

textInput.addEventListener('input', function(event){
    msg = event.target.value
    console.log('input works!')
})

clickBtn.addEventListener('click', btnClick)