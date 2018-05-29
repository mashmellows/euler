let counter = 0
let tempArray = []
let concString = ''
let nthArray = [1,10,100,1000,10000,100000,1000000]


for (let x = 0; x < nthArray[nthArray.length - 1]; x++) {
  concString += String(x + 1)
}

for (let y = 0 ; y < concString.length; y ++) {
  counter += 1
  let number = concString.charAt(y)
  if(nthArray.includes(counter)) {
    tempArray.push(parseInt(number))
  }
}

let total = tempArray.reduce((x, y) => x * y)

console.log(tempArray)
console.log(total)
