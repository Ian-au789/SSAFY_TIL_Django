import os
import sys
import django
from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crawl_toss_comments_by_name(stock_name, target_count=20):
    options = Options()
    # options.add_argument("--headless")  # 필요시 활성화
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. 토스 메인 페이지 접속
        driver.get("https://tossinvest.com/")
        time.sleep(2)

        # 2. 돋보기 버튼 클릭 → 검색창 열기
        search_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[aria-haspopup="dialog"]')
        ))
        search_button.click()
        time.sleep(1)

        # 3. 검색창에 종목명 입력
        search_input = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "_1x1gpvi6")
        ))
        search_input.send_keys(stock_name)
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)

        # 4. 종목 상세 페이지 진입 대기
        wait.until(EC.url_contains("/stocks/"))
        time.sleep(2)

        # 5. 종목 코드 추출
        current_url = driver.current_url
        code = current_url.split("/stocks/")[1].split("/")[0]

        # 6. 커뮤니티 탭 클릭
        community_tab = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-contents-label="커뮤니티"]')
        ))
        community_tab.click()

        # 7. 커뮤니티 페이지 로딩 대기
        wait.until(EC.url_contains("/community"))
        time.sleep(2)

        # 8. 댓글 더 많이 로딩되도록 스크롤
        for _ in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            spans = driver.find_elements(By.CLASS_NAME, "_60z0ev1")
            if len(spans) >= target_count:
                break

        # 9. 수집 결과 반환 dictionary 
        comments = []
        for span in spans[:target_count]:
            text = span.text.strip()
            if len(text) < 80:
                comments.append(text)

        return {
            "title": stock_name,
            "code": code,
            "comments": comments
        }

    except Exception as e:
        print(f"에러 발생: {e}")
        return None

    finally:
        driver.quit()
