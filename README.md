# スクレイピングのサンプル(Kikuchi市役所HPの新着情報をCSV出力)

## 使い方
```
python scrape_sample.py /home/user/data.csv
```
![image](https://user-images.githubusercontent.com/116167055/210737604-7bd6c3b5-76ae-4ffc-a3fe-c099cdcb0e68.png)
![image](https://user-images.githubusercontent.com/116167055/210738004-d3d08f20-2fb1-46ad-8876-6f3dbb736406.png)
![image](https://user-images.githubusercontent.com/116167055/210737890-ea7d2b74-2db9-4d1a-a43d-7b44f9f69e2b.png)

## インストール方法
* Pythonインストール
  * 開発環境は3.9.10で作成
  * requirements.txtから必要ライブラリをインストール
  
* Chromeインストール
```
vi /etc/yum.repos.d/google-chrome.repo
-------------------
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
-------------------
yum -y install google-chrome-stable
google-chrome --version
```
