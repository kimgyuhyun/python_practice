# Chapter 11 part 1

**정규식 간단한 요약**

정규 표현식의 규칙에 대해 간단히 요약한 내용입니다. 앞으로 이 내용에 대해 예제와 함께 차근차근 설명을 드리도록 하겠습니다.

 

^           라인의 처음을 매칭

$            라인의 끝을 매칭

.             임의의 문자를 매칭 (와일드 카드)

\s          공백 문자를 매칭

\S         공백이 아닌 문자를 매칭

\*            바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.

*?          바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.

\+           바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함

+?          바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.

[aeiou]    명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제

[a-z0-9]    - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.

( )         괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.

re.search 메개 변수를 받아 문자열 내에서 검색하는 함수

re.findall 문자열을 쭉 순회하면서 정해진 패턴을 만족하면 추출하는 함수



**텍스트에서 문자 패턴 찾기**

다음 코드는 mbox-short.txt 파일에서 'From:'이라는 문자 패턴이 포함된 문장을 찾아 출력하는 프로그램입니다. 여기에서는 find() 메소드를 사용했습니다.

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
```

같은 프로그램을 정규표현식을 활용해 작성하면 다음과 같습니다.

정규표현식을 사용하기 위해서는 re(regular expression) 모듈을 import 해야 하고, re.search()가 find() 메소드와 같은 역할을 해주는 부분입니다.

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
```



**텍스트에서 시작 패턴 찾기**

이번에는 'From:'으로 시작하는 문장을 출력하는 프로그램입니다.

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
```

그리고 이것을 정규표현식으로 표현하려면 다음과 같이 '^'라는 특수 문자를 사용하면 됩니다

```python
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)
```

차이는 그냥 일반 함수를 썼느냐 정규 표현을 썼느냐 이다



**특수 문자를 활용한 문자 패턴 찾기**

방금 보신 것처럼 정규 표현식에서는 특수 문자를 사용할 수 있습니다. 그리고 방금 보셨던 '^'(캐럿 문자) 외에도 다음과 같은 다양한 특수 문자들이 있습니다.

^ : 문장의 시작을 의미

. : 어떤 문자 한 글자

\* : 앞의 문자가 여러 번 반복될 수 있음을 의미

\+ : 앞의 문자가 1번 이상 나타남을 의미

\S : 공백 문자가 아닌 한 개의 문자
(\는 역슬래시와 같은 문자임)

따라서, 다음과 같은 문자열들은 모두 '^X.*:'라는 패턴을 통해 찾을 수 있습니다.

- X-Sieve: CMU Sieve 2.3
- X-DSPAM-Result: Innocent
- X-DSPAM-Confidence: 0.8475
- X-Content-Type-Message-Body: text/plain
- 그리고 다음과 같은 문자열들은 '^X-\S+:' 패턴으로 찾을 수 있으며,
  - X-Sieve: CMU Sieve 2.3
  - X-DSPAM-Result: Innocent

다음의 문자열은 'X-'와 ':' 사이에 공백 문자가 아닌 문자가 포함되지 않았기 때문에 '^X-\S+:' 패턴으로 찾을 수 없습니다.

- X-: Very short
- X-Plane is behind schedule: two weeks



# Chapter 11 part 2

**패턴 추출하기**

다음 코드에서 '[0-9]+'은 0부터 9까지 문자가 1번 이상 반복되는 패턴을 의미합니다. 이것은 즉, 정수로 이루어진 데이터를 찾는 것입니다. 또한 findall 메서드는 x라는 문자열에 존재하는 패턴('[0-9+]')을 모두 리스트로 저장해주는 기능을 합니다.
따라서, 이 코드는 x라는 문자열에서 정수 형태의 데이터를 모두 추출하여 y에 저장을 하는 코드입니다.

```python
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

# ['2', '19', '42']
```

다음 코드는 'A','E','I','O','U'로 이루어진 패턴을 찾아 출력하는 코드이지만 x 문자열에 해당되는 패턴이 없어서 빈 리스트를 출력합니다. 여기서 알 수 있는 사실은 정규 표현식에서는 소문자와 대문자를 구분한다는 사실입니다.

```python
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[AEIOU]+',x)
print(y)

# [] (빈 리스트 출력)
```



**탐욕적 방식의 패턴 찾기**

만약 다음 문장에서 '^F.+:'라는 패턴과 일치하는 부분을 찾는다면,

x = 'From: Using the : character'

- From:
- From: Using the :

이라는 두 가지 부분이 모두 패턴과 일치하게 됩니다.

이럴 때는 다음과 같이 가장 긴 패턴을 찾아주는데, 이것을 '탐욕적 방식의 패턴 찾기'라고 부릅니다. 일치하는 여러 패턴이 있을 경우 가장 긴 것을 선택한다는 의미입니다.

```python
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# ['From:']
```

'^F.*: *을 붙이면 F뒤에 아무 문자가 오지 않는 F: 로 시작하는 문장을 찾을 수 있다

^F.+:' +를 붙이면 문자가 하나이상 와야해서 F: 로 시작하는 문장을 찾을 수 없다

**비탐욕적 방식의 패턴 찾기**

물론 탐욕적이지 않은 방식으로 패턴을 찾을 수도 있습니다.

다음 코드에서처럼 패턴 뒤에 '?'(물음표)를 붙여주면 여러 대상 중 가장 짧은 것을 선택하게 됩니다.

```python
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# ['From:']
```

*?는 0 또는 그 이상이면서 탐욕적이지 않은 것

+?는 1 또는 그 이상이면서 탐욕적이지 않은 것

**원하는 부분만 추출하기**

다음 코드를 실행하면 '@' 문자 앞 뒤로 공백이 아닌 문자가 오는 문자열 패턴을 찾아줍니다. 따라서 다음과 같이 이메일 주소의 패턴이 추출됩니다.

```python
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('\S+@\S+',x)
print(y)

# ['stephen.marquard@uct.ac.za’]
```

그리고 다음과 같이 From으로 시작하는 이메일 주소 패턴에서 이메일 주소 부분만 추출할 수도 있습니다. 소괄호를 사용해서 말이죠.

```python
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)

# ['stephen.marquard@uct.ac.za']
```



# Chpater 11 part 3

**이메일 호스트를 추출하는 다양한 방법**

이메일 호스트를 추출하는 다양한 방법에 대해 다시 한 번 살펴보겠습니다.

먼저 문자열 메소드를 사용하는 방법입니다. find 메소드와 리스트 슬라이싱을 활용해 다음과 같이 찾을 수 있었습니다.

```python
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# 21
sppos = data.find(' ',atpos)
print(sppos)
# 31
host = data[atpos+1 : sppos]
print(host)
# uct.ac.za
```



다음은 split 메소드를 활용하는 방법입니다. 공백 문자를 기준으로 1차적으로 문자열을 나누고, '@'이 포함되어있는 문자열을 '@'을 기준으로 나누었습니다.

```python
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# 'uct.ac.za'
```

이번엔 정규식을 사용한 방법입니다. 여기에서 '^ '는 공백문자가 아닌 문자를 의미하며, '^'가 중간에 들어갈 경우 뒤에 오는 문자를 제외한 패턴을 의미합니다.

```python
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)

# ['uct.ac.za']
```

여기에서 조금 더 정교하게 패턴을 추출하려면 다음과 같이 코드를 작성할 수도 있습니다.

```python
import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

# ['uct.ac.za']
```





**종합 예제 : 패턴 추출 및 최댓값 찾기**

지금까지 배운 내용들을 종합하면 텍스트 파일에서 특정 패턴을 찾고, 그 패턴들 중 가장 큰 값이 어떤 것인지 찾을 수 있습니다.

```python
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :  continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
```



**예외 문자(Escape Character)**

지금까지 다양한 특수 문자를 배웠습니다. 그런데 만약 그런 특수 문자로 이루어진 패턴을 찾으려면 어떻게 해야 할까요?

그럴 때는 역슬래시(\)를 사용하면 됩니다. 

예를 들어, '$' 문자가 포함된 패턴을 찾고 싶을 때는 다음과 같이 코드를 작성할 수 있습니다.

```python
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)

# ['$10.00']
```



[^ ]와 \S

같은 의미 입니다. \S는 whitespace 문자가 아닌 것과 매치합니다. 다시말해, 공백이 아니면 뭐든 찾아냅니다. [^ ]는 문자 클래스 [] 안에 있는 ^여서 반대(not)을 뜻합니다. 예를 들어, [^0-9]는 숫자가 아닌 문자를 뜻합니다. 결과론적으로 두 가지는 같은 의미이며, 문자 클래스를 이용해 자주 사용하는 정규 표현식을 \d, \D, \s, \S, \w, \W 등 으로 간단화 한 것이라고 생각하시면 됩니다.