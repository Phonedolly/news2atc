import requests
from bs4 import BeautifulSoup


# ct > div.media_end_head.go_trans > div.media_end_head_title > h2

def crawler():
    req = requests.get('https://n.news.naver.com/article/001/0011862376?cds=news_edit')
    html = req.text
    soup = BeautifulSoup(req.text, 'html.parser')  # python이 인식할 수 있는 html 객체로 변환

    journalName = soup.select_one(
        '#contents > div.media_end_linked_more > div > a > em'
    ).text  # 언론사 이름
    title = soup.select_one(
        '#ct > div.media_end_head.go_trans > div.media_end_head_title > h2'
    ).text  # 기사 제목

    # TODO 기사 내용 불러오기 (Selenium 써보기)
    contextList = soup.select(
        '#dic_area > span.article_p'
    )
    # dic_area > span:nth-child(40)
    # dic_area > span:nth-child(3)
    # dic_area > span:nth-child(11)

    context = []
    for i in range(0, 2):
        context[i] = contextList[i].text

    # TODO 기사 요약봇 내용 불러오기

    saver(journalName, title, context)


#  #contents > div.media_end_linked_more > div > a > em
def saver(journalName, title, context):
    with open("dump.news", 'w', encoding='utf-8') as f:
        f.write(journalName)
        f.write(title)
        f.write(context)
