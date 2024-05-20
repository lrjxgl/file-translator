# file-translator

Utilize AI large models or API to translate files, supporting both Chinese and English translations, as well as PDF, docx, txt, and html.

利用AI大模型或者api翻译文件，支持中英文翻译，支持pdf、docx、txt、html。

![](static/1.png)
![](static/index.png)

# 翻译模型 Translation model

The default model is the Qwen1.5-14B-Chat-GPTQ-Int4 model from Ali Qianwen. You can change the model in lib/fanyi_qianwen.py.

默认采用阿里千问Qwen1.5-14B-Chat-GPTQ-Int4模型.可以在lib/fanyi_qianwen.py更改模型。


也可以采用线上大模型接口

https://help.aliyun.com/zh/dashscope/developer-reference/api-details?spm=a2c4g.11186623.0.0.c9c946c10uY6YR

set DASHSCOPE_API_KEY="xxx"



# 安装方法

环境依赖

py310+pytorch 

https://pytorch.org/get-started/locally/ 

git clone https://github.com/lrjxgl/file-translator.git

cd file-translator

pip install -r requirements.txt

# 运行方法

python gradio_app.py

设置翻译引擎

python gradio_app.py --engine qianwen_online

# 资料参考

pdf翻译参考 https://github.com/SUSTYuxiao/PdfTranslator

