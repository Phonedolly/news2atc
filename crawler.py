import json
import math

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def crawler(driver):
    news_url = input("뉴스의 URL을 입력하세요 : ")
    print("해당 URL에서 뉴스를 가져옵니다.")
    # driver.implicitly_wait(3)  # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려준다
    print("Web Driver 조작중...")

    # TODO .article_p 클래스 영역이 없는 기사를 처리하지 못함
    # TODO 더 다양한 예외 case에 대응해야한다
    # TODO try: 블록 줄이기
    try:
        print("URL 접근")

        driver.get(news_url)  # url에 접근한다

        print("html객체 파싱중..")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        print("webdriver 종료")

        print("컨텐츠 추출중...")
        journal_name = soup.select_one(
            '#contents > div.media_end_linked_more > div > a > em'
        ).text  # 언론사 이름
        title = soup.select_one(
            '#ct > div.media_end_head.go_trans > div.media_end_head_title > h2'
        ).text  # 기사 제목

        # article_p 클래스를 찾지 못하는 경우 예외처리로 이동한다.
        driver.find_element_by_class_name('article_p')

        # 기사 내용 (.arcitle_p로 분리되어있는 기사 문단들의 배열)
        article_element_list = soup.select(
            '#dic_area > span.article_p'
        )

        # articleElementList에서 기사를 수집해 article에 저장
        article_context = ""
        for article_element in article_element_list:
            article_context += article_element.text.strip() + '\n\n'  # articleElement.text의 맨 앞에 4단위 whitespace 제거

        article_context = article_context.rstrip()  # 마지막 공백('\n\n') 제거

    except NoSuchElementException:
        # TODO 기사의 문단 나눔까지 다 날라가는 현상 개선하기
        article_context = soup.select_one('#dic_area').get_text().strip()

    except ConnectionError:
        print("연결에 실패하였습니다. 다음을 확인해주세요 : ")
        print(" - 올바른 URL을 입력하였나요?")
        print(" - 네트워크에 연결되어있나요?")

        exit(1)

    article_context_list = article_context_splitter(article_context)  # 훈련소 편지 제한(800)길이로 나눈다
    article = {"journalName": journal_name, "title": title, "articleContextList": article_context_list,
               "articleContext": article_context}
    save_data(article=article)

    return article


def save_data(article):
    _file_name = "dump.news"
    print(_file_name + "에 저장중...")

    with open(_file_name, 'w', encoding='utf-8') as _plain_article:
        # https://docs.python.org/ko/3/library/os.html#os.linesep
        _plain_article.write("신문사 : " + article[
            'journalName'] + '\n')
        _plain_article.write("제목 : " + article['title'] + '\n')
        _plain_article.write("내용 : " + '\n')
        _plain_article.write(article['articleContext'] + '\n')
        print("기사가 " + _file_name + "에 저장되었습니다.")

    with open('dump.json', 'w', encoding='utf-8') as _json_data:
        json.dump(article, _json_data, ensure_ascii=False, indent=4)


def article_context_splitter(article_context):
    _context_length_limit = 800
    _first = 0

    article_context_list = []
    for i in range(math.ceil(len(article_context) / _context_length_limit)):
        _first = i * 800

        if (i + 1) * _context_length_limit < len(article_context):
            _last = (i + 1) * _context_length_limit
        else:
            _last = len(article_context)

        article_context_list.append(article_context[_first:_last])

    return article_context_list
