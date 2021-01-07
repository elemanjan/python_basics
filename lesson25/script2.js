// let arr = [1, 2, 3]
// alert(arr)
// arr.reverse()
// alert(arr)

// let arr2 = ['a', 'b', 'c']
// alert(arr2)
// for (let i = 1; i < 4; i++){
//     arr2.push(i)
// }
// alert(arr2)

// let arr = [1, 2, 3, 4, 5]
// let arr2 = []
// arr2.push(arr[0])
// arr2.push(arr[3])
// arr2.push(arr[4])

// alert(arr2)

let arr = [1, 2, 3, 4, 5, 'a', 'b', 'c']
let num = []
let letter = []
for(let i = 0; i < arr.length; i++){
    if (arr[i] >= '0' && arr[i] <= '9'){
        num.push(arr[i])
    }
    else{
        letter.push(arr[i])
    }
}

alert(num)
alert(letter)