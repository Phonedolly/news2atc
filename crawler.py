import os

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver

FNAME = "dump.news"


def crawler(ChromeDriverDir):
    newsUrl = input("뉴스의 URL을 입력하세요 : ")
    driver = webdriver.Chrome(ChromeDriverDir)
    # driver.implicitly_wait(3)  # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려준다
    print("webdriver 조작중...")
    print("url 접근")
    driver.get(newsUrl)  # url에 접근한다
    print("html객체 파싱중..")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    print("webdriver 종료")

    print("컨텐츠 추출중...")
    journalName = soup.select_one(
        '#contents > div.media_end_linked_more > div > a > em'
    ).text  # 언론사 이름
    title = soup.select_one(
        '#ct > div.media_end_head.go_trans > div.media_end_head_title > h2'
    ).text  # 기사 제목

    # 기사 내용 (.arcitle_p로 분리되어있는 기사 문단들의 배열)
    articleElementList = soup.select(
        '#dic_area > span.article_p'
    )

    # articleElementList에서 기사를 수집해 article에 저장
    article = ""
    for articleElement in articleElementList:
        article += articleElement.text.strip() + os.linesep  # articleElement.text에는 맨 앞에 4단위 whitespace가 존재한다. 이를 strip()으로 제거해준다.
    # 마지막 공백 제거
    article = article.rstrip()
    saver(journalName, title, article)


def saver(journalName, title, article):
    print(FNAME + "에 저장중...")
    with open(FNAME, 'w', encoding='utf-8') as f:
        f.write("신문사 : " + journalName + '\n')
        f.write("제목 : " + title + '\n\n')
        f.write(article)
        print("기사가 " + FNAME + "에 저장되었습니다.", end="\n\n")
    input("계속하려면 Enter")
