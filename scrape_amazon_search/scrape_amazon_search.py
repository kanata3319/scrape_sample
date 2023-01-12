# -*- coding: utf-8 -*-
import argparse
import csv
import chromedriver_binary  # webdriver.Chromeを利用する場合必要
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    print('■ 処理開始(amazonで検索し、結果をCSV出力)')

    # 引数
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help='please set filepath. ex) "/home/user/data.csv"', type=str)
    parser.add_argument("word", help='please set search word.', type=str)
    args = parser.parse_args()

    # webdriverの設定
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) # seconds
    driver.get('https://www.amazon.co.jp/ref=nav_logo')

    # タイトルの取得 --> driver.title
    print('・タイトル: '+driver.title)

    # 入力項目に入力--> elements_input.send_keys("入力内容")
    # 入力項目に入力--> elements_input.clear()
    elements_input = driver.find_element(By.ID, 'twotabsearchtextbox')
    elements_input.send_keys(args.word)
    driver.find_element(By.ID, 'nav-search-bar-form').submit()

    # 検索結果画面
    elements_results = driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div/div/div/div/div/div[2]/div[1]/h2/a[1]')

    # CSV出力
    with open(file=args.filepath, mode='wt', encoding='shift-jis') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\r\n', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['品名', 'URL', '金額'])
        for i in range(len(elements_results)):
            writer.writerow([
                elements_results[i].text,
                elements_results[i].get_attribute('href'),
            ])

    driver.quit()
    print('■ 処理終了')


if __name__ == "__main__":
    main()
