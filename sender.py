import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def sender(recruit_data, article, driver):
    # TODO 예외처리하기
    print("육군훈련소에 뉴스를 보냅니다.")
    # driver.implicitly_wait(1)

    # 800자 단위로 잘린 기사를 각각 보낸다.
    num_of_letter = len(article['articleContextList'])
    print("보낼 편지 수 : " + str(num_of_letter))
    for i in range(num_of_letter):
        if not write_letter(i, recruit_data, article, driver):
            print("편지를 보내는데 실패했습니다. 다시 시도해보세요")
            return


def is_require_login(driver):
    """
    본인 인증이 필요한지 확인한다
    :param driver: 현재 사용하고 있는 웹 드라이버 객체
    :return: 본인 인증의 필요 여부
    """
    # 찾지 못할 경우 -1을 리턴한다
    if driver.find_element_by_class_name('sub_wrap').text.find('실명제 적용 게시판입니다.') == -1:
        return False
    else:
        return True


def gen_password():
    """
    현재 날짜를 바탕으로 편지 비밀번호를 생성한다.
    예를 들어 현재 9월 10일일 경우, 비밀번호는 '0910'이 된다.

    :return: 생성한 비밀번호
    """

    month_num = datetime.datetime.now().month
    if month_num < 10:
        month = str("0" + str(month_num))
    else:
        month = str(month_num)

    day = str(datetime.datetime.now().day)

    password = month + day
    print("편지 비밀번호는 '" + password + "' 입니다")

    return password


def write_letter(letter_index, recruit_data, article, driver):
    is_success = True
    _atcURL = "http://www.katc.mil.kr/katc/community/children.jsp"

    # TODO 예외처리하기
    print("web driver 조작중...")
    print("육군훈련소 URL 접근중...")
    driver.get(_atcURL)

    # 검색조건 입력
    # 입영 날짜
    join_date_selector = Select(driver.find_element_by_id('search_val1'))
    join_date_selector.select_by_value(recruit_data['joinDate'])

    # 생년월일
    driver.find_element_by_id('birthDay').send_keys(recruit_data['birthDay'])

    # 훈련병 이름
    driver.find_element_by_id('search_val3').send_keys(recruit_data['name'])

    # 찾기 버튼 클릭
    # driver.find_element_by_xpath(
    #     '//*[@id="item_body"]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/form/fieldset/input[7]').click()
    driver.find_element_by_xpath(
        '//*[@id="item_body"]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/form/fieldset/input[7]').send_keys(Keys.ENTER)

    # 해당 장병 선택
    # TODO 같은 조건의 장병이 있을 때 선택하도록 하기
    driver.find_element_by_xpath('//*[@id="childInfo1"]').send_keys(Keys.ENTER)

    # 편지쓰기 버튼 클릭하기
    driver.find_element_by_xpath('//*[@id="letterBtn"]').click()

    # 본인인증이 필요한가
    if is_require_login(driver):
        print("인터넷 편지 작성을 위해 실명인증이 필요합니다")
        print("실명인증을 진행하세요")
        # 본인인증 버튼 클릭
        driver.find_element_by_xpath('//*[@id="fn_submit"]').send_keys(Keys.ENTER)

        # 사용자가 직접 본인인증을 하도록 240초 대기한다.
        try:
            element = WebDriverWait(driver, 240).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#jwxe_main_content > div > div > form > fieldset > '
                                                                 'div > div')))

        except TimeoutError:
            is_success = False
            print('제한 시간이 초과되었습니다. 다시 시도하세요.')

        print("본인인증에 성공하였습니다.")

    else:
        print("실명 인증 세션이 유지되고 있습니다")

    # 편지 입력 폼 채우기
    # 훈련병의 소속
    division = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[1]/td').text.strip()

    # 받는 사람
    to = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[2]/td').text.strip()
    # 보내는 사람
    me = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[3]/td').text.strip()

    print()
    print()
    print(str(letter_index + 1) + "번째 편지 입력 폼을 채웁니다.")
    print("소속 : " + division)
    print("받는 사람 : " + to)
    print("보내는 사람 : " + me)
    print("제목 : [" + str(letter_index + 1) + "]" + article['title'])
    driver.find_element_by_xpath('//*[@id="article_title"]').send_keys(
        "[" + str(letter_index + 1) + "]" + article['title'])
    print("내용 : " + article['articleContextList'][letter_index])
    driver.find_element_by_xpath('//*[@id="article_text"]').send_keys(article['articleContextList'][letter_index])
    print("비밀번호 생성중...")
    driver.find_element_by_xpath('//*[@id="writer_password"]').send_keys(gen_password())

    driver.find_element_by_xpath('//*[@id="jwxe_main_content"]/div/div/form/fieldset/div/div/input').send_keys(
        Keys.ENTER)

    driver.implicitly_wait(1)
    driver.switch_to.alert.accept()

    print("편지 작성을 성공했습니다.")
    return is_success
