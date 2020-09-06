
# Welcome to news2atc!😄  
>😓🚨아직 한참 개발중이예요. 현재 기사 자동 추출까지만 가능합니다.🚨🔨  
>최신 개발상황을 보려면 [**dev branch**](https://github.com/Phonedolly/news2atc/tree/dev)로 오세요. **dev**의 개발 내역은 안정화될 때마다 **master**로 병합됩니다.🌠
  
**news2atc**(*Naver **news** **to** korea **a**rmy **t**raining **c**enter*)는 육군훈련소에서 훈련중인 여러분의 가족👨‍👩‍👦, 친구👬, 혹은 애인💕에게 최신 네이버 뉴스 기사를 쉽고 빠르게 전달해줍니다!🚀  
  
# Requirements  
**news2atc**는 `python`으로 개발되어 Windows는 물론 Linux, macOS와 같은 다양한 플랫폼에서 실행할 수 있습니다. 다음과 같은 프로그램 및 라이브러리가 필요합니다.  
 - `python3` : 이 프로그램을 실행하기 위한 기본 인터프리터입니다.  
 - `selenium` : **Chrome Web Driver**로 **Chrome**을 조작하고 웹페이지 객체를 받아옵니다.  
 - `bs4` : `selenium`으로 받은 페이지 객체에서 필요한 정보를 손쉽게 추출합니다.  
 - [Chrome Web Driver](https://chromedriver.chromium.org/downloads)  
  
>**Note:** 아쉽게도 각 플랫폼별 실행 바이너리(*exe*, *run* 등)는 아직 준비되지 않아서, 여러분이 직접 `.py` 파일을 실행해야 합니다.  
  
# Setup  
## 프로젝트 다운로드  
  
**news2atc**를 다운로드합니다. 위로가서 **🥦초록색🥦 Code** 버튼을 누른 후 **💾Download ZIP**을 클릭하거나, [**여기**](https://github.com/Phonedolly/news2atc/archive/master.zip)를 눌러 다운로드하세요. 그런 다음 `master.zip`의 압축을 적절한 곳에 풉니다. **위치를 잘 기억해두세요.**  
  
압축을 풀면 다음과 같은 파일들이 있을 것입니다.  
  
 - `.gitignore`  
 - `main.py`  
 - `crawler.py`  
  
## Python과 라이브러리 설치  
**Python 3**이 필요합니다. [**여기**](https://www.python.org/downloads/)에서 파일을 받아 설치하세요.  
  
이제 필요한 Python 라이브러리들을 설치할 차례입니다. 터미널(윈도우의 경우, **CMD**또는 **Powershell**)에서 다음을 입력하세요.  
> **초보자 분들께 알려드립니다**: `$ `는 입력하지 마세요. `$`는 단순히 터미널에서 **한 줄의 시작**을 표시하기 위한 관용적 표현입니다.  
  
 $ pip install bs4 $ pip install selenium  
## Chrome Web Driver 받기  
  
### Chrome Web Driver 다운로드  
**news2atc**는 **Chrome Web Driver**를 통해 웹브라우저에서 렌더링된 DOM에서 간편하게 기사를 추출합니다. [**여기**](https://chromedriver.chromium.org/downloads)에서 **여러분이 지금 사용하는 크롬 브라우저 버전에 대응되는** Chrome Web Driver를 받으세요.  
  
>**초보자 분들을 위해:**  
>현재 사용하는 크롬의 버전은 주소창에 `chrome://version`을 입력하시고 **Enter⌨️**키를 누르면 확인하실 수 있어요.  
  
파일을 받고 압축을 풀면 Windows 기준으로 `chromedriver.exe`가 보일 것입니다. **이 파일의 위치를 잘 기억해둡니다.**  
  
### config.json 설정하기  
이제 **news2atc**가 Chrome Web Driver를 인식할 수 있도록 작업해봅시다. 다음과 같이 `master.zip`의 압축을 푼 곳에서 `config.json`을 생성합니다. `config.json`에서 `chromedriver.exe`의 **위치**를 `ChromeDriverDir` **Key**의 **Value**로 설정합니다. 아래는 예시입니다.  
  
#### config.json  
 { "ChromeDriverDir" : "C://chromedriver/chromedriver.exe" }  
# Run  
## 가져올 네이버 뉴스 링크 찾아보기  
**news2act**는 네이버 뉴스 모바일 페이지에서 뉴스를 가져오도록 만들어졌습니다. 아래 링크 중 하나에 접속하시면 됩니다.  
  
 - 네이버 모바일  
[m.naver.com](https://m.naver.com)  
  
 - 네이버 뉴스 모바일  
[m.news.naver.com](https://m.news.naver.com)  
  
위 페이지에서 아무 뉴스나 들어가셔서 해당 링크를 복사합니다. 아래와 같은 형식이 될 것입니다.  
  
 https://n.news.naver.com/mnews/article/022/0003500616?sid=103  
이 링크를 잘 복사해두세요.  
  
> **Q: 데스크톱 뉴스 페이지, 혹은 다른 사이트도 지원할 계획이 있나요?**  
>  
> 제 의지에 달렸습니다. 여러분이 이 프로젝트를 **Fork**하셔서 도와주시면 더 쉬워지겠죠!🤣  
  
## news2act 실행하기  
수고하셨습니다!😄 이제 **news2atc**를 실행해봅시다. **news2atc**의 압축을 푼 폴더에서 터미널을 열고 다음을 입력합니다. `main.py`가 있는 폴더가 맞습니다.  
  
 $ py main.py  > **Windows**에선 해당 폴더에서 **Shift**⌨️키를 누른 상태에서 **마우스 오른쪽 버튼🖱️**을 누르면 **여기에서 PowerShell 창 열기**를 선택하여 터미널을 열 수 있어요.  
  
이제 아래와 같이 나타납니다.  
  
 =============Hello! news2atc============= c. 뉴스 가져오기  
 q. 끝내기  
 h. 도움말  
       
    옵션을 입력하세요 :  
`c`를 입력해서 뉴스를 가져와봅시다. **Windows**의 경우 **방화벽 설정**이 표시될 수 있습니다. 허용해주도록 하세요.  
  
이제 프로그램이 **Chrome Web Driver**를 이용해 자동으로 크롬을 잠시 실행하고 닫습니다.  
  
>**⚠️새로 열린 크롬 창은 자동으로 닫힙니다. 임의로 닫지 마세요! ⚠️**  
  
잠시 뒤 프로그램 초기화면으로 돌아오면 `main.py`가 있던 위치에 `dump.news`가 생성되어 있을 것입니다. 이 `dump.news`파일은 텍스트 파일이기 때문에 **메모장**, **VSCode**, **Sublime Text** 등의 텍스트 에디터에서 쉽게 열 수 있습니다.  
  
>😓제가 작업한 것은 여기까지입니다. 추후에 계속 기능 추가를 할 예정이며, 일단은 `dump.news`파일을 열어서 기사를 복사해 인터넷 편지를 쓰시면 되겠습니다.🔨