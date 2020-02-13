# Chapter7 part1

**텍스트 파일은 무엇인가?**

텍스트 파일은 연속적으로 연결되어 있는 줄글들의 집합이라고 생각할 수 있습니다. 우리는 지금까지 많은 텍스트 파일을 만들어 왔습니다.

그럼 텍스트 파일을 열고 처리하는 것과 관련된 몇 가지 함수들을 살펴보도록 하겠습니다.



handle = open(filename, mode)

**open()**

파일을 여는것은 open() 함수를 이용해 달성할 수 있습니다

open 함수가 파일 핸들을 반환하고 여러분이 지정한 변수에 저장합니다

```python
>>>fhand = open('hello.txt', 'r')
>>>print(fhand)

# open('파일명입력', '모드 선택')
# 1. 파일명 입력
# 파일명은 문자열 타입으로 입력하며, 확장자까지 포함시켜 줍니다.
# 2. 모드 선택
# 모드에서는 w 또는 r 두가지를 선택할 수 있습니다. 'w'는 파일을 작성할 때 사용하며, 'r'은 파일을 읽을 때 사용합니다.
```

핸들은 파일에 대한 창구같은 역할을 합니다



**개행 문자**

파이썬에서 행을 바꾸는 문자인 개행 문자는 '\n'입니다. print() 함수를 사용하게 되면 해당 함수에 의해 '\n'가 발생하게 됩니다. 여기서 중요한 것은 '\n'도 하나의 문자라는 점입니다. 아래에 보시는 것처럼 문자열의 길이를 확인하기 위해 len() 함수를 호출해 보면 'Hello World!'와 'Hello\nWorld!'길이가 동일한 것을 확인할 수 있습니다.

```python
>>>stuff = 'Hello\nworld!'
>>>stuff
'Hello\nworld!'
>>>print(stuff)
Hello
world!
>>>stuff = 'X\nY'
>>>print(stuff)
X
Y
>>>len(stuff)
3
```

\n은 하나의 문자이다 백슬래쉬 기호를 이스케이프 문자라고 하며

\n은 줄 바꿈을 의미한다

모든 줄은 개행 문자로 끝난다



# Chapter7 part2

**파일 핸들**

파일 핸들(File Handle)은 순서가 있고 연속적으로 구성된 텍스트 파일을 한줄한줄 읽어 나가게 됩니다. 

```python
fhand = open('mbox.txt')
for cheese in xfile :
    print(cheese)
```

파일을 열고 핸들을 받습니다 핸들의 변수명을 xfile이라고 설정했습니다

이 루프를 각줄에 한번 돌리고 해당 내용을 출력합니다



**파일의 라인 수 세기**

파일의 문장이 몇 줄이 있는지 확인하기 위해서 매우 간단한 방법으로 해결할 수 있습니다. 

```python
fhand = open('Hamlet.txt')
count = 0
for line in fhand :
    count = count + 1
print('Line Count: ', count)
```

파일을 열고 변수 line은 각 줄 당 한번씩 루프를 돌것이고 그때마다 값이 바뀌게 됩니다 한번 루프를 돌때마다 변수값에 1을 더해주어 새로운 줄을 만날때마다 1씩 더하도록 만듭니다



**파일 전체 읽기**

우리는 전체 텍스트 파일을 단일한 하나의 문장으로 읽어 들어 올 수도 있습니다. 물론 각 문장에 대한 구분은 개행문자로 구분되어 있습니다.

```python
>>>fhand = open('mbox-short.txt')
>>>inp = fhand.read()
>>>print(len(inp))
94646으로 출력됩니다.
>>>print(inp[:20])
From stephen.marquar
```

파일을 열고 핸들을 받고 읽기 메서드를 호출  그러면 메소드가 모든 글을 읽고

하나의 큰 문자열로 보내줌



**파일 내용 검색하기**

우리는 기존에 배웠던 문자열과 관련된 내장 함수를 활용해서 특정 문자열로 시작하는 문자를 찾을 수 있습니다.

```python
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)
        
# 결과값으로 From: 으로 시작되는 문자열이 출력되게 됩니다.
```

하지만 결과를 보게 되면 한 줄씩 띄워져 있는 것을 발견할 수 있습니다. 이에 대한 원인은 print()함수로 출력되면서 앞서 말씀드린 것처럼 개행 문자가 계속해서 추가되기 때문입니다. 새로운 라인은 공백으로 인식되기 때문에 해당 부분을 제거 하게 되면 우리는 기본적으로 추가 되어 있던 개행 문자를 삭제 할 수 있습니다. 기억을 떠올려 본다면 문자열의 오른쪽 공백을 제거하는 함수는 rstrip()이었습니다. 

```python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # 오른쪽 공백 제거
    if line.startswith('From:') :
        print(line)
```

루프로 파일 안의 모든 줄을 거친 뒤 line = line.rstrip()을 하면

변수 line은 더 이상 개행문자를 포함하지 않습니다 변수 line안에는 개행문자가 없으므로

print 함수에 의한 줄바꿈이 존재합니다 그래서 단일 간격으로 출력이 됩니다

보통은 이후에 더 하고싶은 일을 작성하고 지금처럼 단순히 출력만 하지는 않고 

뽑아낸 결과로 추가적인 일을  코드가 있을것입니다

그렇게 하는 방법은 본격적으로 전과 같습니다

```python
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip() # 오른쪽 공백 제거
    if not line.startswith('From:') :
        continue
    print(line)
```

from:을 포함하지 않으면  continue문을 이용해 계속 진행

```python
fname = input('Enter the file name')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswich('subject')
        count = count + 1
print('There were', count, 'subject lines in', fname)
```

파일명을 고정하지 않고 유동적으로 바꾸려면 파일명을 입력값으로 받으면 됩니다

이건 if문을 사용한 카운터이며 특별한 패턴만을 세는 카운터입니다

그런데 가끔은 사용자가 잘못된  파일명을 입력할때도 있고 그런 경우도 다뤄야 합니다 그래서

나머지 코드는 그대로 두고 일부만 추가할껍니다

``` python
fname = input('Enter the file name')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', name)
    quit()
    
count = 0
for line in fhand:
    if line.startswich('subject')
        count = count + 1
print('There were', count, 'subject lines in', fname)
```

input으로 들어간 올바른 파일명이 try 부분으로 갑니다 올바른 파일명이므로 except 부분은 넘기고

다음 코드를 진행하여 카운터 수를 출력합니다

잘못된 파일명을 입력하면 except 부분으로 가게되고 파일명을 찾을 수 없게 됩니다

try 코드에서 except 코드로 넘어간 뒤 파일을 열 수 없다고 출력합니다

quit()은 특별한 함수로 실행하게 되면 아무것도 반환하지 않습니다



# Chapter7 part3

실습

이 ly는 문자 변수고 upper이  받은 문자를 대문자로 바꾸어 반환합니다

이건 객체 지향 용어입니다