# Chapter5 part1

**while 루프** 

while과 :(콜론)사이에 오는 조건문이 참의 값을 가지는 경우에는 :(콜론)이하의 코드가 반복해서 작동하게 됨

``` n = 5 ```

```python
 n = 5 

while n > 0 :

 print(n)
 n = n - 1 

print('Blastoff')       

print(n)
```



루프를 제어하기 위해 설계된 이 변수를 반복 변수라고 함



```python
n = 5

while n > 0:

    print('Lather')

    print('Rinse')

print('Dry off!')
```



무한 루프



```python
n = 0

while n > 0 :

    print('Lather')

    print(Rinse)

print('Dry off')
```



 제로 트립



**break** 

루프가 break를 만나게 되면 해당 루프는 실행이 종료 되고 while문 바로 뒤의 코드를 실행하게 됨



**continue** 

루프가 continue를 만나게 되면 해당 루프는 실행이 종료되고 루프가 시작된 지점부터 다시 루프를 실행하게 됨



while 키워드를 이용해 만들어온 루트는 불확정 루트라고 부른다 그 이유는 break을 만나거나

어떤 값이 참인 동안 계속해서 실행되기 때문이다



# Chapter5 part2

**for 루프** 

하나의 파일에 들어 있는 문장의 갯수와 리스트 안에 들어 있는 항목들의 수는 유한개임유한개의 항목들에 대해 우리가 특정 조치들을 취하고 싶을 때 for 루프를 사용함

```python
for i in [5, 4, 3, 2, 1]:

    print(1)

print('Blasstoff')
```



5회 반복하는 반복문을 만들고 반복 변수를 설정하기에 더욱 직접적인 문법



# Chapter5 part3

**루프의 응용**

특정조건이 참인 경우에는 반복적으로 실행되는 불확정 루프의 종류인 while문과 유한개의 요소를 가지고 있으며, 개별 요소를 모두 순회하게 되면 종료되는 for 루프를 살펴보았다

```python
print('Before')

for thing in (9, 41, 12, 3, 74 ,15)

    print(thing)

print('After')
```



이 루프는 원소를 출력하는거 외엔 아무것도 하지 않는다 처음에는 그렇게 하는것이 좋다

본인이 제대로 생각하고 있는지 확인할 수 있기 때문이다



```python
largest_so_far = -1

print('Before', largest_so_far)

for the_num in [9, 41 ,12 ,3 ,74 ,15] :

    if the_num  >  largest_so_far :

        largest_so_far = the_num

    print(largest_so_far, the_num)

print('After', largest_so_far)
```





```python
# Before -1
# largest_so_far:  9 current number:  9
# largest_so_far:  41 current number:  41
# largest_so_far:  41 current number:  12
# largest_so_far:  41 current number:  3
# largest_so_far:  74 current number:  74
# largest_so_far:  74 current number:  15
# After 74
```

9 9                 처음 본 숫자가 9고 젤크니 저장된다

41 41             41이 9보다 크니 저장된다

41 12             12는 41보다 작으니 저장되지 않는다

41 3               3은 41보다 작으니 저장되지 않는다

74 74             74이 41보다 크니 저장된다

74 15            15는 74보다 작으니 저장되지 않는다

After 74       제일 큰 74가 출력된다



# Chapter5 part4

**1. 루프를 사용하여 개수 세기**

리스트에 몇 개의 원소가 있는지를 알고자 할 때 우리는 루프를 사용할 수 있음

```python
zork = 0
print('Before, zork')
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)
```

```python
# Before 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# 6 15
# After 6
```

After값은 숫자가 몇개인지 알려주는 값이 될 수도 있지만 루프가 몇번 반복 실행되었는지 보여주는

값이기도 하다



**2. 루프를 사용하여 합계 구하기**

각 원소를 누적해서 더해 총합을 알아 낼 수도 있음

```python
zork = 0
print('Before, zork')
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)
```

```python
# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154
```

원소의 값을 연속적으로 받고 매 실행마다 누계를 가져와 저희가 확인한 thing을 더합니다



**3. 루프를 사용하여 평균 구하기**

원소의 수와 총합을 활용하면 우리는 평균을 구할 수도 있음

```python
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
```

```python
# Before 0 0
# 1 9 9
# 2 50 41
# 3 62 12
# 4 65 3
# 5 139 74
# 6 154 15
# After 6 154 25.666666666666668
```

매 번 루프를 실행할 때마다 count = count +1과 누계를 얻을 수 있고 여기에 나타난다

for 루프의 어떤 순간 마지막 계산을 하고 for 루프에서 빠져나와 나눕니다

6과 156이 원소의 개수와 누계이며 sum을 count로 나누어 평균을 구합니다



  

**4. 루프를 사용하여 필터링 하기**

특정 값보다 큰 수를 print를 이용해 확인 할 수 있습니다.

```python
print('Before')
for value in [9, 41, 12 3, 74, 15] :
    if value > 20:
        print('Large number',value)
print('After')
```

```python
# Before
# Large number 41
# Large number 74
# After
```

 20보다 큰 수를 찾는 탐색문입니다

저희가 루프로 읽는 큰 집합에서 무언가를 선택하거나 탐색해야할때 사용할 수 있습니다.



**5. 부울값을 사용하여 특정 값을 검색하기**

우리가 원하는 특정 값이 list에 있는지 확인 할 수 있습니다. 부울 변수를 이용하게 됩니다. 부울 변수는 True(참) 또는 False(거짓)의 값을 가지게 됩니다.

```python
found = false
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)
```

```python
# Before False
# False 9
# False 41
# False 12
# True 3
# True 74
# True 15
# After True
```

특정한 값이 존재하는지 알고 싶을 때 불리언 변수를 사용한다

1, 42와 같은 정수형 변수와 98.6과 같은 실수형 변수  

따옴표와 함께 적인 Hello world같은 문자열 변수

if구문이 value ==3 불리언 값을 반환한다

3을 찾으면 기본적으로 found는 True로 바뀌기 전까지 False값을 유지한다

하지만 found값을 False로 되돌리는 코드가 없다 그래서 한 번 3을 발견하고 나면 True 값으로 남는다

이거 보다 효율적인 코드는 6번에 있다



**6. 가장 작은 수를 찾는 코드 완성하기**

가장 작은 수를 찾는 루프를 완성하기 위해서는 우리는 None 자료형에 대해서 알아야 합니다. None은 값이 없다는 것을 말합니다. 하나의 빈 상자에 이 상자는 비어 있습니다라고 명시적으로 표시하고 있다고 생각하면 될 듯합니다.

또한 "is"와 "is not"의 연산자는 자료형과 값이 동일할 때 True를 반환하게 됩니다. 예를 들어, 0 == 0.0은 True이지만 0 is 0.0은 False입니다. 값은 동일하지만 자료형이 전자는 int이고 후자는 float 이기 때문입니다.

```python
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
```

```python
# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3
```

None은 공백을 나타내기 위해 자주 쓰임  최소값이 존재하지는 않지만 표식을 항당하여 숫자가

아니라고 나타낼것이기 때문입니다 

smallest라는 변수를 만들어 None를 할당함으로서 구현할 수 있습니다

is 연산자는 == 연산자 보다 강력하다

이 방법은 최대값을 구할 때도 유용하다



is와 is not 연산자는 파이썬에서 매우 유용하다 == 연산자와 같다 이들은 질문을 던진다

공백이 공백인지 참 또는 거짓 값을 반환하는 == 연산자보다 강력하다

비교대상  두 개의 자료형과 값이 같은지 물어봅니다

0 == 0.0을 적으면 참이라고 합니다

하지만 0 is 0.0을 적으면 거짓을 반환합니다 이 둘의 값은 같지만 자료형이 다르기 때문이다

매우 강력한 연산자이니 남용하면 안된다

숫자나 문자열을 사용한다면 == 연산자를 사용하고 is는 사용하지 마세요

is 연산자는 불리언 자료형이나 None 자료형에만 사용한다 그냥  None 또는 True False 값에만 사용



# chapter5 part5

실습 

루프의 종료 메커니즘과 입력값 예외 처리를 통한 유효한 입력인지 알아보기

문제를 발견하면 continue를 이용해서  다음 반복을 실행하도록하는 방법을 사용

루프의 합계 패턴을 이용 누적된 데이터로  출력하고싶은 값을 출력