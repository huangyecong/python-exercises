# Python自动获取小说工具

# ----------------------------------1、怎么发送请求----------------------------------
# pip install requests （可以使用pip list查看是否成功安装，如果requests显示在list，便是成功安装）
import requests

# pip install lxml (主要用来去除html标签)
from lxml import etree

# ----------------------------------2、发送给谁----------------------------------
url = 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/1.html'

# 计数器，用于限制爬取5个章节
chapter_count = 0
max_chapters = 5

# 进入循环
# while True:  # 注意此处是 True 而不是 true
while chapter_count < max_chapters:  # 控制循环次数为5次

    # 伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }

    # ----------------------------------3、发送请求----------------------------------
    resp = requests.get(url, headers=headers)
    # 设置编码
    resp.encoding = 'utf-8'

    # ----------------------------------4、响应信息----------------------------------
    # XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。
    # //:代表寻找所有（如：//div,找到的是就是页面所有的div标签）

    e = etree.HTML(resp.text)
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))
    title = e.xpath('//h1/text()')[0]
    # 更新url为页面上的链接地址
    url = f'https://dldl1.nsbuket.cc{e.xpath("//tr/td[2]/a/@href")[0]}'

    # ----------------------------------5、保存----------------------------------
    #  使用 'a' 模式追加章节内容
    # 'w'模式：表示写入,你使用了 'w' 模式来打开文件，它会在每次循环时覆盖文件内容。
    # 'a' 模式（append）：，这里应该使用'a' 模式，而不是 'w' 模式。'a' 模式会将新内容追加到文件末尾，而不会覆盖现有内容
    with open('./斗罗大陆.txt', 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')

    # 计数器加1
    chapter_count += 1

    # 输出当前爬取的章节
    print(f"爬取了 {chapter_count} 章节: {title}")

    # 输出完成提示
    print("已爬取完5个章节，内容已保存到 '斗罗大陆.txt'")

  # 为了避免死循环，在获取完内容后break退出循环
    # if url == '/xiaoshuo/douluodalu/':
    #     break
