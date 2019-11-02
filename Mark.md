# JavaScript：

## do while和while的区别：

### 代码片段

~~~javascript
var times = 12;
do{
    console.log("tried: " + times);
    times ++;
}while (times < 20);

while(times < 20){
    console.log("try: " + timse);
    times ++;
}
~~~

1. **do while表示先去执行，再判断 ， while则先判断对错再去做。**