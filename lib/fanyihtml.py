from bs4 import BeautifulSoup
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
from fanyi import fanyi

# 定义一个递归函数来打印文档树
def parse_html_tree(element, indent=0):
    # 打印当前元素的名称和属性（如果有的话）
    #print("  " * indent + element.name)
    # 打印当前元素的文本内容（如果有的话）
    if element.string:
        if element.name not in ['script', 'style']:
            element.string=fanyi(element.get_text(strip=True))
        #print("  " * (indent + 1) + "Text: " + element.get_text(strip=True))
    # 遍历子元素并递归调用此函数
    for child in element.children:
        if child.name  in ['script', 'style']:
            continue
        if child.name:  # 确保只处理标签元素，忽略NavigableString等类型
            #child.string=fanyi(element.get_text(strip=True))   
            parse_html_tree(child, indent + 1)
        elif child.string:
            print(child.string)
              

def html_fix(soup):
    # 查找所有的div标签
    div_tags = soup.find_all()
    
    for div in div_tags:
        if div.name in   ['script', 'style','title','head','meta']:
            continue
        # 找到div中的所有子节点
        children = div.contents
        
        # 遍历子节点，寻找直接文本并包裹进新的<span>标签
        new_children = []
        buffer = ""  # 用于累积连续的直接文本
        
        for child in children:
            if child.name in   ['script', 'style','title','head','meta']:
                continue
            if isinstance(child, str):  # 如果是直接文本
                buffer += child.strip()  # 累积文本并去除两边空白
            else:  # 如果是标签
                # 如果累积的buffer不为空，则先包裹buffer中的文本到新的<span>
                if buffer:
                    new_children.append(soup.new_tag('span'))
                    new_children[-1].string = buffer
                    buffer = ""  # 重置buffer
                # 添加当前标签到新子节点列表
                new_children.append(child)
        
        # 处理最后一个累积的文本（如果有的话）
        if buffer:
            new_children.append(soup.new_tag('span'))
            new_children[-1].string = buffer
        
        # 用处理后的新子节点替换原div中的内容
        div.clear()
        for new_child in new_children:
            div.append(new_child)
    return str(soup.prettify())
def remove_nested_spans(soup):
    for span in soup.find_all('span'):
        if span.name == 'span' and span.parent.name == 'span':
            if span.has_attr("class"):
                span.parent["class"]=span["class"]
            span.parent.string = span.string
            span.extract()
    return soup 
def html_fanyi(fromFile,toFile):
    html=open(fromFile,'r',encoding='utf-8')
    soup = BeautifulSoup(html, 'lxml')
    html_fix(soup)
    remove_nested_spans(soup)
    #soup = BeautifulSoup(html, 'lxml')
    parse_html_tree(soup)
    con=str(soup.prettify())
    #保存翻译后的html文件
    open(toFile,'w',encoding='utf-8').write(con)
    return con