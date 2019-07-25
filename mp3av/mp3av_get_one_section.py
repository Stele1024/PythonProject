import re
import os
import requests

print("Note: Don't add / in end of url.")
target_url = input('Audio_section_URL:') 
host_url = input('Maomiav_url(examples:https://www.****.com):')


def get_one_page_sourcecode(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) \
    AppleWebKit/537.36 (KHTML, like Gecko)Chrome/67.0.3396.99 Safari/537.36'}
    proxies = {'': ''}
    response = requests.get(url=url, headers=headers, proxies=proxies)
    response.encoding = 'utf-8'
    text = response.text
    return text


def get_all_number_page(text):
    return int(re.findall(r'下一页</a><a\s?href="(.*?).htm">尾页</a>',
                          text, re.S)[0])


def parse_section_link_title(text):
    pattern = re.compile(r'<li>.*?href="(.*?)".*?</span>(.*?)</a></li>', re.S)
    result = re.findall(pattern, text)
    return result


def get_section_link_title():
    text = get_one_page_sourcecode(target_url)
    number = get_all_number_page(text)
    links_titles = []
    for numbers in range(1, number+1):
        url = target_url+str(numbers)+'.htm'
        text = get_one_page_sourcecode(url=url)
        link_title = parse_section_link_title(text=text)
        links_titles.extend(link_title)
    return links_titles


def get_download_link(links_titles):
    title_link = []
    for section in links_titles:
        url = host_url+section[0]
        text = get_one_page_sourcecode(url=url)
        result = re.findall(r'"page_title">(.*?)</div>.*?src="(.*?)"></audio>',
                            text, re.S)
        title_link.extend(result)
    return title_link


def download_mp3(title_link):
    title = title_link[0][0][:7]
    os.makedirs('mp3/'+title)
    count = 0
    for i in title_link:
        with open('mp3/'+title+'/'+title_link[count][0]+'.mp3', 'wb') as a:
            url = title_link[count][1]
            text = requests.get(url=url).content
            a.write(text)
        count += 1


def main():
    links_titles = get_section_link_title()
    title_link = get_download_link(links_titles=links_titles)
    download_mp3(title_link=title_link)


if __name__ == '__main__':
    main()
