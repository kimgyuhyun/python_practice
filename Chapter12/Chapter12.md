# Chapter 12 part 1

**전송 제어 프로토콜 (TCP)**

- IP(인터넷 프로토콜) 위에서 구성

- IP는 데이터를 잃어버릴 수 있음 -

  데이터를 저장하고 있다가 손실이

  일어난 것으로 추정되면 재전송



- 전송 윈도우를 통해 흐름 제어를 조절



- 믿을만한 pipe 역할을 제공



**TCP 연결 / 소켓**

"컴퓨터 네트워킹에서 인터넷 소켓, 또는 네트워크 소 켓은 인터넷 프로토콜을 기반으로 한

인터넷 등의 컴퓨터 네트워킹에서 양방향 커뮤니케이션의 끝점입니다"



프로세스          ←                     인터넷                      → 프로세스



**TCP 포트 번호**

- 포트는 애플리케이션에 대응되거나 프로세스에 대응되는

  소프트웨어 커뮤니케이션의 말단

- 한 서버에 여러 네트워크 에플리케이션이 존재할 수 있게 해줌

- 잘 알려진 포트 번호는

  | Port number | Assignment                                                   |
  | ----------- | ------------------------------------------------------------ |
  | 20          | [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol) (FTP) Data Transfer |
  | 21          | [File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol) (FTP) Command Control |
  | 22          | [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) Secure Login |
  | 23          | [Telnet](https://en.wikipedia.org/wiki/Telnet) remote login service, unencrypted text messages |
  | 25          | [Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) (SMTP) E-mail routing |
  | 53          | [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) (DNS) service |
  | 67, 68      | [Dynamic Host Configuration Protocol](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) (DHCP) |
  | 80          | [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (HTTP) used in the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) |
  | 110         | [Post Office Protocol](https://en.wikipedia.org/wiki/Post_Office_Protocol) (POP3) |
  | 119         | [Network News Transfer Protocol](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol) (NNTP) |
  | 123         | [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) |
  | 143         | [Internet Message Access Protocol](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol) (IMAP) Management of digital mail |
  | 161         | [Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) (SNMP) |
  | 194         | [Internet Relay Chat](https://en.wikipedia.org/wiki/Internet_Relay_Chat) (IRC) |
  | 443         | [HTTP Secure](https://en.wikipedia.org/wiki/HTTP_Secure) (HTTPS) HTTP over TLS/SSL |

**공통 TCP 포트**

- Telnet (23) - Login

- SSH (22) - Secure Login

- HTTP (80)

- HTTPS (443) - Secure

- SmTP (25) (Mail)

- IMAP (143/220/993) - Mail

  Retrieval

- POP (109/110) - Mail

- Retrieval

- DNS (53) - Domain Name

- FTP (21) - File Transfer



URL에 포트 번호가 있는 경우가 있는데, 이는 웹서버가 '관레적으로 정해진' 포트에서

돌지 않는 경우



**파이썬에서 소켓**

파이썬에서는 다음과 같은 방법으로 소켓을 굉장히 쉽게 만들 수 있다

파이썬은 내부적으로 TCP 소켓을 지원한다

```python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
```

먼저 socket 모듈을 import하고,

인터넷에 연결되는 소켓을 연속된 문자의 흐름인 스트림 방식으로 만들어줍니다.

그리고 그 소켓에 data.pr4e.org라는 호스트에 80이라는 포트로 연결을 했습니다.

이렇게 간단한 코드 3줄로 말이죠



# Chapter 12 part 2

**애플리케이션 프로토콜**

- TCP(와 파이썬)는 믿을만한 소켓을
  제공. 소켓으로 어떤 일을 할 수 있고
  어떤 문제를 해결?

-  애플리케이션 프로토콜

  메일

  월드 와이드 웹(WWW)


**HTTP - 하이퍼텍스트 전송 프로토콜**

- 인터넷, 애플리케이션 레이어에서 가장 많이 사용되는 프로토콜

-  웹을 위해 개발 - HTML, 이미지, 문서 등을 가져옴

-  문서 외에 다양한 데이터에도 확장하여 사용 가능

  RSS, 웹 서비스 등

  기본 컨셉: 연결 - 문서 요청 - 문서 수신 - 연결 종료



**HTTP**

HyperText Transfer Protocol을 줄인 말이며, 브라우저가 서버로부터 인터넷을 통해 웹 문서를
받는 경우의 규칙을 정한 것



**프로토콜이란?**

- 규칙의 모음. 모두가 따르므로 서로가 서로의
  행동을 예측 가능

- 서로 충돌하지 않아야 함 

  미국의 이차선 도로에서는 오른쪽 도로로 달려야 함

  영국의 이차선 도로에서는 왼쪽 도로로 달려야 함



http://www.dr-chuck.com/page1.htm

http://     www.dr-chuck.com / page1.htm

프로토콜           호스트                     문서



**서버로부터 데이터 받기**

- 사용자가 ‘href=값’을 가지고 있는 앵커 태그를 클릭해 새로운
  페이지로 이동할 때마다 브라우저는 웹 서버와 연결을 만들고 GET
  요청을 실행해 페이지 URL에 나타난 값을 수신
- 서버는 문서를 포맷팅하고 유저에게 보여주는 HTML 문서를 리턴



**인터넷 표준**

- 모든 인터넷 프로토콜 기준은 한
  기관에 의해 개발
-  Internet Engineering Task Force
  (IETF)
-  www.ietf.org
-  기준은 “RFCs”라고 부름 -
  “Request for Comments”



**HTTP 요청을 만드는 법**

- 서버에 연결하고 “www.dr-chuck.com"
-  문서를 요청 (또는 기본 문서 요청)
  • GET http://www.dr-chuck.com/page1.htm HTTP/1.0
  • GET http://www.mlive.com/ann-arbor/ HTTP/1.0
  • GET http://www.facebook.com HTTP/1.0



$ telnet www.dr-chuck.com 80
Trying 74.208.28.177...
Connected to www.dr-chuck.com.Escape character is '^]'.
GET http://www.dr-chuck.com/page1.htm HTTP/1.0



HTTP/1.1 200 OK
Date: Thu, 08 Jan 2015 01:57:52 GMT
Last-Modified: Sun, 19 Jan 2014 14:25:43 GMT
Connection: close
Content-Type: text/html



<h1>The First page</h1>

<p>If yok like,  you can switch to
    the <a href="Http://www.dr-chuck.com/page2.htmm">secound
    page</a>.</p>
page</a>.</p>
conection closed bu foreign host
</p>



# Chapter 12 part 3

**간단한 웹 브라우저**

파이썬에서의 HTTP 요청

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
```

decode는 복호화



HTTP/1.1 200 OK

Date: Tue, 11 Feb 2020 18:47:16 GMT

Server: Apache/2.4.18 (Ubuntu)

Last-Modified: Sat, 13 May 2017 11:22:22 GMT

ETag: "a7-54f6609245537"

Accept-Ranges: bytes

Content-Length: 167

Cache-Control: max-age=0, no-cache, no-store, must-revalidate

Pragma: no-cache

Expires: Wed, 11 Jan 1984 05:00:00 GMT

Connection: close

Content-Type: text/plain   

​                                                                                                          HTTP 헤더

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

​                                                                                                          HTTP 바디

# <실습> 소켓

소켓 열고 명령 보내고 데이터를 받는 코드

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
```



# Chapter 12 part 4

**ASCII**

아스키 코드는 1 byte로 영문자와 숫자, 그리고 일부 특수문자들을 표현할 수 있습니다.
ord() 함수를 사용하면 다음과 같이 각각의 문자에 대한 아스키 코드 값을 확인할 수 있습니다.

```python
print(ord('H'))
# 72
print(ord('e'))
# 101
print(ord('\n'))
# 10
```



**유니코드(Unicode)**

유니코드 체계는 이미 몇 십억개의 문자를 포함하고 있으며, 새로운 문자 몇 십억개를 더 저장할 여력이 있습니다.
유니코드를 압축하는 UTF-8, UTF-16, UTF-32 등 다양한 방법이 있지만 가장 실용적인 방법은 UTF-8을 사용하는 것입니다.

- UTF-16 – 길이 고정됨 - 2 바이트
-  UTF-32 – 길이 고정됨 - 4 바이트
-  UTF-8 – 1-4 bytes

​        ASCII를 포함하며, 호환

​        ASCII를 자동으로 감지 가능

​        UTF-8 은 시스템 간에 데이터를 교환할 때
​        가장 실용적으로 추천되는 인코딩 형식입니다

- 파이썬3에서 모든 문자열은
  유니코드 형식
-  그러므로 파일에서 데이터를
  가져와 파이썬에서 작업하는 경우
  거의 대부분 “그냥 작동”합니다
- 그러나 소켓을 통해 네트워크로
  데이터를 전송하거나 DB와
  연결하는 경우 데이터를
  인코딩/디코딩해야 함 (UTF-8이
  많이 쓰임)

예전 파이썬 2.x 버전에서는 유니코드로 나타내고 싶으면 별도의 문자열 앞에 'u'라는 문자를 넣어주어야 했습니다.

```python
# Python 2.7.10 
x = '이광춘'
print(type(x))
# <type 'str'>
x = u'이광춘'
print(type(x))
# <type 'unicode'>
```

 그런데 파이썬 3.x 버전부터는 기본적으로 문자열이 유니코드로 저장이 됩니다.

```python
# Python 3.5.1
x = '이광춘'
print(type(x))
# <class 'str'>
x = u'이광춘'
print(type(x))
# <class 'str'>
```

하지만, 파이썬 내부에서 데이터를 사용하는 것이 아니라 네트워크를 통해 데이터를 주고 받을 때는 다른 형태로 데이터를 변환해야하는 경우도 있습니다.

다음 코드에서 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' 문자열은 유니코드입니다. 따라서 데이터를 전송하기 전에 UTF-8 byte 방식으로 인코딩를 해주어야 하는데, 그럴 때 사용되는 메소드가 encode() 입니다.

```python
'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
```

그리고 이렇게 인코딩된 문자열을 소켓을 통해 전송합니다.

```python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd
```



```python
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
```

이제 서버에서 받은 데이터를 data라는 변수에 저장합니다. 그리고 이 데이터는 현재 디코딩이 안 되어있기 때문에 decode() 메소드를 사용해 디코딩하여 출력하면 유니코드 형태로 우리에게 보여지는 것입니다.

**파이썬 문자열에서 Byte로**

- 네트워크 소켓 등 외부 자원과 통신하는 경우, 문자열이 아니라 Byte 형식을
  사용해야 함. 따라서 파이썬 3에서는 문자열을 Byte로 인코딩 필요
-  외부에서 데이터를 가져오는 경우 해당 문자셋에 대하여 디코딩을 해야
  파이썬3에서 정상적인 문자열으로 사용할 수 있다



# Chapter 12 part 5

**urllib 라이브러리**

urllib을 활용하면 아주 간단하게 웹 브라우저를 만들 수 있습니다.

```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
```

이전에 여러 줄에 걸쳐 만들었던 웹 브라우저가 urllib 라이브러리를 활용하면 이렇게 4줄만에 완성이 됩니다.

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief 

실행하면 이런 결과가 나옵니다

이것을 응용하면 이전에 파일에서 데이터를 읽어왔던 것을 인터넷에서 데이터를 읽어올 수 있습니다.

```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
```

이렇게 urllib을 이용하면 네트워크를 통해 문서를 다루는 과정을 비약적으로 줄이고

파일에서 데이터를 처리하는 과정도 굉장히 간소화 할 수 있습니다



앞에 나온 코드랑 같은 방식으로 웹페이지도 읽을 수 있습니다

```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
```

<h1>The First page</h1>

<p>If you like, you can swich to the <a
    href="http://www.dr-chuck.com/page2.htm">secondpage</a>.
</p>



# <실습> Urllib

단어의 출현 빈도에 대한 딕셔너리를 반환합니다

```python
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
```

url을 열고 딕셔너리를 만들어서 모든 줄을 반복하고 복호화 하고 단어 단위로 나눕니다

한번 line.decode() 파이썬 내부 문자 집합으로 바뀝니다 그리고 split()을 하고 개수를 셉니다

이전에 개수를 세기 위해 만든 코드와 다른게 없습니다



# Chapter12 part 6

**HTML 파싱
(웹 스크래핑라고도 함)**

**웹 스크래핑이란?**

- 프로그램이나 스크립트가 브라우저처럼 행동하며 페이지를
  살펴보고 정보를 추출하고 조사하는 것을 지칭
  검색엔진은 웹 페이지를 스크래핑함

- 이걸 스파이더링 또는 크롤링이라고도 함

**왜 스크래핑 하나?**

- 데이터를 가져오기 - 특히 소셜 데이터 - 누가 연결돼 있는지
-  외부로 내보내는 기능이 없는 시스템에서 데이터 가져오기
-  사이트를 모니터링하며 새로운 정보 감지
-  검색엔진의 데이터베이스를 구축하기 위한 스크래핑

**웹 페이지 스크래핑**

- 웹 페이지 스크래핑은 웹 페이지 내용을 마음대로 빼간다는
  점에서 논란의 여지가 있음
-  copyright된 정보를 다시 출판하는 것은 허용되지 않음
-  이용약관을 위배하지 않도록 유의



**BeautifulSoup을 활용한 웹 스크래핑**

BeautifulSoup는 아주 강력한 라이브러리입니다. 지난 시간에 배운 urllib과 더불어 사용하면 다음과 같이 원하는 웹 페이지에 존재하는 모든 링크의 URL을 출력할 수 있습니다.

```python
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
```





# <실습> BeautifulSoup

```python
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
```

urllip을 사용할거고 BeautifulSoup를 가져올 겁니다 BeautifulSoup 객체를 얻습니다

SSL 라이브러리를 쓰고 있고 우리가 다룰 사이트가 SSL을 사용하는데 해킹적인 관점에서 넣어줍니다

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

이 부분은 SSL 인증서 에러를 무시하는 방법입니다



BeautifulSoup를 urllib과 함께 사용하는 방법