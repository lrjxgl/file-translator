'''
from lib.fanyihtml import html_fanyi

from lib.pdf2html import pdf_to_html
from lib.fanyidocx import docx_fanyi
'''
from lib.fanyitxt import txt_fanyi
'''
# 翻译html
fromFile="test/demo.html"
toFile="output/demo-zh.html"
con=html_fanyi(fromFile,toFile)
 

# 翻译pdf
pdfFile="test/demo.pdf"
fromFile="test/demo.html"
pdf2htmlEX = 'D:/program/pdf2htmlEX/pdf2htmlEX.exe'
#fromFile=pdf_to_html(pdfFile,"output",pdf2htmlEX)
fromFile="output/demo.pdf.html"
toFile="output/demo.pdf-zh.html"
con=html_fanyi(fromFile,toFile)
'''
'''
# 翻译docx
fromFile="test/demo.docx"
toFile="output/demo.docx-zh.docx"
docx_fanyi(fromFile,toFile)

'''
# 翻译txt
fromFile="test/demo.txt"
toFile="output/demo-zh.txt"
con=txt_fanyi(fromFile,toFile) 
print(con)

print("翻译完成")