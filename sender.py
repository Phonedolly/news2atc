from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def sender(recruitData, articleData, ChromeDriverDir):
    atcURL = "http://www.katc.mil.kr/katc/community/children.jsp"

    print("육군훈련소에 뉴스를 보냅니다.")
    driver = webdriver.Chrome(ChromeDriverDir)
    driver.implicitly_wait(4)
    print("webdriver 조작중...")
    print("육군훈련소 URL 접근중...")
    driver.get(atcURL)

    obj = driver.page_source
    # 검색조건 입력
    # 입영 날짜
    joinDateSelector = Select(driver.find_element_by_id('search_val1'))
    joinDateSelector.select_by_value(recruitData['joinDate'])

    # 생년월일
    driver.find_element_by_id('birthDay').send_keys(recruitData['birthDay'])

    # 훈련병 이름
    driver.find_element_by_id('search_val3').send_keys(recruitData['name'])

    # 찾기 버튼 클릭
    driver.find_element_by_xpath(
        '//*[@id="item_body"]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/form/fieldset/input[7]').click()

    # 해당 장병 선택
    # TODO 같은 조건의 장병이 있을 때 선택하도록 하기
    driver.find_element_by_xpath('//*[@id="childInfo1"]').send_keys(Keys.ENTER)

    # 편지쓰기 버튼 클릭하기
    driver.find_element_by_xpath('//*[@id="letterBtn"]').click()

    # TODO 본인인증 요구 페이지인지 판단하는 함수 만들기

    # TODO USE while(True) FOR DEBUG PURPOSE ONLY
    while (True):
        pass
