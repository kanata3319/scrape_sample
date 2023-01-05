import argparse
import csv
import chromedriver_binary  # webdriver.Chromeを利用する場合必要
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    print('■ 処理開始(菊池市役所ホームページの新着情報をCSV出力)')

    # 引数
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help='please set filepath. ex) "/home/user/data.csv"', type=str)
    args = parser.parse_args()

    # webdriverの設定
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) # seconds
    driver.get('https://www.city.kikuchi.lg.jp/')

    # タイトルの取得 --> driver.title
    print('・タイトル: '+driver.title)

    # IDタグから要素を取得 --> driver.find_element(By.ID, 'id')
    # nameタグから要素を取得 --> driver.find_element(By.NAME, 'name')
    # ある要素までのパスを指定して要素を取得 --> driver.find_element(By.XPATH, 'xpath')
    # 新着情報の取得
    elements_datetime = driver.find_elements(By.XPATH, '//*[@id="topnews_content"]/ul/li/span')
    elements_title = driver.find_elements(By.XPATH, '//*[@id="topnews_content"]/ul/li/a')
    if len(elements_datetime) != len(elements_title):
        print('error.')

    # CSV出力
    with open(file=args.filepath, mode='wt', encoding='shift-jis') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\r\n', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['日付', 'タイトル', 'URL'])
        for i in range(len(elements_datetime)):
            writer.writerow([
                elements_datetime[i].text,
                elements_title[i].text,
                elements_title[i].get_attribute('href')  # aタグのhref(URL)を取得
            ])

    driver.quit()
    print('■ 処理終了')


if __name__ == "__main__":
    main()
