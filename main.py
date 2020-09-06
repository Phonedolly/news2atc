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
    except KeyError:
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
            print("사용해주셔서 감사합니다! 이 프로그램의 소스 코드는 https://github.com/Phonedolly/news2atc에서 확인하실 수 있습니다.\n\n계속하려면 Enter",
                  end="\n\n")
            input()
