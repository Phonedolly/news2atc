from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def sender(recruit_data, article, chrome_driver_dir):
    # TODO 예외처리하기
    print("육군훈련소에 뉴스를 보냅니다.")
    driver = webdriver.Chrome(chrome_driver_dir)
    driver.implicitly_wait(4)

    num_of_letter = len(article['articleContextList'])
    print("보낼 편지 수 : " + str(num_of_letter))
    for i in range(num_of_letter):

        if not write_letter(recruit_data, article, driver):
            print("편지를 보내는데 실패했습니다. 다시 시도해보세요")
            return

    # TODO USE while(True) FOR DEBUG PURPOSE ONLY
    while (True):
        pass


def require_login(driver):
    if driver.find_element_by_class_name('sub_wrap').text.find('실명제 적용 게시판입니다.'):
        return True
    else:
        return False


def write_letter(recruit_data, article, driver):
    is_success = True
    _atcURL = "http://www.katc.mil.kr/katc/community/children.jsp"

    # TODO 예외처리하기
    print("webdriver 조작중...")
    print("육군훈련소 URL 접근중...")
    driver.get(_atcURL)

    obj = driver.page_source
    # 검색조건 입력
    # 입영 날짜
    joinDateSelector = Select(driver.find_element_by_id('search_val1'))
    joinDateSelector.select_by_value(recruit_data['joinDate'])

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
    if require_login(driver):
        print("인터넷 편지 작성을 위해 실명인증이 필요합니다")
        print("실명인증을 진행하세요")
        # 본인인증 버튼 클릭
        driver.find_element_by_xpath('//*[@id="fn_submit"]').send_keys(Keys.ENTER)
        #
        try:
            element = WebDriverWait(driver, 240).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#jwxe_main_content > div > div > form > fieldset > div > div')))

        except TimeoutError:
            is_success = False
            print('제한 시간이 초과되었습니다. 다시 시도하세요.')

        finally:
            pass

    else:
        print("실명 인증 세션이 유지되고 있습니다")

    # 편지 입력 폼 채우기

    division = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[1]/td').text.strip()

    to = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[2]/td').text.strip()
    me = driver.find_element_by_xpath(
        '//*[@id="jwxe_main_content"]/div/div/form/fieldset/table/tbody/tr[3]/td').text.strip()

    print("소속 : " + division)
    print("받는 사람 : " + to)
    print("보내는 사람 : " + me)

    # TODO USE while(True) FOR DEBUG PURPOSE ONLY
    while True:
        pass

    return is_success
