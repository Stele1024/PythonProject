import os
import re
import sys
import requests
from requests.exceptions import RequestException

print("Don't add / in the end of url.")
target_url = input('What is the url(examples:https://www.*****.com):')


def get_download_mp3_link(all_mp3_link_title):
    tests = []
    for subection in all_mp3_link_title:
        snap = []
        for link_title in subection:
            url = target_url + link_title[0]
            text = get_one_page_sourcecode(url=url)
            links_titles = re.findall(r'"page_title">(.*?)</div>.*?<audio\s?preload="auto"\s?src="(.*?)"></audio>', text , re.S)
            snap.extend(links_titles)
        tests.append(snap)
    return tests


def get_how_page(mp3_subsection_page_text):
    pattern = re.compile(r'下一页</a><a\s?href="(.*?).htm">尾页</a>', re.S)
    number = re.findall(pattern, mp3_subsection_page_text)
    return number


def get_one_page_sourcecode(url):
    """获取单个页面的源码"""
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                                 'Chrome/67.0.3396.99 Safari/537.36'}
        proxies = {'': ''}
        response = requests.get(url=url, headers=headers, proxies=proxies)  # response变量接收了requests实例返回的响应体
        response.encoding = 'utf-8'  # 设置了响应体的编码
        one_page_text = response.text  # 响应体的text属性可以获取响应体中的文本内容
        return one_page_text
    except RequestException as error:
        print('module_get_one_page_sourcecode', error)


def parse_mp3_column_page(mp3_column_page_text):
    """获取主页面内所有的MP3栏目的超链接和标题"""
    pattern = re.compile(r'<li><a\s?href="(.*?)".*?<h3>(.*?)</h3>.*?-->(.*?)<!--.*?</li>', re.S)  # 定义一个正则模式
    result = re.findall(pattern, mp3_column_page_text)  # 使用这个正则模式匹配MP3栏目的超链接和标题
    if result is None:
        raise Exception('正则匹配失败')
    else:
        return result


def parse_mp3_subsection_page(mp3_subsection_page_text):
    pattern = re.compile(r'<li><a\s?href="(.*?)".*?</span>(.*?)</a></li>', re.S)
    result = re.findall(pattern, mp3_subsection_page_text)
    if result is None:
        raise Exception('正则匹配失败')
    else:
        return result


def get_mp3_subsection_link_title(mp3_column_link_title):
    all_mp3_subsection_link_title = []
    # 第一个for获取一个column的总页面
    for count in range(len(mp3_column_link_title)):
        url = target_url+mp3_column_link_title[count][0]
        mp3_subsection_page_text = get_one_page_sourcecode(url=url)
        numbers = get_how_page(mp3_subsection_page_text)
        snap = []
        for i in range(1, int(numbers[0])+1):
            url = target_url+mp3_column_link_title[count][0]+str(i)+'.htm'
            mp3_subsection_page_text = get_one_page_sourcecode(url=url)
            mp3_subsection_link_title = parse_mp3_subsection_page(mp3_subsection_page_text)
            snap.extend(mp3_subsection_link_title)
        all_mp3_subsection_link_title.append(snap)
    return all_mp3_subsection_link_title


def get_all_mp3_subsection_link_title():
    all_mp3_link_title = []
    title = []
    for i in range(1, 4):
        url = target_url+'/htm/mp3avclass/'+str(i)+'.htm'
        mp3_column_page_text = get_one_page_sourcecode(url=url)
        mp3_column_link_title = parse_mp3_column_page(mp3_column_page_text=mp3_column_page_text)
        test = get_mp3_subsection_link_title(mp3_column_link_title)
        all_mp3_link_title.extend(test)
        tests = get_download_mp3_link(all_mp3_link_title=all_mp3_link_title)
        title.extend(mp3_column_link_title)
    return tests, title


def download_mp3(test, title):
    count = 0
    for subsection in test :
        os.makedirs('mp3/'+title[count][1])
        for link_title in subsection:
            with open('mp3/'+title[count][1]+'/'+link_title[0]+'.mp3', 'wb') as a :
                url = link_title[1]
                mp3 = requests.get(url=url).content
                a.write(mp3)
        count += 1


def main():
    tests, title = get_all_mp3_subsection_link_title()
    download_mp3(test=tests, title=title)

if __name__ == '__main__':
    main()
