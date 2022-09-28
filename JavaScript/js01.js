// alert('hello python');
// while循环

var i = 0;
while (i<3){
    console.log(i);
    i++;
}

//for循环
for (var j=0;j<5;j++){
    console.log(j)
}

// for in
var aList = Array(11,22,33,44,55)
for (i in aList){
    // 遍历出来是下标索引
    console.log(i);
    console.log(aList[i]);
}

var objA = {
    name: 'test',
    age: 18,
    gender: '男'
}
for (i in objA){
    console.log(i);
    console.log(objA[i]);
}