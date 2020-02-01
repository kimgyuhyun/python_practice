# Chapter8 part1

**프로그래밍**

통상 프로그래밍은 알고리즘과 자료구조로 나눌 수가 있습니다. 알고리즘이 특정 문제를 해결 하기 위한 규칙 또는 단계라면, 자료구조는 컴퓨터내에서 자료를 구조화 하는 특별한 방식이라고 생각 할 수 있습니다

**무엇인 컬랙션이 아닌가?**

컬렉션이 무엇인지 알기 위해 우리는 컬렉션이 아닌 것을 알아야 합니다. 하나의 변수에 새로운 값을 할당하게 되면 기존의 값은 사라지고 그 자리에 대체하게 됩니다. 즉, 하나의 변수에는 하나의 값만 할당하는 것을 우리는 배웠습니다. 하나의 변수에 여러 값을 넣는 것이 가능하도록 하는 것이 컬렉션입니다. 

**리스트 (List)**

리스트는 컬렉션의 한 종류 입니다.

1. 리스트의 각 항목들은 '[]'로 둘러싸게 됩니다.
2. 리스트 내의 항목들에 대한 구분은 ,(콤마)로 구분합니다.
3. 리스트 내에 또 다른 리스트를 내포할 수 있습니다.
4. 비어 있는 리스트를 만들 수 있습니다.
5. 리스트의 항목들에 인덱스 값으로 접근할 수 있습니다.
6. 리스트의 항목들은 바뀔 수 있습니다.

 ```python
>>>print([1, 24, 76])
[1, 24, 76]
>>>print(['red', 'yellow', 'blue'])
['red', 'yellow', 'blue']
>>>print(['red', 24, 98.6])
['red', 24, 98.6]
>>>print([1,[5, 6], 7])
[1, [5, 6], 7]
>>>print([])
[]
 ```

구조 안에 또 다른 구조가 들어가 있는 형태이며 때때로 아주 복잡한 경우도 있다

```python
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
```

[] 안에는 여러가지를 넣을 수 있습니다 파일핸들이나 파일, 문자열 그리고 문자열 안의 문자도

문자열 리스트에 넣을 수 있습니다

for 문과 반복 변수를 이용하여 리스트의 처음부터 끝까지 돌아본 것 입니다

```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
```

여기서 friend는 반복 변수고 friends는 리스트 변수 입니다

```python
>>>friends = ['Joseph', 'Glenn', 'Sally']
>>>print(friends[1])
Glenn
```

문자열과 마찬가지로 리스트 안을 볼 수 있습니다

```python
>>>fruit = 'Banana'
>>>fruit[0] = 'b'
typeError:'str' object does not support item assignment
>>>x = fruit.lower()
>>>print(x)
banana
>>>lotto = [2, 14, 26, 41, 63]
>>>print(lotto)
[2, 14, 26, 41, 63]
>>>lotto[2] = 28
>>>print(lotto)
[2, 14, 28, 41, 63]
```

리스트는 가변형입니다 리스트에 원소가 3개 있을때 가운데 있는 원소를 바꿀 수도 있다는 말입니다

변형이 불가능한 것을 살펴보면  문자열이 변형 불가입니다



**len()**

리스트에서도 해당 리스트가 몇개의 항목을 가지고 있는지를 len()함수를 통해서 확인할 수 있습니다.

```python
>>>great = 'Hello Bob'
>>>print(len(great))
9
>>>x = [1, 2, 'joe', 99]
>>>print(len(x))
4
```

우리는 지금까지 len 함수를  문자열의 길이를 재는 데 사용했습니다

리스트의 경우 len 함수가 리스트 안의 원소의 개수를 세어 줍니다 글자수가 아니라

몇 개의 원소가 있는지를 알려줍니다



**range()**

range() 함수는 인자로 전달되는 값에 따라서 숫자로 이루어진 리스트를 반환하게 됩니다.

```python
>>>pritn(range(4))
[0, 1, 2, 3]
>>>friends  ['Joseph', 'Glenn', 'Sally']
>>>print(len(friends))
3
>>>print(range(len(friends)))
[0, 1, 2]
```

range 함수는 사용자가 원하는 반환 횟수를 매개 변수로 받습니다

```python
friends  ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year', friend)
```

리스트 안에 무엇이 있든 그냥 가는 for 루프입니다 만약 여러분들이 루프를 실행하면서

위치, 루프 위에서부터의 상대적 위치 알 필요가 없다면 상관없습니다 하지만 때때로

루프를 실행하면서 위치를 알고 싶을 때가 있습니다 그럴때는

```python
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year', friend)
```

friend에 range와 len을 사용하여 0, 1, 2를 얻어냅니다



# Chapter8 part2

**연산자 활용**

**리스트 병합**

리스트 타입도 '+' 연산자를 활용해서 서로 다른 리스트를 더할 수 있습니다.

```python
>>>a = [1, 2, 3]
>>>b = [4, 5, 6]
>>>c = a + b
>>>print(c)
[1, 2, 3, 4, 5, 6]
>>>print(a)
[1, 2, 3]
```

리스트 끼리 더하는 경우에는 덧셈이 둘을 연결하여 줍니다

**리스트 슬라이싱**

리스트도 :(콜론)을 이용해 자를 수가 있습니다. 여기서 중요한 것은 예를 들어 t[1:3]과 같은 경우 3번째 인덱스에 해당하는 항목은 포함되지 않는다는 것입니다. 

```python
>>>t = [9, 41, 12, 3, 74, 15]
>>>(t[1:3])
[41,12]
>>>(t[:4])
[9, 41, 12, 3]
>>>(t[3:])
[3, 74, 15]
>>>(t[:])
[9, 41, 12, 3, 74, 15]
```

아무 숫자도 안적으면 리스트 전체를 나타냅니다 문자열에서 다뤘던 것과 거의 동일합니다

**dir() 메소드**

특정 타입에서 사용할 수 있는 메소드의 목록들을 볼 수 있는 함수도 있습니다.

```python
>>>x = list()
>>>type(x)
<type 'list'>
>>>dir(x)
['append', 'count', 'extend', 'index', 'insert',
 'pop', 'remove', 'reverse', 'sort']
```

리스트에 관한 여러가지의 메소드가 존재하고 본 링크에서 리스트에 관한 모든것을 찾아볼 수 있습니다

**리스트 만들기**

빈 리스트 만들기 - 항목 추가하기 - 항목 정렬하기 - in을 활용해 'Glenn'이 친구 목록에 있는지 확인하기

```python
>>>stuff = list()
>>>stuff.append('book')
>>>stuff.append(99)
>>>print(stuff)
['book', 99]
>>>stuff.append('cookie')
>>>print(stuff)
['book', 99, 'cookie']
```

빈 리스트를 만들어 stuff에 할당해서 stuff는 이제 리스트 오브젝트입니다

append 메소드를 사용하여 리스트에 book을 넣어줍니다

리스트에는 보통 같은 종류의 변수가 있는 경우가 많습니다 같은 종류의 값이

리스트 여러 위치에 있습니다만 항상 그럴 필요는 없습니다

```python
>>>some = [1, 9, 21, 10, 16]
>>>9 in some
True
>>>15 in some
False
>>>20 not in some
True
```

in 연산자는 문자열의 startswich나 end함수와 비슷하게 작동합니다

```python
>>>friends = ['Joseph', 'Glenn', 'Sally']
>>>friends.sort()
['Glenn', 'Joseph', 'Sally']
>>>print(friends[1])
Joseph
```

sort 메소드를 사용해  리스트를 정렬합니다

문자열은 변형 불가하고 리스트는 변형 가능합니다 그래서 자체적으로 정렬하라고 할 수 있는것입니다

```python
>>>nums = [3, 41, 12, 9, 74, 15]
>>>print(len(nums))
6
>>>print(max(nums))
74
>>>print(min(nums))
3
>>>print(sum(num))
154
>>>print(sum(nums)/len(nums))
25.6
```

len 함수는 원소 개수를 세어줍니다

max 함수는 리스트 내의 최댓값을 알려줍니다

min 함수는 리스트 내의 최솟값을 알려줍니다

sum 함수는 모든 값의 핪을 알려줍니다

평균을 내고 싶은 경우 sum과 len으로 전체 합을 리스트의 길이로 나누어주면 됩니다

```python
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)
```

inp에 숫자를  계속 받고 done을 입력하면 중단되며 받아왔던 값의 평균을 구해주는 코드

리스트를 배우기전에 사용하던 방식입니다

```python
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average', average)
```

세 줄은 동일합니다 다른점은 실제 계산을 지금 하는것이 아니라 그냥 값을 리스트에 추가한다는 것입니다

이 두가지 방법 모두 같은 결과를 내줍니다 하지만 한가지 다른점이 있는데

숫자가 100만, 10억개처럼 많은 경우 모든 숫자가 메모리속에 저장되어 있어야합니다

첫번째보다 두번째 방법이 메모리를 더 많이 차지합니다



# Chapter8 part3

**문자열과 리스트**

문자열과 리스트는 잘 어울려 사용됩니다.

```python
>>>abc = 'With three words'
>>>stuff = abc.split()
>>>print(stuff)
['With', 'Three', 'words']
>>>print(len(stuff))
3
>>>print(stuff[0])
with
>>>print(stuff)
['With', 'Three', 'words']
>>>for w in stuff :
    print(w)
...
...
With
Three
words
```

split이 하는 역할은 문자열을 살펴보고 공백을 찾고 공백을 기준으로 문자열을 여러 조각으로 나누어

분리된 각 조각으로 구성된 리스트를 반환하는 것입니다

문자열을 보고 stuff에 단어 단위로 분리하여 넣고서는 반복 변수 w를 이용하면

w가 세 단어를 연속으로 받아서 for 문을 돌 것입니다

그러면각 각 줄의 데이터를 단어 단위로 효과적으로 전달할 수 있습니다

 

**구분자**

명시적으로 구분자를 넣어주지 않으면, 빈칸을 구분자로 인지하고 나누게 됩니다.

```python
>>>line = 'A lot               of spaces'
>>>etc = line.split()
>>>print(etc)
['A', 'lot', 'of', 'spaces']
>>>
>>>line = 'first;second;third'
>>>thing = line.split()
>>>print(thing)
['first;second;third']
>>>print(len(thing))
1
>>>thing = line.split(';')
>>>print(thing)
['firs', 'second', 'third']
>>>print(len(thing))
3
```

line에서 저 줄에는 공백이 없기때문에 받은 리스트를 살펴보면 하나의 원소만 있고 세미콜론도 그대로 입니다

공백 대신 세미콜론을 기준으로 나누라고 해주고 나온 결과물을 보면 세미콜론을 기준으로 나뉜

세 단어 리스트가 있고 첫번째, 두번째, 세번째 원소가 있습니다

**이메일 주소 추출하기**

지금까지 배운 메소드와 자료구조를 활용하면 우리가 원하는 값만을 추출할 수가 있습니다.

```python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswich('From ') : continue
    words = line.split()
    print(words[2])
```

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 에서 요일만 출력하는 간단한 루프

때로는 더 깊이 들어가 한 번 분할한 결과물을 다른 구획 문자를 기준으로 또 분할하는 경우도 있습니다

```python
words = line.split()
email = words[1]           stephen.marquard@uct.ac.za
pieces= email.split('@')   ['stephen.marquard', 'uct.ac.za']
print(pieces[1])           'uct.ac.za'

```

예전에 find와 pause를  사용해 했던 일보다 많이 깔끔해졌습니다



# Chapter8 part4

실습

피싱을 하고 자료를 읽는 코드

```python
wds[0] != 'From' or len(wds) < 3 :
```

이렇게 작성하면 트레이스백 에러가 발생합니다

```python
if len(wds) < 3 or wds[0] != 'From' :
```

가디언 패턴이 먼저 오고 그 후 or이 와야 합니다

가디언 패턴이 먼저 오고 확인 결과가 참이라면 뒤 문장은 확인하지 않습니다

이를 최단 평가(short circuit evaluatiom)라고 합니다