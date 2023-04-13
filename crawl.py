from bs4 import BeautifulSoup
import os
import pyhttpx

def wget_test():
    import os
    out_image = 'out_005.png'
    url = 'http://mangadoom.co/wp-content/manga/5170/886/005.png'
    os.system("wget -O {0} {1}".format(out_image, url))

def req_test():
    import shutil
    # import requests
    from curl_cffi import requests

    # 定义存储路径
    text_path = "text/"
    image_path = "image/"
    table_path = "table/"

    # 创建存储路径
    os.makedirs(text_path, exist_ok=True)
    os.makedirs(image_path, exist_ok=True)
    os.makedirs(table_path, exist_ok=True)

    # 发送HTTP请求并解析网页内容
    url = "https://www.sec.gov/Archives/edgar/data/1445305/000144530522000041/wk-20211231.htm"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    session = pyhttpx.HttpSession()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # 存储文本内容
    with open(text_path + "req_test_content.txt", "w", encoding="utf-8") as f:
        f.write(soup.get_text())

    # 存储图片内容
    for i,img in enumerate(soup.find_all("img")):
        img_url = img.get("src")
        img_url = 'https://www.sec.gov/Archives/edgar/data/1445305/000144530522000041/'+img_url
        # img_url = 'https://img-blog.csdnimg.cn/0ec717a4284340c7b68ab8a4d689d96d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAT2hfUHl0aG9u,size_20,color_FFFFFF,t_70,g_se,x_16'

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(image_path + f'req_test_img_{i}.jpg', "wb") as f:
                f.write(img_response.content)
                # img_response.raw.decode_content = True
                # shutil.copyfileobj(img_response.raw, f)
        else:
            print('fail to get img! eeror code:', img_response.status_code)

    # 存储表格内容
    for table in soup.find_all("table"):
        with open(table_path + "table.html", "w", encoding="utf-8") as f:
            f.write(str(table))

def sele_test():
    from selenium import webdriver
    import urllib.request
    from urllib import request
    import os
    import time
    from bs4 import BeautifulSoup
    import random
    from PIL import Image

    # 创建文件夹用于存储文本、图像和表格内容
    if not os.path.exists('text'):
        os.makedirs('text')
    if not os.path.exists('image'):
        os.makedirs('image')
    if not os.path.exists('table'):
        os.makedirs('table')

    # 创建Chrome浏览器实例并访问页面
    driver = webdriver.Chrome()
    url = 'https://www.sec.gov/Archives/edgar/data/1445305/000144530522000041/wk-20211231.htm'
    driver.get(url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    # 获取网页内容
    page_source = driver.page_source

    # 存储文本内容
    with open('text/page_content.txt', mode='w', encoding='utf-8') as f:
        f.write(page_source)

    # 存储图像内容

    #eeeeeeeeeeee-as
    # opener = urllib.request.build_opener()
    # ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    #        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    #        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
    #        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
    #        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
    #        ]
    # opener.addheaders = [('User-Agent', random.choice(ua_list))]
    # urllib.request.install_opener(opener)

    soup = BeautifulSoup(page_source, 'html.parser')
    img_tags = soup.find_all('img')
    for i, img in enumerate(img_tags):
        img_src = 'https://www.sec.gov/Archives/edgar/data/1445305/000144530522000041/'+img.get('src')
        # img_src = 'https://img-blog.csdnimg.cn/0ec717a4284340c7b68ab8a4d689d96d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAT2hfUHl0aG9u,size_20,color_FFFFFF,t_70,g_se,x_16'
        img_name = img_src.split('/')[-1]

        #eeeeeeeeeeee
        urllib.request.urlretrieve(img_src, f'image/_ee_{i}_.jpg')

        #eeeeeeeeeeee
        # try:
        #     req = request.Request(img_src, headers=headers)
        #     data = request.urlopen(req).read() #error
        #     with open('image/_ee_{img_name}', 'wb') as f:
        #         f.write(data)
        #         f.close()
        # except Exception as e:
        #     print(str(e))

        #eeeeeeeeeeeee
        # response = requests.get(img_src)
        # # 检查响应状态码
        # if response.status_code == 200:
        #     # 获取图片内容
        #     content = response.content
        #     # 使用Pillow库读取图片
        #     # image = Image.open(BytesIO(content))
        #     # 保存图片到本地
        #     with open('image.jpg', 'wb') as f:
        #         f.write(content)
        #         print('图片保存成功！')
        # else:
        #     print('请求图片失败，状态码：', response.status_code)

    # 存储表格内容
    tables = soup.find_all('table')
    for i, table in enumerate(tables):
        with open(f'table/table_{i}.html', mode='w', encoding='utf-8') as f:
            f.write(str(table))

    # 关闭浏览器
    driver.quit()

def main():
    # sele_test()
    # req_test()
    wget_test()

main()
