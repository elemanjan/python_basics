var resultBtn = document.getElementById('btn_click')
var textInput1 = document.getElementById('text1')
var textInput2 = document.getElementById('text2')
var oper = document.getElementById('oper')
let value1 = 0
let value2 = 0
let operVal = ''
let result = document.getElementById('result')

function btnClick(){
    switch(operVal){
        case '+':
            result.innerHTML = Number(value1) + Number(value2)
            break
        case '-':
            result.innerHTML = Number(value1) - Number(value2)
            break
        case '*':
            result.innerHTML = Number(value1) * Number(value2)
            break
        case '/':
            result.innerHTML = Number(value1) / Number(value2)
            break
    }
}

textInput1.addEventListener('change', function(event){
    value1 = event.target.value
})

textInput2.addEventListener('change', function(event){
    value2 = event.target.value
})

oper.addEventListener('change', function(event){
    operVal= event.target.value
})
resultBtn.addEventListener('click', btnClick)