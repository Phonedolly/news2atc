---


---

<h1 id="welcome-to-news2atc😄">Welcome to news2atc!😄</h1>
<blockquote>
<p>최신 개발상황을 보려면 <a href="https://github.com/Phonedolly/news2atc/tree/dev"><strong>dev branch</strong></a>로 오세요. <strong>dev</strong>의 개발 내역은 안정화될 때마다 <strong>master</strong>로 병합됩니다.🌠</p>
</blockquote>
<p><strong>news2atc</strong>(<em>Naver <strong>news</strong> <strong>to</strong> korea <strong>a</strong>rmy <strong>t</strong>raining <strong>c</strong>enter</em>)는 육군훈련소에서 훈련중인 여러분의 가족👨‍👩‍👦, 친구👬, 혹은 애인💕에게 최신 네이버 뉴스 기사를 쉽고 빠르게 전달해줍니다!🚀</p>
<p><strong>유용한 링크들</strong></p>
<ul>
<li><a href="#%EB%B9%A0%EB%A5%B8-%EC%8B%9C%EC%9E%91"><strong>빠른 시작</strong></a> : <strong>python</strong>에 익숙하신 분들을 대상으로 한 빠른 시작 가이드</li>
<li><a href="#Requirements"><strong>자세한 설명</strong></a> : <strong>python</strong>을 모르시는 분들을 위한 자세하고 쉬운 가이드</li>
<li><a href="https://github.com/Phonedolly/news2atc/tree/dev"><strong>Dev 브런치</strong></a></li>
<li><a href="https://github.com/Phonedolly/news2atc/issues"><strong>이슈 트래커</strong></a> : 🚨<strong>news2atc</strong>에 문제가 있나요?</li>
</ul>
<h1 id="빠른-시작">빠른 시작</h1>
<p><strong>news2atc</strong>는 <a href="https://www.python.org/"><strong>python3</strong></a> 프로젝트입니다. <strong>python2</strong>에서는 동작을 보장하지 않습니다.</p>
<ol>
<li>
<p>우선 <code>bs4</code>와 <code>selenium</code>이 필요합니다. 필요에 따라 루트 디렉토리에서 <code>venv</code>를 구성하셔도 좋습니다.</p>
<pre><code> $ pip install bs4
 $ pip install selenium
</code></pre>
</li>
<li>
<p>여러분이 지금 사용하고 있는 크롬의 버전에 대응되는 <a href="https://chromedriver.chromium.org/downloads"><strong>ChromeDriver</strong></a>를 다운로드하고, 적절한 위치에 압축을 푸세요.</p>
</li>
<li>
<p><code>config.json</code>을 구성합니다. 이 파일은 프로젝트 <strong>루트 디렉토리</strong>에 저장하세요. 다음과 같이 작성합니다.</p>
<pre><code> {  
    "ChromeDriverDir" : "your_chrome_driver_path",  
    "recruit": {  
       "joinDate": "20200910",  
       "birthDay": "000101",  
       "name": "홍길동"  
 	}  
 }
</code></pre>
<p>세부사항은 아래 <strong>표</strong>를 참조하세요.</p>

<table>
<thead>
<tr>
<th>Key</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ChromeDriverDir</code></td>
<td><code>chromedriver.exe</code>의 경로</td>
</tr>
<tr>
<td><code>joinDate</code></td>
<td>입영 날짜. <code>YYYYMMDD</code> 형식으로 입력합니다. 예를 들어 <code>20200910</code>은 2020년 9월 10일을 의미합니다.</td>
</tr>
<tr>
<td><code>birthDay</code></td>
<td>훈련병의 생일. <code>YYMMDD</code>형식으로 입력합니다. 예를 들어 <code>000101</code>은 2000년 01월 01일을 의미합니다.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>훈련병의 이름</td>
</tr>
</tbody>
</table></li>
<li>
<p>이제 <code>main.py</code>를 실행합니다.</p>
<pre><code> $ py main.py
</code></pre>
<blockquote>
<p>프로그램을 실행하면 <strong>Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.</strong> 라는 표시가 있는 <strong>Chrome</strong> 창이 나타납니다. 이 창은 <strong>news2atc</strong>가 제어하므로 함부로 조작하지 마세요.</p>
</blockquote>
<p>다음과 같은 모습이 될 것입니다.</p>
<pre><code> =============Hello! news2atc=============  
 c. 뉴스 가져오고 훈련소로 보내기  
 h. 도움말  
 q. 끝내기
</code></pre>
<p>이제 <code>c</code>를 누르고 프로그램의 지시사항대로 진행해보세요.</p>
<blockquote>
<p>⚠️유의사항⚠️</p>
<ul>
<li>
<p><strong>news2act</strong>는 네이버 뉴스 모바일 페이지에서 뉴스를 가져오도록 만들어졌습니다. 아래 링크 중 하나에 접속하여 뉴스 기사의 URL을 구해보세요.</p>
<ul>
<li>네이버 모바일<br>
<a href="https://m.naver.com"><strong>m.naver.com</strong></a></li>
<li>네이버 뉴스 모바일<br>
<a href="https://m.news.naver.com"><strong>m.news.naver.com</strong></a></li>
</ul>
<p>아래와 같은 형식의 뉴스 기사 URL에서 작동합니다.<br>
<code>https://n.news.naver.com/mnews/article/022/0003500616?sid=103</code></p>
</li>
<li>
<p><strong>news2atc</strong>가 <strong>본인인증</strong>을 요구하면 <strong>240초</strong> 이내에 새로 나타난 본인인증 팝업을 이용해 인증을 완료해야합니다. 본인인증은 실제 Chrome 브라우저에서 동작하는 것과 동일하게 작동합니다. <strong>news2atc</strong>를 (육군 훈련소 측이 지정한)일정 시간 이상 대기시키거나 <strong>news2atc</strong>를 종료하는 경우 본인인증된 세션이 소멸됩니다.</p>
</li>
</ul>
</blockquote>
</li>
<li>
<p>프로그램 메인 메뉴에서 <code>q</code>를 누르면 <strong>Chrome Driver</strong>가 제어하는 크롬 창이 닫힌 뒤 프로그램이 종료됩니다.</p>
</li>
</ol>
<h1 id="requirements">Requirements</h1>
<p><strong>news2atc</strong>는 <code>python</code>으로 개발되어 Windows는 물론 Linux, macOS와 같은 다양한 플랫폼에서 실행할 수 있습니다. 다음과 같은 프로그램 및 라이브러리가 필요합니다.</p>
<ul>
<li><code>python3</code> : 이 프로그램을 실행하기 위한 기본 인터프리터입니다.</li>
<li><code>selenium</code> : <strong>Chrome Driver</strong>로 <strong>Chrome</strong>을 조작하고 웹페이지를 받아옵니다.</li>
<li><code>bs4</code> : <code>selenium</code>으로 받은 페이지에서 필요한 정보를 손쉽게 추출합니다.</li>
<li><a href="https://chromedriver.chromium.org/downloads"><strong>Chrome Driver</strong></a></li>
</ul>
<blockquote>
<p><strong>Note:</strong> 아쉽게도 각 플랫폼별 실행 바이너리(<em>exe</em>, <em>run</em> 등)는 아직 준비되지 않아서, 여러분이 직접 <code>.py</code> 파일을 실행해야 합니다.</p>
</blockquote>
<h1 id="setup">Setup</h1>
<h2 id="python과-라이브러리-설치">Python과 라이브러리 설치</h2>
<p><strong>Python 3</strong>이 필요합니다. <a href="https://www.python.org/downloads/"><strong>여기</strong></a>에서 파일을 받아 설치하세요.</p>
<p>이제 필요한 Python 라이브러리들을 설치할 차례입니다. 터미널(윈도우의 경우, <strong>CMD</strong>또는 <strong>Powershell</strong>)에서 다음을 입력하세요.</p>
<blockquote>
<p><strong>🐥초보자 분들께 알려드립니다</strong>: <code>$</code>는 입력하지 마세요. <code>$</code>는 단순히 터미널에서 <strong>한 줄의 시작</strong>을 표시하기 위한 관용적 표현입니다.</p>
</blockquote>
<pre><code>$ pip install bs4
$ pip install selenium
</code></pre>
<h2 id="프로젝트-다운로드">프로젝트 다운로드</h2>
<p><strong>news2atc</strong>를 다운로드합니다. 위로가서 <strong>🥦초록색🥦 Code</strong> 버튼을 누른 후 <strong>💾Download ZIP</strong>을 클릭하거나, <a href="https://github.com/Phonedolly/news2atc/archive/master.zip"><strong>여기</strong></a>를 눌러 다운로드하세요. 그런 다음 <code>master.zip</code>의 압축을 적절한 곳에 풉니다. <strong>위치를 잘 기억해두세요.</strong></p>
<p>압축을 풀면 다음과 같은 파일들이 있을 것입니다.</p>
<ul>
<li><code>.gitignore</code></li>
<li><code>main.py</code></li>
<li><code>crawler.py</code></li>
</ul>
<h2 id="chrome-driver-받기">Chrome Driver 받기</h2>
<h3 id="chrome-driver-다운로드">Chrome Driver 다운로드</h3>
<p><strong>news2atc</strong>는 <strong>Chrome Driver</strong>를 통해 웹브라우저에서 렌더링된 DOM에서 간편하게 기사를 추출합니다. <a href="https://chromedriver.chromium.org/downloads"><strong>여기</strong></a>에서 <strong>여러분이 지금 사용하는 크롬 브라우저 버전에 대응되는</strong> Chrome Driver를 받으세요.</p>
<blockquote>
<p><strong>🐥초보자 분들을 위해:</strong><br>
현재 사용하는 크롬의 버전은 주소창에 <code>chrome://version</code>을 입력하시고 <strong>Enter⌨️</strong>키를 누르면 확인하실 수 있어요.</p>
</blockquote>
<p>파일을 받고 압축을 풀면 Windows 기준으로 <code>chromedriver.exe</code>가 보일 것입니다. <strong>이 파일의 위치를 잘 기억해둡니다.</strong></p>
<h3 id="config.json-설정하기">config.json 설정하기</h3>
<p>이제 <strong>news2atc</strong>가 Chrome Driver를 인식할 수 있도록 작업해봅시다. 다음과 같이 <code>master.zip</code>의 압축을 푼 곳에서 <code>config.json</code>을 생성합니다.</p>
<p>다음과 같이 작성합니다.</p>
<pre><code>{  
   "ChromeDriverDir" : "your_chrome_driver_path",  
   "recruit": {  
      "joinDate": "20200910",  
      "birthDay": "000101",  
      "name": "홍길동"  
	}  
}
</code></pre>
<p>세부사항은 아래 <strong>표</strong>를 참조하세요.</p>

<table>
<thead>
<tr>
<th>Key</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ChromeDriverDir</code></td>
<td><code>chromedriver.exe</code>의 경로</td>
</tr>
<tr>
<td><code>joinDate</code></td>
<td>입영 날짜. <code>YYYYMMDD</code> 형식으로 입력합니다. 예를 들어 <code>20200910</code>은 2020년 9월 10일을 의미합니다.</td>
</tr>
<tr>
<td><code>birthDay</code></td>
<td>훈련병의 생일. <code>YYMMDD</code>형식으로 입력합니다. 예를 들어 <code>000101</code>은 2000년 01월 01일을 의미합니다.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>훈련병의 이름</td>
</tr>
</tbody>
</table><h1 id="run">Run</h1>
<h2 id="가져올-네이버-뉴스-링크-찾아보기">가져올 네이버 뉴스 링크 찾아보기</h2>
<p><strong>news2act</strong>는 네이버 뉴스 모바일 페이지에서 뉴스를 가져오도록 만들어졌습니다. 아래 링크 중 하나에 접속해보세요.</p>
<ul>
<li>
<p>네이버 모바일<br>
<a href="https://m.naver.com"><strong>m.naver.com</strong></a></p>
</li>
<li>
<p>네이버 뉴스 모바일<br>
<a href="https://m.news.naver.com"><strong>m.news.naver.com</strong></a></p>
</li>
</ul>
<p>위 페이지에서 아무 뉴스나 들어가셔서 해당 링크를 복사합니다. 아래와 같은 형식이 될 것입니다.</p>
<pre><code> https://n.news.naver.com/mnews/article/022/0003500616?sid=103
</code></pre>
<p>이 링크를 잘 복사해두세요.</p>
<blockquote>
<p><strong>Q: 데스크톱 뉴스 페이지, 혹은 다른 사이트도 지원할 계획이 있나요?</strong></p>
<p>여러분이 요청하신다면 추가해보겠습니다. <strong>Fork</strong>하셔서 기여해주시면 더욱 좋지요.</p>
</blockquote>
<h2 id="news2act-실행하기">news2act 실행하기</h2>
<p>수고하셨습니다!😄</p>
<p>이제 <strong>news2atc</strong>를 실행해봅시다. <strong>news2atc</strong>의 압축을 푼 폴더에서 터미널을 열고 다음을 입력합니다. <code>main.py</code>가 있는 폴더가 맞습니다.</p>
<pre><code> $ py main.py
</code></pre>
<blockquote>
<p><strong>Windows</strong>에선 해당 폴더에서 <strong>Shift</strong>⌨️키를 누른 상태에서 <strong>마우스 오른쪽 버튼🖱️</strong>을 누르면 <strong>여기에서 PowerShell 창 열기</strong>를 선택하여 터미널을 열 수 있어요.</p>
</blockquote>
<p>이제 아래와 같이 나타납니다.  또한 <strong>Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.</strong> 라는 표시를 가지는 새 <strong>Chrome</strong>창이 나타납니다.</p>
<pre><code> =============Hello! news2atc=============
 c. 뉴스 가져오기  
 q. 끝내기  
 h. 도움말  
       
 옵션을 입력하세요 :  
</code></pre>
<p><code>c</code>를 입력해서 뉴스를 가져와봅시다. URL을 입력하라는 표시가 나타날 것입니다. <a href="#%EA%B0%80%EC%A0%B8%EC%98%AC-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%89%B4%EC%8A%A4-%EB%A7%81%ED%81%AC-%EC%B0%BE%EC%95%84%EB%B3%B4%EA%B8%B0"><strong>가져올 네이버 뉴스 링크 찾아보기</strong></a>에서 구한 URL을 입력합니다.</p>
<blockquote>
<p><strong>Windows</strong>의 경우 <strong>방화벽 설정</strong>이 표시될 수 있습니다. 허용해주도록 하세요.</p>
</blockquote>
<p>이제 프로그램이 <strong>Chrome Driver</strong>를 이용해 뉴스를 받아온 뒤 스스로 육군훈련소 홈페이지에 접속합니다. 곧 <strong>본인 인증</strong>을 요구할 것입니다. 새롭게 나타난 <strong>본인 인증</strong> 팝업에서 <strong>본인 인증</strong>을 진행해주세요.<br>
<img src="https://i.ibb.co/5hr7JRQ/2020-09-12-222109.png" alt="본인인증 팝업"></p>
<p>이후 <strong>news2atc</strong>가 빠르게 편지 입력 form을 채우고 편지를 전송합니다. 뉴스 본문의 길이가 800자를 넘는 경우 <code>[1]뉴스제목</code>, <code>[2]뉴스제목</code>, <code>...</code>, <code>[n]뉴스제목</code>의 제목으로 기사를 나눠서 전송합니다. 예를 들어 본문 길이가 2400자인 경우, 총 3번의 편지를 작성하게 됩니다.</p>
<p>잠시 뒤 <strong>news2atc</strong>의 초기화면으로 돌아오면 <code>main.py</code>가 있던 위치에 <code>dump.json</code>과 <code>dump.news</code>이 생성되어 있을 것입니다. <code>dump.json</code>은 <strong>news2atc</strong>가 내부에서 생성한 뉴스 데이터를 <strong>그대로 출력</strong>한 것이고, <code>dump.news</code>는 뉴스의 <a href="https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A0%88%EC%9D%B8_%ED%85%8D%EC%8A%A4%ED%8A%B8"><strong>plain text</strong></a>만을 <strong>언론사 이름</strong>, <strong>제목</strong>, <strong>기사 본문</strong>의 형식으로 정리한 것입니다. <code>dump.news</code>는 📄텍스트 파일이기 때문에 <strong>메모장</strong>, <strong>VSCode</strong>, <strong>Sublime Text</strong> 등의 텍스트 에디터에서 쉽게 열 수 있습니다😀</p>
<p>계속하여 메인 화면에서 <code>c</code>를 누르고 새 뉴스 URL을 입력하는 방식으로 뉴스를 전송할 수 있습니다. <strong>본인 인증</strong>을 한 상태가 저장되어있기 때문에, <strong>news2atc</strong>를 종료하지 않는 한 추가로 본인인증을 할 필요가 없습니다.</p>
<blockquote>
<h3 id="news2atc의-사용자-여러분께"><strong>news2atc의 사용자 여러분께</strong></h3>
<p><strong>news2atc</strong>는 단지 약간의 불편함을 개선하기 위해 만들어진 프로그램입니다. 부디 <strong>💔악의적인 목적💢</strong>으로 사용하지 말아주세요. 육군훈련소도, 또 여러분의 훈련병도 그런 일을 원하지 않을 것입니다.</p>
</blockquote>

