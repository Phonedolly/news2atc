# news2atc
# initially created by Phonedolly at 2020-09-05
import os
import platform
import json

import crawler

OS_TYPE = platform.system()


def clearScreen():
    if OS_TYPE != 'Windows':
        os.system('clear')  # not windows
    else:
        os.system('cls')  # windows


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        with open('config.json') as f:
            json_data = json.load(f)
            ChromeDriverDir = json_data['ChromeDriverDir']
            # PhantomJSDir = json_data['PhantomJSDir']
    except Exception:
        print("config.json의 형식이 올바르지 않습니다. config.json은 'ChromeDriverDir' 키와 적절한 값(chromedriver의 경로)을 포함해야합니다.")
        exit(1)

    while (True):
        clearScreen()
        print("=============Hello! news2atc=============")
        print("c. 뉴스 가져오기")
        print("q. 끝내기")
        print("h. 도움말")

        option = input("\n\n옵션을 입력하세요 : ")

        if option == 'c':
            crawler.crawler(ChromeDriverDir)
        elif option == 'q':
            print("bye <3")
            break;
        elif option == 'h':
            clearScreen()
            print("=============Hello! news2atc=============")
            print("news2atc를 사용해주셔서 감사합니다!", end="\n\n")
            print("네이버 뉴스의 기사를 받아와서 자동으로 육군 훈련소 인터넷 편지를 보냅니다. 첫 편지 발송 전 육군 훈련소 홈페이지에서 본인인증을 해야 하며, 이 프로그램의 지시를 따라 진행하시면 됩니다. 본인 인증 후 일정 시간 동안은 추가 인증없이 계속 발송할 수 있습니다.", end="\n")
            print("기사는 현재 모바일 버전 기준으로 인식됩니다. 따라서 m.naver.com이나 m.news.naver.com에서 확인할 수 있는 기사의 링크를 복사하셔야합니다.", end="\n\n")
            print("이 프로그램의 소스 코드는 https://github.com/Phonedolly/news2atc에서 확인하실 수 있습니다.", end="\n\n")
            print("계속하려면 Enter", end="\n")
            input()
