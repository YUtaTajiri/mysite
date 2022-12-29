from bs4 import BeautifulSoup
import requests

#データを取り出すだけのプログラム
# webページの情報を取得する
site_data = requests.get('https://www.walkerplus.com/event_list/today/ar1046/')
soup = BeautifulSoup(site_data.content, 'html.parser')

# 特定のクラスだけ抜き出して表示
links = soup.select('.m-mainlist-item')
list1 = []
def get_title1():
    for link in links:
    #rstrip()で空白を作ることができる
        data = str(link.span.string).rstrip()
    # Noneを除外する
        if data == 'None':
            continue
    #変数linkの後ろにaタグを続ける事で「’aタグ’の’href’要素」を指定することができる
        result = 'https://www.walkerplus.com' + link.a.get('href')
        list1.append([data, result])



#webサイト2
site_data2 = requests.get('https://www.tjkagoshima.com/events/')
soup2 = BeautifulSoup(site_data2.content, 'html.parser')

links2 = soup2.select('.col-xs-6.col-sm-3')
list2 = []
def get_title2():
    for link2 in links2:
    #rstrip()で空白を作ることができる
        data2 = link2.text.rstrip()
        data2_limit = data2[:50]
    # Noneを除外する
        if data2 == 'None':
            continue
    #変数linkの後ろにaタグを続ける事で「’aタグ’の’href’要素」を指定することができる
        result2 =  link2.a.get('href')
        list2.append([data2_limit, result2])

#webサイト3
site_data3 = requests.get('https://amu.jrkagoshimacity.com/event/')
soup3 = BeautifulSoup(site_data3.content, 'html.parser')
links3 = soup3.select('.card__item__link')
list3 = []
def get_title3():
    for link3 in links3:
        data3 = link3.text.rstrip()
        result3 =link3.get('href')
    #https~が既についた状態で抽出されるタグがある為
        if 'https' in result3:
            list3.append([data3, result3])
        else:
            result3_new = 'https://amu.jrkagoshimacity.com/' + result3
            list3.append([data3, result3_new])

