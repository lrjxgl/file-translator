import os
from lib.fanyihtml import html_fanyi
from lib.pdf2html import pdf_to_html
from lib.fanyidocx import docx_fanyi
from lib.fanyitxt import txt_fanyi
from lib.pdf2docx import pdf_docx
import time
import gradio as gr
import mammoth

def replace_whitespace_with_html(s):
    # 将空格替换为&nbsp;
    s = s.replace(' ', '&nbsp;')
    # 将换行符(\n)替换为<br>以在HTML中实现换行
    s = s.replace('\n', '<br>')
    return s


def infer(input_file):
    _, extension = os.path.splitext(input_file)
    # 移除点字符
    file_type=extension[1:]
    fromFile=input_file
    doc_file="output/"+str(time.time())+".docx"      
    doc_file_zh="output/"+str(time.time())+"-zh.docx" 
    if file_type=='pdf':
        pdf_file=input_file  
        pdf_docx(pdf_file,doc_file)        
        docx_fanyi(doc_file,doc_file_zh)

    if file_type=='html':
        toFile="output/"+str(time.time())+"-zh.html"
        html_fanyi(input_file,toFile)
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(toFile, 'r', encoding='utf-8') as f:
            fanyi_content = f.read()   
        return content,fanyi_content,toFile 
    elif file_type=='docx':
        doc_file=input_file
        docx_fanyi(input_file,doc_file_zh)
    elif file_type=='doc':
        doc_file=input_file
        docx_docx(input_file,doc_file) 
        docx_fanyi(doc_file,doc_file_zh)
    elif file_type=='txt':
        
        toFile="output/"+str(time.time())+"-zh.txt"
        fanyi_content=txt_fanyi(fromFile,toFile) 
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        content=replace_whitespace_with_html(content)
        fanyi_content=replace_whitespace_with_html(fanyi_content)
        return content,fanyi_content,toFile
    
    print("翻译完成") 
    fanyi_content=""
    content=""
    if file_type=='docx' or file_type=='pdf':
        with open(doc_file, 'rb') as docx_fd:
            result = mammoth.convert_to_html(docx_fd)
            content = result.value
        with open(doc_file_zh, 'rb') as docx_fd:
            result = mammoth.convert_to_html(docx_fd)
            fanyi_content = result.value
        return content,fanyi_content,doc_file_zh

with gr.Blocks(title="文档翻译") as demo:
    gr.Label("文件翻译",container=None)
    up=gr.File( label="PDF文件")
    
    
    with gr.Row():
        html1=gr.HTML()
        html2=gr.HTML()
    outfile=gr.File(label="下载生成的文本文件")
    submit=gr.Button("提交")
    submit.click(infer,inputs=[up],outputs=[html1,html2,outfile])
 
demo.launch()
