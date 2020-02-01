# Chapter9 part1

**컬렉션(Collection)**

리스트나 딕셔너리 같은 변수를 가지는 상황이며 하나의 정보보다는 여러 개의 정보를 저장할 때 사용됩니다.

 

**리스트(List)**

리스트는 순서대로 정리된 컬렉션입니다. 데이터를 추가하면 항상 리스트의 끝에 추가되고 0부터 n-1번 위치까지 순서대로 n개의 원소가 저장되어있습니다.

**딕셔너리(Dictionary)**

리스트와 달리 딕셔너리에는 순서라는 것이 없습니다.

대신 키(Key)라는 것이 존재합니다. 마치 물건에 포스트잇으로 라벨을 붙이는 것과 비슷합니다.

딕셔너리는 다음과 같이 dict()라는 생성자를 통해 생성할 수 있습니다.

그리고 다음과 같이 생성할 수 있습니다

```python
>>>purse = dict()
>>>purse['money'] = 12
>>>purse['candy'] = 3
>>>purse['tissues'] = 75
>>>print(purse)
{'money': 12, 'tissues': 75, 'candy': 3}
>>>print(purse['candy'])
3
>>>purse['candy'] = purse['candy'] + 2
>>>print(purse)
{'money': 12, 'tissues': 75, 'candy': 5}
```

리스트와 딕셔너리의 차이점을 보면 둘 다 새로운 원소를 추가할 수 있습니다

둘 다 원소삭제가 가능합니다 차이는 인덱싱 메커니즘에서 발생합니다

우리가 어떻게 대상을 보는지  어떻게 저장하는지에 관한 것입니다

```python
>>>lst = list ()					>>>ddd = dict()
>>>lst.append(21)					>>>ddd['age'] = 21
>>>lst.append(18)					>>>ddd['course'] = 182
>>>print(lst)                       >>>print(ddd)
[21, 183]							{'course': 182, 'age': 21}
>>>lst[0] = 23						>>>ddd['age'] = 23
>>>print(lst)						>>>print(ddd)
[23, 183]							{'course': 182, 'age' : 23}
```

값은 같은데 키가 다릅니다

리스트에서 키는 항상 위치이며 여러분이 지정하지 않습니다 여러분이 넣은 순서대로

내부에서 자동으로 할당합니다

딕셔너리에서 키는 문자열이며 이외에 다른 타입으로도 만들 수 있습니다

```python
>>>jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
>>>print(jjj)
{'jan': 100, 'chuck': 1, 'fred': 42}
>>>ooo = { }
>>>print(ooo)
{}
```

딕셔너리 표현법에서 좋은 점은 print 구문과 정확히 같은 문법을 사용한다는 것

빈 중괄호를 쓰는 방법이 빈 딕셔너리를 생성하는 지름길



**연관 배열 (Associative Arrays)**

이렇게 키와 값이 연결되는 개념을 보통 연관 배열라고 합니다. 접근하는 방식이 리스트와 비슷하지만 키를 갖고 접근한다는 차이점이 있습니다.

여기에서 연관이 의미하는 것은 키와 값 사이의 연결 관계입니다.

리스트에는 위치와 값 사이에 연결 관계가 있었습니다. 그러나 위치와의 연결 관계는 비교적 덜 강력하고 덜 유연합니다.

그래서 대부분의 현대 프로그래밍 언어에는 연관 배열라는 개념이 있습니다.

 

**연관 배열의 다양한 이름**

- property maps : Perl / PHP

- hash maps : Java

- property bags : C# /  .Net


# Chapter9 part2

**사람의 방식으로 이름 빈도수 세기**

사람이 여러 개의 이름을 보고 그 빈도수를 세는 방식은 보통 다음과 같습니다.

1) 새로운 이름을 보면 목록에 추가한다.
2) 추가된 이름이 1번 나왔다는 표시를 한다.
3) 목록에 있는 이름이면 기존의 숫자에 1을 더해준다.
4) 모든 이름을 살펴본 후 표시의 갯수를 세어 가장 높은 것을 찾는다.

이 과정을 파이썬 코드로 다음과 같이 표현할 수 있습니다.

```python
>>>ccc = dict()
>>>ccc['csev'] = 1
>>>ccc['cwen'] = 1
>>>print(ccc)
{'csev': 1, 'cwen': 1}
>>>ccc['cwen'] = ccc['cwen'] + 1
>>>print(ccc)
{'csev': 1, 'cwen': 2}
```

새로운 이름을 보았을때 딕셔너리를 확장하고 이미 봤었던 기존에 이름은 값을 추가할 수 있습니다

**딕셔너리를 이용해 이름 빈도수 세기**

그런데 만약 수백만 개의 이름이 있다면 이런 방식으로 세는 것이 매우 어려워집니다.
이때 딕셔너리를 사용하면 쉽게 해결할 수 있는데, 기본 아이디어는 다음과 같습니다.

1) 이미 저장되어 있는 이름인지 확인한다.
2-1) 만약 이미 저장되어 있는 이름일 경우 : 1을 더한다.
2-2) 만약 저장되지 않은 이름일 경우 : 이름을 저장하고 1을 배정한다.
3) 최종 결과 중 가장 빈도가 많은 이름을 찾는다.

여기서 가장 중요한 부분은 이미 저장되어 있는 이름인지 확인하는 부분입니다.

만약 다음과 같이 딕셔너리에 없는 키를 찾으려고하면 오류가 발생하게 됩니다.

딕셔너리도 할 수 있는일과 할 수 없는 일에 대한 규칙이 있습니다

딕셔너리에 없는 키는 찾을 수 없다는 것입니다

```python
>>>ccc = dict()
>>>print(ccc['csev'])
Tracback error
```

트레이스백 에러가 뜨게 되는데 이 문제는  in 연산자로 쉽게 해결할 수 있습니다

**in 연산자**

이런 문제를 for, list, 문자열에서 사용했던 in 연산자를 사용해 해결할 수 있습니다.

이와 같이 ccc라는 딕셔너리 안에 'csev'라는 값이 있는지 확인하기 위해 in 연산자를 사용하면 참(True) 또는 거짓(False)이라고 우리에게 알려줍니다.

```python
>>>'csev' in ccc
False
```

in 연산자를 사용함으로써 트레이스백 에러를 피했습니다

여기서 만약 없다면 1을 추가하고 있다면 1을 더하라고 할 수 있습니다

그런 일을 수행하는 코드가 바로 이것입니다

```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name in counts: 
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

{'csev':2,'zqin':1,'cwen':2}
```

if 문에서 만약 우리가 보는 이름이 키 형태로 딕셔너리에 보이지 않으면 값을 1로 하여 딕셔너리에    추가합니다

else 문에서 만약 이미 존재한다면 해당 키의 값을 받아와서 1을 더하고 다시 집어넣습니다

```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
       counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# {'csev': 2, 'zqian': 1, 'cwen': 2}
```

그리고 이렇게 not 연산자를 사용해서 동일하게 해결할 수도 있습니다.

**get 메소드**

이와 같이 딕셔너리에 존재하는 키인지 아닌지 여부에 따라 처리하는 패턴은 get이라는 메소드를 사용해서 간결하게 해결할 수 있습니다.

여기에서 counts.get(name, 0)의 의미는 counts 딕셔너리에 name이라는 키가 존재할 경우 name에 대한 값을 불러오고,

그렇지 않을 경우에는 counts 딕셔너리에 name이라는 키에 0이라는 값을 갖는 데이터를 추가하라는 의미입니다.

```python
if name in counts:
    x = counts[name]
else :
    x = 0  
{'csev':2,'zqian':1'cwen':2}
```

```python
x = counts.get(name, 0)
{'csev':2,'zqian':1'cwen':2}
```

저 네 줄이 이 한 줄과 같다고 생각하면 됩니다

왜나하면 이미 있는 대상이면 x는 그 값이 될 것이고 아니라면 0이 되기 때문입니다

```python
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
```

get 메소드를 이용하여 값을 가져오고 1을 더해서 다시 집어넣습니다

이미 값이 1인 경우 1을 더해서 2가 됩니다

새로 0이 배정된 경우 1을 더해 1이 됩니다



# Chapter9 part3

이런 종류의 문제는 사람이 하기에 매우 어려운 문제이지만, 지난 시간에 배웠던 것과 같은 패턴의 문제이기 때문에 딕셔너리를 사용해 쉽게 해결할 수 있습니다.

단지, 리스트에 저장된 데이터가 아니라 긴 문장 형태의 데이터라는 점이 다를 뿐이죠.

그러면 먼저 문장을 어떻게 단어로 바꿀 수 있는지 알아보겠습니다.



**split 메소드**

문자열에 split 메소드를 실행시키면 다음과 같이 띄어쓰기를 기준으로 문장을 분할해 단어들의 리스트로 만들어줍니다.
(참고로, 별도의 옵션을 사용하면 공백 문자(스페이스바)가 아닌 다른 문자를 기준으로도 분할할 수 있습니다)

``` python
counts = dict()
line = input('Enter a line of text:')
words = line.split()

print('wdrds:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)
```

 문장을 한줄 받아서 수를 세는 패턴의 코드입니다

나중에는 문장 대신 파일을 받을겁니다

이 코드를 실행하게 되면

```python
Enter a line of text:
the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car
wdrds: ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']
Counting...
Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}
```

counts가 딕셔너리로 만들어진 히스토그램이 나오게 됩니다

한 줄의 텍스를 받았을 때 단어 단위로 나누고 어떻게 문장의 단어별로

히스토그램을 얻어내는지에 대한 코드였습니다



**딕셔너리에 루프를 적용하는 방법**

지금부터는 딕셔너리에 루프(반복문)를 적용하는 방법에 대해 알아보겠습니다.

지금까지는 딕셔너리를 만드는데만 루프를 사용했지만, 딕셔너리에 저장된 데이터를 다룰 때도 루프가 유용하게 사용됩니다.

먼저 counts라는 딕셔너리를 for 반복문에 넣고 다음과 같이 실행하면, 딕셔너리의 키와 값이 각각 출력됩니다.

```python
>>>counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
>>>for key in counts:
    print(key, counts[key])
    
jan 100
chuck 1
fred 42
```

in연산자를 사용하고 끝자리에 딕셔너리를 넣었는데 for 문의 마지막 자리에는 여러가지를

넣을 수 있고 넣은 대상의 키를 받을 수 있습니다



**items 메소드**

keys, values 메소드로는 딕셔너리의 키와 값의 쌍을 얻을 수 없었는데요, 키와 값의 쌍을 얻기 위해서는 items 메소드를 사용하면 됩니다.
다음과 같이 딕셔너리에 items 메소드를 실행하면 '튜플(tuple)'이라는 자료 구조 안에 키와 값이 쌍을 이루어 저장된 리스트가 반환됩니다.
(튜플에 대해서는 다음 단원에 배우겠습니다)

```python
>>>jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
>>>print(list(jjj))
['jan', 'chuck', 'fred']
>>>print(jjj.keys())
['jan', 'chuck', 'fred']
>>>print(jjj.values())
[100, 1, 42]
>>>print(jjj.items())
[('jan', 100), ('chuck', 1), ('fred', 42)]
```

키를 얻는 방법에는 여러가지가 있습니다

print(list(jjj))  명령어로 기존의 딕셔너리를 리스트로 반환하여 키로 구성된 리스트를 얻습니다

기존의 딕셔너리와 동일한 구성을 가지며 키로만 구성되어 있습니다

print(jjj.keys())  명령어로 keys 메소드를 이용해 키로 구성된 리스트를 제게 주는 똑같은 일을 합니다

print(jjj.values()) 그리고 values 메소드로 딕셔너리에서 값만 달라고 할 수도 있습니다

print(jjj.items()) 이 코드는 items 메소드를 이용하여  원소를 직접 물어보는겁니다 딕셔너리의 원소를 달라고 하면 리스트를 주는데 이는 우리가 다루는 첫 번째 복합적인 자료 구조 형태입니다

리스트 안에 세 개의 원소가 있고  각 원소는 두개의 원소로 구성된 튜플로 되어 있습니다

```python
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for aaa, bbb in jjj.items() :
    print(aaa, bbb)
    
jan 100
chuck 1
fred 42
```

items 메소드를 쓰면 키와 값의 쌍으로  된 리스트를 반환하는데 키만 주는것도 아니고

값만 주는것도 아니고 키와 값 쌍으로 리스트를 주기 때문에 아주 멋진 루프를 만들 수 있게 해줍니다

items 메소드가 준 리스트의 모든 원소들은 키와 값 쌍으로 되어있으므로 2개의 반복 변수를 사용한다



**파일에 저장된 데이터 읽어와서 빈도 분석하기**

지난 시간에 배웠던 파일에서 데이터를 읽어오는 방법을 기억하실 겁니다.

그리고 파일에서 읽어온 데이터를 이와 같이 한 문장씩 읽어온 후 위에서 배운 코드와 연결시키면 텍스트 파일에 있는 모든 단어에 대한 빈도가 계산될 것입니다.
(만약 이 코드가 이해되지 않는다면 한 줄씩 천천히 곱씹으며 완벽히 이해하시기 바랍니다.)

```python
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
```

사용자에게 파일명을 물어보고

파일을 열고

빈 딕셔너리를 생성합니다

그리고서 반복 변수로 문장을 차례로 받은다음 한 줄, 한 줄 처리하고

해당 문장을 단어 단위로 나눕니다

그리고 반복 변수 word를 사용하여 각 줄의 단어들을 돌며 히스토그램을 만듭니다

```python
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
```

items 메소드를 써 키와 값을 반복 변수 두개를 써  키와 값 쌍을 순서대로 받습니다

그리고 bigcount가  현재 가장 큰 값인지를 확인합니다 값이 none라면 아직 아무것도 못 봤거나

방금 읽은 count 값이 지금까지에 bigcount 값보다 큰 경우입니다

최댓값을 찾는 루프인데 추가적으로 가장 큰 값이 몇인지 기록하고 그 값에 해당되는 단어는

무엇인지 기록하는 기능이 들어가 있습니다



딕셔너리는 지금까지 본 컬렉션 중 가장 강력합니다

컬렉션이 무엇인지 이해하기 위해 리스트와 딕셔너리를  보는것이 좋습니다

하나 이상의 대상을 자기 내부에 포함하여 다룰 수 있게 하는 파이썬의 도구입니다



# Chapter9 part4

실습

딕셔너리를 활용한 데이터 빈도수 측정

