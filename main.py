# news2atc
# initially created by Phonedolly at 2020-09-05
import os
import platform
import json
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import crawler
import sender

OS_TYPE = platform.system()
USER_AGENT = "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320"


def clear_screen():
    if OS_TYPE != 'Windows':
        os.system('clear')  # not windows
    else:
        os.system('cls')  # windows


def init():
    print("config.json 불러오는중...")
    try:
        with open('config.json', encoding='utf-8') as f:
            json_data = json.load(f)
            chrome_driver_dir = "chromedriver.exe"
            recruit_data = json_data['recruit']
            # PhantomJSDir = json_data['PhantomJSDir']

    except FileNotFoundError as e:
        print(e)
        print("config.json을 찾지 못했습니다.")
        exit(1)

    except KeyError as e:
        print(e)
        print("config.json의 형식이 올바르지 않습니다. config.json은 'ChromeDriverDir' 키와 적절한 값(chromedriver의 경로)을 포함해야합니다.")
        exit(1)

    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=" + USER_AGENT
    )
    print("Chrome Web Driver 초기화")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    return {'driver': driver, 'recruit_data': recruit_data}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO argv[]을 알맞게 처리하도록 개선하기. 참조: https://docs.python.org/ko/3.7/library/argparse.html

    initObj = init()
    driver = initObj['driver']
    recruit_data = initObj['recruit_data']

    while True:
        driver.get("https://github.com/Phonedolly/news2atc")
        clear_screen()
        print("=============Hello! news2atc=============")
        print("c. 뉴스 가져오고 훈련소로 보내기")
        print("h. 도움말")
        print("q. 끝내기")

        option = input("\n\n옵션을 입력하세요 : ")

        if option == 'c':
            article = crawler.crawler(driver)
            sender.sender(recruit_data, article, driver)

        elif option == 'h':
            clear_screen()
            print("=============Hello! news2atc=============")
            print("news2atc를 사용해주셔서 감사합니다!", end="\n\n")
            print(
                "네이버 뉴스의 기사를 받아와서 자동으로 육군 훈련소 인터넷 편지를 보냅니다. 첫 편지 발송 전 육군 훈련소 홈페이지에서 본인인증을 해야 하며, 이 프로그램의 지시를 따라 진행하시면 "
                "됩니다. 본인 인증 후 일정 시간 동안은 추가 인증없이 계속 발송할 수 있습니다.",
                end="\n")
            print("기사는 현재 모바일 버전 기준으로 인식됩니다. 따라서 m.naver.com이나 m.news.naver.com에서 확인할 수 있는 기사의 링크를 복사하셔야합니다.",
                  end="\n\n")
            print("이 프로그램의 소스 코드는 https://github.com/Phonedolly/news2atc에서 확인하실 수 있습니다.", end="\n\n")
            print("계속하려면 Enter", end="\n")
            input()


        elif option == 'q':
            print("Chrome Web Driver 종료 중...")
            driver.quit()

            print("bye <3")
            break

        else:
            clear_screen()
