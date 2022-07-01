# 디버깅 없이 실행으로 실행 하여야함,,

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome('C:/Users/aq348/Desktop/Python/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://www.jobplanet.co.kr/users/sign_in?_nav=gb')

driver.find_element_by_name('user[email]').send_keys('eks1228@hotmail.co.kr')
driver.find_element_by_name('user[password]').send_keys('das71762076')
driver.find_element_by_class_name('btn_sign_up').click()
time.sleep(3)

f = open('csv_com_Fin_.csv','a', encoding='utf-8-sig')
wr = csv.writer(f)
wr.writerow(['이름', '총 별점', '리뷰 수', '복지 및 급여', '업무 와 삶의 균형', '사내문화', '승진 기회 및 가능성',' 경영진', '기업 추천율(%)', 'CEO 지지율(%)', '성장가능성(%)', '8시간 미만', '8시간', '9시간', '10시간', '11시간 이상', '야근 없음', '야근 1일 미만', '야근 1일', '야근 2일', '야근 3일 이상', '주말 근무 없음', '주말 근무 1일 미만', '주말 근무 1일', '주말 근무 2일', '주말 근무 3일 이상', '휴가 0-7일', '휴가 8-14일', '휴가 15-21일', '휴가 22-29일', '휴가 30일 이상', '업무일정 조정 자유', '업무일정 조정 상황따라', '업무일정 조정 눈치', '업무일정 조정 제한적', '업무일정 조정 어려움', '원격 자유', '원격 별도 신청', '원격 눈치', '원격 제한적', '원격 어려움'])
f.close()

u = open('finance_data.txt', 'r')
lines = u.readlines() # finance.csv 파일의 id가 리스트로 저장 되어있음
 # 에러나서 튕겼을 시 아래 문구 추가
 # lines = lines[이어갈 부분 id의 리스트 인덱스 : ]
u.close()

for Number in lines :
    # 프리미엄 리뷰
    driver.get('https://www.jobplanet.co.kr/companies/'+ str(Number) +'/premium_reviews')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="premium_detail_box"]/div[1]/div[1]/ul/li[4]/button').send_keys(Keys.ENTER)
    time.sleep(5)
    for t in range(500, 4001, 500) :
        driver.execute_script("window.scrollTo(0,"+str(t)+")")
        time.sleep(1)
    html2 = driver.page_source
    soup2 = bs(html2, 'html.parser')
    
    b_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_650 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    b_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_650 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    b_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_650 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    b_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_650 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    b_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_650 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    c_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_651 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    c_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_651 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    c_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_651 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    c_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_651 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    c_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_651 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    d_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_652 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    d_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_652 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    d_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_652 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    d_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_652 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    d_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_652 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    e_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_653 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    e_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_653 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    e_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_653 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    e_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_653 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    e_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_653 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    f_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_655 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    f_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_655 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    f_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_655 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    f_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_655 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    f_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_655 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    g_1 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_656 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(1) > span.statistic').string
    g_2 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_656 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(2) > span.statistic').string
    g_3 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_656 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(3) > span.statistic').string
    g_4 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_656 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(4) > span.statistic').string
    g_5 = soup2.select_one('#premium_detail_box > div.premium_detail_wrap > div.unit_chart_review_box > div > div.unit_chart_review_item.open.id_656 > div > div.review_status_box.success.multiple_single > div > div:nth-child(1) > ul > li:nth-child(5) > span.statistic').string
    
    # 리뷰
    driver.get('https://www.jobplanet.co.kr/companies/'+ str(Number) +'/reviews')
    time.sleep(3)
    html3 = driver.page_source
    soup3 = bs(html3, 'html.parser')
    
    name = soup3.select('body > div.body_wrap > div.cmp_hd > div.new_top_bnr > div > div.top_bnr_wrap > div > div > div.company_info_sec > div.company_info_box > div.company_name > h1 > a')[0].text 
    m_score = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_star_wrap.type2 > span').string
    vote = soup3.select_one('#viewCompaniesMenu > ul > li.viewReviews > a > span').string
    benefit = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_bar_set.barfill.total > div:nth-child(1) > div > div.rate_bar_unit > span.txt_point').string
    balance = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_bar_set.barfill.total > div:nth-child(2) > div > div.rate_bar_unit > span.txt_point').string
    culture = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_bar_set.barfill.total > div:nth-child(3) > div > div.rate_bar_unit > span.txt_point').string
    promote = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_bar_set.barfill.total > div:nth-child(4) > div > div.rate_bar_unit > span.txt_point').string
    board = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.left_sec > div.rate_bar_set.barfill.total > div:nth-child(5) > div > div.rate_bar_unit > span.txt_point').string
    recom_ = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.right_sec.rate_pie_group.premium_total_reviews > div:nth-child(1) > div.rate_pie.pie1 > span.txt_point').string[0:-1]
    ceo_ = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.right_sec.rate_pie_group.premium_total_reviews > div:nth-child(2) > div.rate_pie.pie2 > span.txt_point').string[0:-1]
    prob_ = soup3.select_one('#premiumReviewStatistics > div > div > div > div.stats_smr_sec.right_sec.rate_pie_group.premium_total_reviews > div:nth-child(3) > div.rate_pie.pie3 > span.txt_point').string[0:-1]
    
    f = open('csv_com_Fin_.csv','a', encoding='utf-8-sig')
    wr = csv.writer(f)
    wr.writerow([name, m_score, vote, benefit, balance, culture, promote, board, recom_, ceo_, prob_, b_1, b_2, b_3, b_4, b_5, c_1, c_2, c_3, c_4, c_5, d_1, d_2, d_3, d_4, d_5, e_1, e_2, e_3, e_4, e_5, f_1, f_2, f_3, f_4, f_5, g_1, g_2, g_3, g_4, g_5])
    f.close()