# Chapter10 part1

**리스트(List)와 비슷한 컬렉션, 튜플(Tuple)**

튜플은 리스트와 굉장히 비슷합니다.

다음 코드를 보시면 리스트와의 차이는 단지 대괄호 대신 소괄호를 사용했다는 정도라는 것을 알 수 있습니다.
리스트와 같이 순서가 있어서 인덱스로 접근이 가능하고, 최대값도 찾을 수 있습니다.

```python
>>>x = ('Glenn', 'Sally', 'Joseph')
>>>print(x[2])
Joseph
>>>y = ( 2, 9, 2 )
>>>print(y)
(1, 9, 2)
>>>print(max(y))
9
>>>for iter in y:
    print(iter)
    
1
9
2
```

튜플을 for ~ in 뒤에 쓰면 튜플을 순회합니다 튜플은 순서를 보존하기 때문에

이렇게 1, 9, 2 순서가 나오게 되죠

**변경 불가능한 속성 (immutable)** 

하지만 리스트와 큰 차이가 있는데, 그것은 변경불가능(immutable), 즉 값을 변경할 수 없다는 특성입니다.

예를 들면, 리스트에서는 다음과 같이 원소의 값을 변경할 수 있습니다.

```python
>>>x = [9, 8, 7]
>>>x[2] = 6
>>>print(x)
>>>[9, 8, 6]
```

리스트는 바꿀 수 있습니다

```python
x = (9, 8, 7)
x[2] = 6
print(x)

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-4-6136e7d6cb90> in <module>()
#       1 x = (9, 8, 7)
# ----> 2 x[2] = 6
#       3 print(x)
# 
# TypeError: 'tuple' object does not support item assignment
```

튜플을 수정할 수 없는 이유는 효율성 때문입니다

값을 저장하고 접근만 할 거라면 리스트보다 튜플을 쓰는게 낫습니다

또 튜플을 사용하기 좋을때는 임시로 사용하는 변수를 만들 때입니다

물론, 이런 특성으로 인해 리스트에서 할 수 있는 일을 하지 못하는 경우도 있습니다.

다음 코드를 보시면, 한 번 생성된 튜플은 정렬하거나, 값을 추가하거나, 순서를 바꿀 수 없습니다.

```python
x = (3, 2, 1)
x.sort()
# Traceback:
# AttributeError: 'tuple' object has no attribute 'sort'
x.append(5)
# Traceback:
# AttributeError: 'tuple' object has no attribute 'append'
x.reverse()
# Traceback:
# AttributeError: 'tuple' object has no attribute 'reverse'
```

이외에도 리스트에서 할 수 있는 것 중 값을 변경하는 것들은 튜플에서 할 수 없습니다.

구체적으로 리스트에 내장된 함수와 튜플에 내장된 함수를 비교하면 다음과 같습니다.

```python
 l = list()
 dir(l)
# ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

 t = tuple()
 dir(t)
# ['count', 'index']
```

즉, 값을 변경하지 않아도 되는 count, index와 같은 함수만 작동하는 것입니다.



**튜플의 장점**

**임시 변수로 활용**

이런 변경이 되지는 않는 속성으로 인해 튜플은 파이썬에서 더 효율적으로 동작됩니다.

하지만 이런 특성은 입문하는 사람에들에겐 큰 장점이 아닐 수 있습니다. 그러면 튜플은 언제 사용하면 좋을까요?

튜플을 다음과 같이 좌변에 사용하면 간단하게 여러 변수에 값을 넣을 수 있습니다.

단, 이럴 경우 좌변과 우변의 갯수는 일치해야합니다.

```python
>>>(x, y) = (4, 'fred')
>>>(print(y)
fred
>>>(a,b) = (99, 98)
>>>print(a)
99
```

튜플을 좌변에 놓을 수 있고 함수가 튜플을 리턴할 수도 있습니다

```python
def t() :
    return (10, 20)
x, y = t()
print(x, y)

# 10 20
```

이와 같은 특성을 잘 활용하면 함수에서 여러 개의 값을 한꺼번에 반환할 수도 있습니다

**딕셔너리를 처리하는데 활용**

지난 시간에 잠시 보셨던 것처럼 딕셔너리의 items 메소드는 딕셔너리에 저장된 각 키와 값의 한 쌍을 튜플로 이루어진 리스트 형태로 만들어줍니다.

따라서 다음과 같이 사용할 수도 있습니다.

```python
>>>d = dict()
>>>d['csev'] = 2
>>>d['cwen'] = 4
>>>for (k,v) in d.items(): 
    print(k, v)
    
csev 2
cwen 4
>>>tups = d.items()
>>>print(tups)
dict_items([('csev': 2), ('cwen': 4)])
```

k, v는 여기서 연속적으로 키와 값을 받으며 루프를 돌게 됩니다

근데 만약 딕셔너리에 뭐가 있는지 궁금하다면 딕셔너리에 내장된

items() 메소드를 사용하면 됩니다

**여러 값에 대해 비교 가능**

튜플의 또다른 장점은 여러 값에 대해 비교가 가능하다는 점입니다.

비교의 방법은 각 튜플의 가장 왼쪽 값끼리 비교한 후 둘의 값이 다를 경우에는 나머지 값들을 비교하지 않고 큰지 작은지 여부를 판단합니다.

만약 가장 왼쪽 값이 동일할 경우에는 그 다음 값을 비교하고, 그 값도 같으면 또 다음 값을 비교하는 형태로 비교가 진행됩니다.

```python
>>>(0, 1, 2) < (5, 1, 2)
True
 >>>(0, 1, 2000000) < (0, 3, 4)
True
>>> ( 'Jones', 'Sally' ) < ('Jones', 'Sam')
True
 >>>( 'Jones', 'Sally') > ('Adams', 'Sam')
True
```

왼쪽에서 오른쪽으로 가장 왼쪽 튜플이나 0번 튜플이 가장 중요하게 작용하는데

사실 다른건 그냥 비교 자체를 하지 않습니다



# Chapter10 part2

**튜플의 특성을 활용해 딕셔너리 정렬하기**

 튜플의 특성을 배웠습니다

```python
(0, 1, 2) < (5, 1, 2)
# True
(0, 1, 2000000) < (0, 3, 4)
# True
( 'Jones', 'Sally' ) < ('Jones', 'Sam')
# True
( 'Jones', 'Sally') > ('Adams', 'Sam')
# True
```

.튜플끼리 비교가 가능하며, 이때 가장 왼쪽에 있는 값끼리 비교한다는 것이었습니다.

```python
tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])
```

그리고 딕셔너리의 items 메소드를 실행하면 키와 값이 쌍을 이루는 튜플로 이루어진 리스트 형태로 반환된다는 것도 배웠습니다



**키를 기준으로 정렬하기**

위의 두 가지 특성을 활용하면 키를 기준으로 딕셔너리를 정렬할 수 있습니다. 방법은 다음과 같습니다.

1. 딕셔너리에서 items 메소드를 실행해 튜플로 이루어진 리스트 형태로 만든다.
2. 이 리스트를 sorted 함수로 정렬한다. 그러면 각각의 튜플의 왼쪽 값, 즉 키를 기준으로 정렬이 된다.

즉, 다음과 같은 코드로 딕셔너리를 키를 기준으로 정렬할 수 있습니다.

```python
>>>d = {'b':1, 'a':10, 'c':22}
>>>d.items()
dict_items([('b', 1), ('a', 10), ('c', 22)])
>>>sorted(d.items())
[('a', 10), ('b', 1), ('c', 22)]
```

items를 써보면 매핑된 대로 나오는데 순서가 뒤죽박죽입니다 여기서

sorted 함수를 써줍니다 시퀀스를 받아서 정렬한뒤에 리턴해줍니다

뒤의 값은 고려하지 않고 앞의 키의 값들을 오름차순으로 정렬해줍니다

여기에서 정렬된 키와 값을 한 줄씩 보기 좋게 출력하려면 이렇게 코드를 작성하면 됩니다. 여기에서 k, v는 소괄호가 없지만 컴마로 나열되어있기 때문에 튜플입니다.

```python
for k, v in sorted(d.items()):
    print(k, v)
# a 10
# b 1
# c 22
```

여기에서 k, v는 소괄호가 없지만 컴마로 나열되어있기 때문에 튜플입니다.



**값을 기준으로 정렬하기**

여기에서 값을 기준으로 정렬하려면 조금의 아이디어만 있으면 됩니다. 방법은 다음과 같습니다.

1. 딕셔너리에서 items 메소드를 실행한다.
2. 튜플을 활용해 키와 값을 분리한다.
3. 키와 값의 위치를 바꾼 리스트를 생성한다.
4. 생성된 리스트를 정렬한다.

이 과정을 코드로 표현하면 다음과 같습니다. 실행결과를 보시면 값을 기준으로 오름차순 정렬이 된 것을 볼 수 있습니다.

```python
>>>c = {'a':10, 'b':1, 'c':22}
>>>tmp = list()
>>>for k, v in c.items() :
    tmp.append( (v, k) )

>>>print(tmp)
[(10, 'a'), (1, 'b'), (22, 'c')]
>>>tmp = sorted(tmp, reverse=True)
>>>print(tmp)
[(22, 'c'), (10, 'a'), (1, 'b')]
```

(v, k)로 리스트를 만들어서 값이 앞에, 키가 뒤에 가도록 만들어줍니다

 reverse=True를 추가해주면 내림차 순으로 나옵니다



**가장 많이 등장한 단어 Top 10 출력하기**

이제 지난 시간에 배웠던 빈도수를 출력하는 프로그램을 다시 살펴보겠습니다

```python
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1
```

파일을 열고  딕셔너리를 만들고 for 루프로 파일을 한 줄씩 읽어옵니다

그리고 split을 통해 띄어쓰기를 기준으로 나눕니다

그리고 다시 for 루프가 있는데 이 루프는 split된 단어들에 대해 돕니다

한 줄씩 루프를 돌고 또 그 한줄에서 한 단어씩 루프를 도는겁니다

그리고 단어를 세서 counts.get(word, 0 )에 1을 더해 저장합니다

코드의 이 시점에서는 단어별로 개수만 세고 있습니다 정렬되지는 않았습니다

```python
lst = []
for key, val in counts.items():
    newtup = (val, key) 
    lst.append(newtup)

lst = sorted(lst, reverse=True)
```

값과 키의 순서를 바꾸어 튜플을 만들어줍니다 그 다음 튜플을 리스트에 넣어줍니다

그 결과 튜플로 된 리스트가 만들어집니다

lst = sorted(lst, reverse=True) 를 사용해  리스트를 내림차순으로 정렬하고 리스트에  다시 돌려줍니다

```python
for val, key in lst[:10] :
    print(key, val)
```

범위를 지정해서 앞에서부터 10개만 출력합니다

값과 키를 뽑아서 일련의 과정을 반복하는데

출력할 때는 또 뒤집어줍니다 뒤집고 뒤집어서 키와 값의 형태로 출력해줍니다

```python
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key) 
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)
```

전체 코드입니다

**리스트 컴프리헨션 (List comprehension)**

마지막으로 리스트 컴프리헨션(List comprehension)이라는 것을 살펴보겠습니다.

이것은 조금 전에 작성했던 딕셔너리를 키를 기준으로 정렬해서 출력하는 코드입니다.

```python
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )

tmp = sorted(tmp)
print(tmp)

# [(1, 'b'), (10, 'a'), (22, 'c')]
```

그리고 다음의 코드는 정확히 위의 코드와 동일한 역할을 합니다

```python
>>>c = {'a':10, 'b':1, 'c':22}
>>>print( sorted( [ (v,k) for k,v in c.items() ] ) )
[(1, 'b'), (10, 'a'), (22, 'c')]
```

리스트가 두 개짜리 튜플로 돼 있습니다 그러니 c.items()에 있는 모든 k,v에 대해 for 루프처럼

반복하게 되고 이걸 도장처럼 리스트에 찍어냅니다 이걸 반복해서 리스트를 만들고 정렬합니다	



튜플, 리스트, 딕셔너리는 관계가 깊습니다 파이썬의 가장 기초가 되는 컬렉션입니다



# Chapter10 part3

실습

튜플을 이용한 딕셔너리 정렬

튜플을 왜 사용한건지 궁금하실겁니다 그냥 리스트를 써도 되거든요

그렇지만 튜플이 리스트보다 더 효율적이기 때문입니다

어차피 값을 수정하지 않을 거니까요

그냥 튜플들의 리스트인 tmp 리스트만 수정했고

리스트 안의 튜플은 수정하지 않았습니다

그래서 보다 효율적인 튜플을 사용하는 겁니다

그렇기 때문에 튜플 순서를 바꿔주는것도 따로 만들었습니다