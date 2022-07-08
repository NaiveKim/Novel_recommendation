import columns as columns
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

#######################전체카테고리 페이지###########################
# https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=all&genreCode=&orderTypeCode=sale&is&isFinished=false&page=1 ~ 500까지

#######################인기순 변경###############################
# //*[@id="_ico_arrow"] ------------정렬순
# //*[@id="content"]/div/div/div[2]/div/div[2]/ul/li[2]/a ------인기순
#######################소설링크 x path################################
# //*[@id="content"]/div/ul/li[1]/div/h3/a 소설 링크 xpath
# //*[@id="content"]/div/ul/li[2]/div/h3/a
# //*[@id="content"]/div/ul/li[25]/div/h3/a 1~25
#######################소설 페이지############################3
# //*[@id="content"]/div[1]/h2   ---- 제목
# //*[@id="content"]/ul[1]/li/ul/li[2]/span/a ----- 장르
# //*[@id="content"]/ul[1]/li/ul/li[3]/a ------ 작가
# //*[@id="content"]/div[2] ---- 작품소개
# //*[@id="content"]/div[2]/div[2]
# //*[@id="content"]/div[2]/div[1]/span/a
# //*[@id="content"]/div[2]
# //*[@id="content"]/div[2]/div[2]
# //*[@id="reviewCount"] ------댓글창
# //*[@id="cbox_module_wai_u_cbox_sort_option_tab2"]/span[2] 전체댓글 변경
#######################댓글####################################
# //*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[1]/div[1]/div/div[2]
# //*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[2]/div[1]/div/div[2]
# //*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[15]/div[1]/div/div[2]
#######################댓글 페이지 변경#########################
# //*[@id="cbox_module"]/div/div[7]/div/a[1] -----1에서 2
# //*[@id="cbox_module"]/div/div[7]/div/a[3] -----2에서 3
# //*[@id="cbox_module"]/div/div[7]/div/a[4] -----3에서 4
# //*[@id="cbox_module"]/div/div[7]/div/a[5] -----4에서 5
# //*[@id="cbox_module"]/div/div[7]/div/a[6] -----5에서 다음

# //*[@id="cbox_module"]/div/div[7]/div/a[3]

##//*[@id="content"]/div/ul/li[1]/div/h3
##//*[@id="content"]/div/ul/li[2]/div/h3
##//*[@id="content"]/div/ul/li[1]/div/h3/em

audult_signal = '//*[@id="content"]/div/ul/li[1]/div/h3/em'
genre_xpath = '//*[@id="content"]/ul[1]/li/ul/li[2]/span/a'
author_xpath = '//*[@id="content"]/ul[1]/li/ul/li[3]/a'
intro_xpath = '//*[@id="content"]/div[2]/div[2]'
comment_btn_xpath = '//*[@id="reviewCount"]'
all_comment_btn_xpath = '//*[@id="cbox_module_wai_u_cbox_sort_option_tab2"]/span[2]'
comment_number_xpath = '//*[@id="cbox_module"]/div/div[1]/span'
comment_first_page_xpath = '//*[@id="cbox_module"]/div/div[7]/div/strong/span[1]'

review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'                   #review button
#                      //*[@id="movieEndTabMenu"]/li[6]/a
end_page = 3 # 할당받은 페이지로 수정하세요.

# //*[@id="cbox_module"]/div/div[7]/div/a[7]/span[1]
# //*[@id="cbox_module"]/div/div[7]/div/a[3]/span

for i in range(1, end_page+1): #할당받은 끝 페이지
    url = 'https://series.naver.com/novel/categoryProductList.series?categoryTypeCode=all&genreCode=&orderTypeCode=sale&is&isFinished=false&page={}'.format(i)
    titles = []
    genres = []
    authors = []
    intros = []
    comments = []
    try:

        for j in range(1, 3): #25 -- 한 페이지에 25개 소설
            driver.get(url)
            time.sleep(0.5)
            novel_xpath = '//*[@id="content"]/div/ul/li[{}]/div/h3/a'.format(j)  # 소설페이지

            try:
                title = driver.find_element("xpath", novel_xpath).text # 소설 제목 따기
                driver.find_element("xpath", novel_xpath).click() # 소설 제목 클릭
                time.sleep(0.3)
                genre = driver.find_element('xpath', genre_xpath).text # 소설 장르 따기
                author = driver.find_element('xpath', author_xpath).text # 소설 작가 따기
                # driver.find_element('xpath','//*[@id="content"]/div[2]/div[1]/span/a').click
                intro = driver.find_element('xpath', intro_xpath).text # # 소설 소개 따기
                titles.append(title)
                genres.append(genre)
                authors.append(author)
                intros.append(intro)
                driver.find_element('xpath', comment_btn_xpath).click() # 댓글창 이동
                time.sleep(0.3)
                driver.find_element('xpath', all_comment_btn_xpath).click()
                time.sleep(0.3)
                comment_range = driver.find_element('xpath', comment_number_xpath).text
                comment_range = comment_range.replace(',', '')
                comment_range = (int(comment_range)-1) // 75 + 2 #댓글 한페이지당 15개 댓글, 5개씩 댓글 페이지 정렬
                try:
                    comment_page = [1, 3, 4, 5, 6]
                    to_comment_page = [3, 4, 5, 6, 7]

                    for k in range(1, 16):
                        comment_xpath = '//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[{}]/div[1]/div/div[2]'.format(k)
                        comment = driver.find_element('xpath', comment_xpath).text
                        comments.append(comment)

                    try:
                        for l in comment_page:
                            driver.find_element('xpath', '//*[@id="cbox_module"]/div/div[7]/div/a[{}]'.format(l)).click()
                            time.sleep(0.3)

                            for m in range(1, 16):
                                comment_xpath = '//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[{}]/div[1]/div/div[2]'.format(m)
                                comment = driver.find_element('xpath', comment_xpath).text
                                comments.append(comment)


                    except:
                        print('comment pages1', i, j, l, m)
                    try:
                        for n in range(1, 4): #comment_range
                            try:
                                for o in to_comment_page:
                                    driver.find_element('xpath','//*[@id="cbox_module"]/div/div[7]/div/a[{}]'.format(o)).click()
                                    time.sleep(0.3)

                                    for p in range(1, 16):
                                        comment_xpath = '//*[@id="cbox_module_wai_u_cbox_content_wrap_tabpanel"]/ul/li[{}]/div[1]/div/div[2]'.format(p)
                                        comment = driver.find_element('xpath', comment_xpath).text
                                        comments.append(comment)
                            except:
                                print('comment_each', i, j, l, m, o, p)
                    except:
                        print('comment pages', i, j, l, m, o)
                    driver.back()
                except:
                    print('comment page', i, j, l, m)
                # driver.back()
            except:
                print('novel', i, j)
        print(len(titles))
        df = pd.DataFrame({'titles':titles, 'genres':genres, 'authors':authors, 'intros':intros, 'comments':comments})
        df.to_csv('./crawling_data/naver_comments_test_page.csv', index=False)#.format(end_page, i), index=False)
    except:
        print('page', i)



driver.close()