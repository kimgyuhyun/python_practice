

# Chapter6 part1

**1. 문자열 읽기, 타입 변환**

문자열을 사용한 데이터를 읽어 오게 되면 우리는 에러나 사용자 입력에 대해 많은 대처를 할 수 있게 됩니다.

또한, 사용자 입력으로 들어오는 값은 문자열 타입으로 입력되므로 입력된 값으로 다른 무엇인가를 하기를 원한다면 적절한 타입 변환을 해야줘야 합니다.

```python
name = input('Enter: ')
print(type(name))
print(name)

# > Enter: 123 으로 입력합니다.
# 인풋값 123의 타입은 <class 'str'>과 같습니다.
# 123으로 출력됩니다.
```



**2. 문자열의 내부 들여다 보기**

우리는 특정 문자열을 구성하고 있는 개별 문자 값에 인덱스를 활용해서 접근할 수 있습니다. 여기서 유의해야 할 것은 첫번째 오는 문자에 대한 인덱스는 0부터 시작한다는 점입니다. 만약 해당 문자열이 가지고 있는 인덱스를 넘어서는 값을 호출하게 되면 오류가 발생하게 됩니다.

```python
>>>fruit = 'banana'
>>>letter = fruit[1]
>>>print(letter)
a
>>>x = 3
>>>w = fruit(x - 1) <  fruit의 인덱스인 x - 1
>>>print(w)
n
```

인덱스는 연산자입니다 문자열 변수의 마지막에 대괄호를 적는 문법으로 사용할 수 있습니다

문자열의 길이 보다 긴 인덱스로는 색인할 수 없습니다

```python
zot = 'abc'
print(zot[5])

IndexError: string index out of range
```

각 인덱스는 0, 1, 2로 인덱스 5는 찾을 수 없습니다



**3. len 함수**

문자열에 대해서 우리는 len() 내장 함수를 활용해서 문자열의 길이를 알 수 있습니다. 예를 들어, len(banana)라고 한다면 banana가 몇개의 문자로 구성되어 있는지를 알 수 있게 되는 것입니다.

```python
>>>fruit = 'banana'
>>>print(len(fruit))
6
```

문자열 변수를 전달해서 len 함수 안의 매개변수로 전달하면  문자열의 길이를 반환합니다



**4. 문자열의 길이만큼 루프 실행**

우리는 len() 함수을 활용하면 문자열의 길이 만큼 루프를 실행 할 수 있습니다.

```python
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
# 0 b
# 1 a
# 2 n
# 3 a
# 4 n
# 5 a
```

 기본적인 불황적 루프이지만 반복 값을 신중히 설계하여 루프 데이터를 읽는데 성공 했습니다

또 다른 방법은 유한 루프를 사용하는 방법입니다.

일반적으로 while 루프와 for 루프 모두를 사용할 수 있고 그 외 조건이 같을 때 for 루프를 사용하는걸

선호합니다 



```python
fruit = 'banana'
for letter in fruit:
    print(letter)
    
# b
# a
# n
# a
# n
# a

```

letter를 반복 변수로 지정하고 연속적인 값으로 문자열의 각 문자를 가져옵니다

루프를 실행하면서  index에 해당하는 숫자를 실제로 알아야하는 것이 아니라

문자열의 각 숫자를 순서대로 확인하고 싶은 것이라면 그냥 for 루프를 이용하면 된다

```python
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
```

가장 큰 문자를 찾거나 가장 작은 문자를 찾거나 문자가 존재하는지 탐색하거나

banana라는 단어에서 a가  몇 개 있는지 셀 수 있는 코드입니다.



# Chapter6 part2

**문자열 슬라이싱**

지금까지 우리는 문자열에서 단일 문자를 가져 왔습니다. 특정 범위에 있는 문자를 가져올 수도 있습니다.

```python
>>>s = 'Monty python'
>>>print(s[0:4])  
Mont
>>>print(s[6:7])
p
>>>print(s[6:20])
python
```

s[0:4]는  좌표 0에서부터 시작하며 따라 올라가며 읽습니다  하지만 4를 포함하지 않습니다

s[6:7]은 인덱스 6에서 시작해서 인덱스 7까지 이지만 7을 포함하지 않습니다 결과로 p만 나오는 이유 입니다

s[6:20]은 문자열이 20까지 없으니 에러가 뜰거 같지만 파이썬은 친절하게도 끝에서 멈출게 하며 

코드를 실행시켜줘서 python이 결과로 나옵니다

```python
>>>s = 'Monty python'
>>>print(s[:4])  
Mo
>>>print(s[8:])
thon
>>>print(s[:])
Monty python
```

첫 번째 인덱스를 생략하면 문자열의 시작에서 시작한다고 가정합니다

두 번째 인덱스를 생략하면 문자열의 마지막까지라고 가정합니다



**문자열 합치기**

문자열 연결은 수리 연산자인 "+"를 이용해서 달성할 수 있습니다.

```python
>>>a = 'Hello'
>>>b = a + 'There'
>>>print(b)
HelloThere
>>>c = a + ' ' + 'There'
>>>print(c)
Hello There
```

자동적으로 공백이 더해지지 않기 때문에 공백 문자열을 별도로 합쳐야 한다

**in 을 논리 연산자로 사용하기** 

특정 문자열에 우리가 확인하고자 하는 문자가 있는지 확인하기 위해 우리는 in을 사용할 수 있습니다.

```python
>>>fruit = 'banana'
>>>'n' in fruit
True
>>>'m' in fruit
False
>>>'nan' in fruit
True
>>>if 'a' in fruit :
    print('Found it!')
    
Found it!    
```

n이 fruit에 포함됐는지 물어보는것

m이 fruit에 포함됐는지 물어보는것

nan이 fruit에 포함됐는지 물어보는것

a가 fruit에 있다면 들여쓰기 된 부분을 출력하란 뜻



**문자열 라이브러리**

문자열 타입의 객체에서 우리는 다양한 메소드를 사용할 수 있습니다.

```python
>>>great = 'Hello Bob'
>>>zap = great.lower()
>>>print(zap)
hello bob
>>>print(great)
Hello Bob
>>>print('Hi There'.lower())
hi there
```

문자열은 객체입니다 객체는 메소드라고 부르는것을 가지고 있습니다

따라서 문자열 객체는 내장된 능력이 있습니다

.lower()은 문자열의 소문자 버전을 보여달라고 말하는 함수입니다

상수에 대해서도 메소드를 호출할 수 있습니다 상수 역시 객체입니다

메소드는 특별한 형태의 함수 호출입니다 함수에 매개 변수로 전달하는 대신 객체 온점 함수 이름을

적는것으로 일어나는  함수 호출입니다



```python
>>>stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>>dir (stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

클래스는 객체 지향 개념이다 하지만 문자열이므로 dir 함수를 사용할 수 있습니다

여기에 있는 모든것이 x에 대해 실행할 수 있는것입니다

**문자열 탐색**

```python
>>>fruit = 'banana'
>>>pos = fruit.find('na')
>>>print(pos)
2
>>>aa = fruit.find('z')
>>>print(aa)
-1
```

find() 작업은 하위 문자열을 문자열에서 탐색합니다

**대문자 또는 소문자로 바꾸기**

```python
>>>great = 'Hello Bob'
>>>nnn = great.upper()
>>>print(nnn)
HELLO BOB
>>>www = great.lower()
>>>print(www)
hello bob
```

.upper()은 대문자로 바꿔주는 메소드 입니다

.lower()은 소문자로 바꿔주는 메소드 입니다

great는 여전히 대문자와 소문자가 모두 포함된 Hello Bob입니다

왜냐하면 메소드는 기본적으로  기존 문자열을 바꾸지 않고 원본 문자열의  대문자 버전 복사본과

소문자 버전 복사본을  주기 때문입니다



```python
>>>great = 'Hello Bob'
>>>nstr = great.replace('Bob','Jane')
>>>print(nstr)
Hello Jane
>>>nstr = great.replace('o'.'x')
>>>print(nstr)
Hellx BxB
```

바꾸기 전 문자열(Bob)와 바꿀 문자열(Jane)을 전달합니다

문자열에 있는 모든 o를 탐색하고 찾아낸 o를 x로 대체합니다



**Strip 메소드**

문자열에서 공백을 제거할 수 있는 메소드가 존재합니다. 

lstrip(): 왼쪽 공백 제거

rstrip(): 오른쪽 공백 제거

strip(): 오른쪽 왼쪽 공백 제거

```python
>>>greet = '                     Hello Bob       '
>>>greet.lstrip()
'Hello Bob      '
>>>greet.rstrip()
'      Hello Bob' 
>>>greet.strip()
'Hello Bob'
```

공백은 출력이 일어나지 않도록 하는 모든 종류의 문자를 일컫습니다 의미가 있기만 하다면요



**시작문자열 찾기**

startswith 라는 메소드를 통해서 우리는 특정 문자로 문자열이 시작되는지도 확인할 수 있습니다. 결과값은 불리언 타입으로 반환됩니다. 즉, 해당 문자로 시작한다면 True, 그렇지 않다면 False가 반환됩니다.

```python
>>>line = 'Please have a nice day'
>>>print(line.startswith('Please')
True
>>>print(line.startswith('p')
False
```

line은 문자열 Please로 시작하나요?

True

line이 소문자 p로 시작하나요?

False

이 메소드를 if구문의 조건문으로 활용할 수도 있습니다.



```python
>>>data = 'From stephen.marquard@uct.ac.za sat jan  5 09:14:16 2008'
>>>atpos = data.find('@')
>>>print(atpos)
21
>>>sppos = data.find(' ',atpos)
>>>print(sppos)
31
>>>host = data[atpos+1 : sppos]
>>>print(host)
uct.ac.za
```

data.find('@')은 @ 기호의 위치를 반환합니다

data.find(' ', atpos)는@ 기호의 위치에서 시작해서 공백을 찾습니다



# Chapter6 part3

실습

이 다섯줄이 이 문자열을 잘라내는 특정한 임무를 하는 코드입니다.

```python
str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece)
print(value)
```

0.8475