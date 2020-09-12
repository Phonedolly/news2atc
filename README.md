# Welcome to news2atc!😄  
>최신 개발상황을 보려면 [**dev branch**](https://github.com/Phonedolly/news2atc/tree/dev)로 오세요. **dev**의 개발 내역은 안정화될 때마다 **master**로 병합됩니다.🌠
  
**news2atc**(*Naver **news** **to** korea **a**rmy **t**raining **c**enter*)는 육군훈련소에서 훈련중인 여러분의 가족👨‍👩‍👦, 친구👬, 혹은 애인💕에게 최신 네이버 뉴스 기사를 쉽고 빠르게 전달해줍니다!🚀



**유용한 링크들**
- [**빠른 시작**](#빠른-시작) : **python**에 익숙하신 분들을 대상으로 한 빠른 시작 가이드
- [**자세한 설명**](#Requirements) : **python**을 모르시는 분들을 위한 자세하고 쉬운 가이드
- [**Dev 브런치**](https://github.com/Phonedolly/news2atc/tree/dev)
- [**이슈 트래커**](https://github.com/Phonedolly/news2atc/issues) : 🚨**news2atc**에 문제가 있나요?

# 빠른 시작
**news2atc**는 [**python3**](https://www.python.org/) 프로젝트입니다. **python2**에서는 동작을 보장하지 않습니다.

1. 우선 `bs4`와 `selenium`이 필요합니다. 필요에 따라 루트 디렉토리에서 `venv`를 구성하셔도 좋습니다.

		$ pip install bs4
		$ pip install selenium

2. 여러분이 지금 사용하고 있는 크롬의 버전에 대응되는 [**ChromeDriver**](https://chromedriver.chromium.org/downloads)를 다운로드하고, 적절한 위치에 압축을 푸세요.
3. `config.json`을 구성합니다. 이 파일은 프로젝트 **루트 디렉토리**에 저장하세요. 다음과 같이 작성합니다.

		{  
		   "ChromeDriverDir" : "your_chrome_driver_path",  
		   "recruit": {  
		      "joinDate": "20200910",  
		      "birthDay": "000101",  
		      "name": "홍길동"  
			}  
		}
	세부사항은 아래 **표**를 참조하세요.
		
	|	Key|	Value|
	|	--|--|
	|	`ChromeDriverDir`|`chromedriver.exe`의 경로|
	|	`joinDate`|입영 날짜. `YYYYMMDD` 형식으로 입력합니다. 예를 들어 `20200910`은 2020년 9월 10일을 의미합니다.|
	|	`birthDay`|훈련병의 생일. `YYMMDD`형식으로 입력합니다. 예를 들어 `000101`은 2000년 01월 01일을 의미합니다.|
	|	`name`|훈련병의 이름|

4. 이제 `main.py`를 실행합니다.

		$ py main.py
	
	> 프로그램을 실행하면 **Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.** 라는 표시가 있는 **Chrome** 창이 나타납니다. 이 창은 **news2atc**가 제어하므로 함부로 조작하지 마세요.
	
	다음과 같은 모습이 될 것입니다.
	
		=============Hello! news2atc=============  
		c. 뉴스 가져오고 훈련소로 보내기  
		h. 도움말  
		q. 끝내기
	이제 `c`를 누르고 프로그램의 지시사항대로 진행해보세요.
	> ⚠️유의사항⚠️
	> - **news2act**는 네이버 뉴스 모바일 페이지에서 뉴스를 가져오도록 만들어졌습니다. 아래 링크 중 하나에 접속하여 뉴스 기사의 URL을 구해보세요.
	>
	> 	- 네이버 모바일  
	>[**m.naver.com**](https://m.naver.com)  
	>	- 네이버 뉴스 모바일  
	>[**m.news.naver.com**](https://m.news.naver.com) 
	>
	>	아래와 같은 형식의 뉴스 기사 URL에서 작동합니다.
	>`https://n.news.naver.com/mnews/article/022/0003500616?sid=103`
	> - **news2atc**가 **본인인증**을 요구하면 **240초** 이내에 새로 나타난 본인인증 팝업을 이용해 인증을 완료해야합니다. 본인인증은 실제 Chrome 브라우저에서 동작하는 것과 동일하게 작동합니다. **news2atc**를 (육군 훈련소 측이 지정한)일정 시간 이상 대기시키거나 **news2atc**를 종료하는 경우 본인인증된 세션이 소멸됩니다.
5. 프로그램 메인 메뉴에서 `q`를 누르면 **Chrome Driver**가 제어하는 크롬 창이 닫힌 뒤 프로그램이 종료됩니다.
 
  
# Requirements  
**news2atc**는 `python`으로 개발되어 Windows는 물론 Linux, macOS와 같은 다양한 플랫폼에서 실행할 수 있습니다. 다음과 같은 프로그램 및 라이브러리가 필요합니다.  
 - `python3` : 이 프로그램을 실행하기 위한 기본 인터프리터입니다.  
 - `selenium` : **Chrome Driver**로 **Chrome**을 조작하고 웹페이지를 받아옵니다.  
 - `bs4` : `selenium`으로 받은 페이지에서 필요한 정보를 손쉽게 추출합니다. 
 - [**Chrome Driver**](https://chromedriver.chromium.org/downloads)  
  
>**Note:** 아쉽게도 각 플랫폼별 실행 바이너리(*exe*, *run* 등)는 아직 준비되지 않아서, 여러분이 직접 `.py` 파일을 실행해야 합니다.  
  
# Setup
## Python과 라이브러리 설치  
**Python 3**이 필요합니다. [**여기**](https://www.python.org/downloads/)에서 파일을 받아 설치하세요.  
  
이제 필요한 Python 라이브러리들을 설치할 차례입니다. 터미널(윈도우의 경우, **CMD**또는 **Powershell**)에서 다음을 입력하세요.  
> **🐥초보자 분들께 알려드립니다**: `$ `는 입력하지 마세요. `$`는 단순히 터미널에서 **한 줄의 시작**을 표시하기 위한 관용적 표현입니다. 

	$ pip install bs4
	$ pip install selenium
	
## 프로젝트 다운로드  
  
**news2atc**를 다운로드합니다. 위로가서 **🥦초록색🥦 Code** 버튼을 누른 후 **💾Download ZIP**을 클릭하거나, [**여기**](https://github.com/Phonedolly/news2atc/archive/master.zip)를 눌러 다운로드하세요. 그런 다음 `master.zip`의 압축을 적절한 곳에 풉니다. **위치를 잘 기억해두세요.**  
  
압축을 풀면 다음과 같은 파일들이 있을 것입니다.  
  
 - `.gitignore`  
 - `main.py`  
 - `crawler.py`  

## Chrome Driver 받기  
  
### Chrome Driver 다운로드  
**news2atc**는 **Chrome Driver**를 통해 웹브라우저에서 렌더링된 DOM에서 간편하게 기사를 추출합니다. [**여기**](https://chromedriver.chromium.org/downloads)에서 **여러분이 지금 사용하는 크롬 브라우저 버전에 대응되는** Chrome Driver를 받으세요.  
  
>**🐥초보자 분들을 위해:**  
>현재 사용하는 크롬의 버전은 주소창에 `chrome://version`을 입력하시고 **Enter⌨️**키를 누르면 확인하실 수 있어요.  
  
파일을 받고 압축을 풀면 Windows 기준으로 `chromedriver.exe`가 보일 것입니다. **이 파일의 위치를 잘 기억해둡니다.**  
  
### config.json 설정하기  
이제 **news2atc**가 Chrome Driver를 인식할 수 있도록 작업해봅시다. 다음과 같이 `master.zip`의 압축을 푼 곳에서 `config.json`을 생성합니다.

다음과 같이 작성합니다.

	{  
	   "ChromeDriverDir" : "your_chrome_driver_path",  
	   "recruit": {  
	      "joinDate": "20200910",  
	      "birthDay": "000101",  
	      "name": "홍길동"  
		}  
	}
세부사항은 아래 **표**를 참조하세요.
	
|	Key|	Value|
|	--|--|
|	`ChromeDriverDir`|`chromedriver.exe`의 경로|
|	`joinDate`|입영 날짜. `YYYYMMDD` 형식으로 입력합니다. 예를 들어 `20200910`은 2020년 9월 10일을 의미합니다.|
|	`birthDay`|훈련병의 생일. `YYMMDD`형식으로 입력합니다. 예를 들어 `000101`은 2000년 01월 01일을 의미합니다.|
|	`name`|훈련병의 이름|

# Run  
## 가져올 네이버 뉴스 링크 찾아보기  
**news2act**는 네이버 뉴스 모바일 페이지에서 뉴스를 가져오도록 만들어졌습니다. 아래 링크 중 하나에 접속해보세요.
  
 - 네이버 모바일  
[**m.naver.com**](https://m.naver.com)  
  
 - 네이버 뉴스 모바일  
[**m.news.naver.com**](https://m.news.naver.com) 
  
위 페이지에서 아무 뉴스나 들어가셔서 해당 링크를 복사합니다. 아래와 같은 형식이 될 것입니다.

     https://n.news.naver.com/mnews/article/022/0003500616?sid=103


이 링크를 잘 복사해두세요.  
  
> **Q: 데스크톱 뉴스 페이지, 혹은 다른 사이트도 지원할 계획이 있나요?**  
>  
> 여러분이 요청하신다면 추가해보겠습니다. **Fork**하셔서 기여해주시면 더욱 좋지요.
  
## news2act 실행하기  
수고하셨습니다!😄

이제 **news2atc**를 실행해봅시다. **news2atc**의 압축을 푼 폴더에서 터미널을 열고 다음을 입력합니다. `main.py`가 있는 폴더가 맞습니다.  

     $ py main.py

 > **Windows**에선 해당 폴더에서 **Shift**⌨️키를 누른 상태에서 **마우스 오른쪽 버튼🖱️**을 누르면 **여기에서 PowerShell 창 열기**를 선택하여 터미널을 열 수 있어요.  
  

이제 아래와 같이 나타납니다.  또한 **Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.** 라는 표시를 가지는 새 **Chrome**창이 나타납니다.

     =============Hello! news2atc=============
     c. 뉴스 가져오기  
     q. 끝내기  
     h. 도움말  
           
     옵션을 입력하세요 :  

`c`를 입력해서 뉴스를 가져와봅시다. URL을 입력하라는 표시가 나타날 것입니다. [**가져올 네이버 뉴스 링크 찾아보기**](#가져올-네이버-뉴스-링크-찾아보기)에서 구한 URL을 입력합니다.
>**Windows**의 경우 **방화벽 설정**이 표시될 수 있습니다. 허용해주도록 하세요. 
  
이제 프로그램이 **Chrome Driver**를 이용해 뉴스를 받아온 뒤 스스로 육군훈련소 홈페이지에 접속합니다. 곧 **본인 인증**을 요구할 것입니다. 새롭게 나타난 **본인 인증** 팝업에서 **본인 인증**을 진행해주세요.

![본인인증 팝업](https://i.ibb.co/5hr7JRQ/2020-09-12-222109.png)
 
이후 **news2atc**가 빠르게 편지 입력 form을 채우고 편지를 전송합니다. 뉴스 본문의 길이가 800자를 넘는 경우 `[1]뉴스제목`, `[2]뉴스제목`, `...`, `[n]뉴스제목`의 제목으로 기사를 나눠서 전송합니다. 예를 들어 본문 길이가 2400자인 경우, 총 3번의 편지를 작성하게 됩니다.

잠시 뒤 **news2atc**의 초기화면으로 돌아오면 `main.py`가 있던 위치에 `dump.json`과 `dump.news`이 생성되어 있을 것입니다. `dump.json`은 **news2atc**가 내부에서 생성한 뉴스 데이터를 **그대로 출력**한 것이고, `dump.news`는 뉴스의 [**plain text**](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A0%88%EC%9D%B8_%ED%85%8D%EC%8A%A4%ED%8A%B8)만을 **언론사 이름**, **제목**, **기사 본문**의 형식으로 정리한 것입니다. `dump.news`는 📄텍스트 파일이기 때문에 **메모장**, **VSCode**, **Sublime Text** 등의 텍스트 에디터에서 쉽게 열 수 있습니다😀

계속하여 메인 화면에서 `c`를 누르고 새 뉴스 URL을 입력하는 방식으로 뉴스를 전송할 수 있습니다. **본인 인증**을 한 상태가 저장되어있기 때문에, **news2atc**를 종료하지 않는 한 추가로 본인인증을 할 필요가 없습니다.

> ### **news2atc의 사용자 여러분께**
> **news2atc**는 단지 약간의 불편함을 개선하기 위해 만들어진 프로그램입니다. 부디 **💔악의적인 목적💢**으로 사용하지 말아주세요. 육군훈련소도, 또 여러분의 훈련병도 그런 일을 원하지 않을 것입니다.
