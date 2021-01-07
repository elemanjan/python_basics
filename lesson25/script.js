function adminka(){
    var num = 0
    var user = prompt('Введите логин');
    if (user === 'admin'){
        while(num < 3){
            var pass = prompt('Введите пароль');
            if (pass === 'pass'){
                console.log('Добро пожаловать админ :)');
                num = 3
            }
            else{
                console.log('Пароль неверный!');
                num = num + 1
            }
        }
    }
    else{
        console.log("Логин неверный")
    }
}
adminka();
