import random
from http import HTTPStatus
from dashscope import Generation  # 建议dashscope SDK 的版本 >= 1.14.0

def fanyi(text):
  
    # 按行翻译
    lines = text.split("\n")
    content=""
    for i in range(len(lines)):
        line=lines[i]
        if(len(line)>200):
            arr2=line.split(".")
            for j in range(len(arr2)):
                s2=arr2[j].strip()
                 
                if len(s2)<=2:
                    content=content+s2+"\n"
                else:   
                    s=en2zh(s2) 
                    content=content+s+"." 
        else:
            if len(line.strip())<=2:
                content=content+line+"\n"
            else:
                s=en2zh(line)
                content=content+s+"\n" 
         
    return content
def en2zh(prompt):
    print("翻译",prompt)
    messages=[]
    messages.append({"role": "user", "content": "现在请当作一个英语翻译助手，我输入的英文你翻译成中文，我输入中文你翻译成英文，只返回翻译后的文字。内容："+prompt})
    response = Generation.call(model="qwen-turbo",
                               messages=messages,
                               # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
                               seed=random.randint(1, 10000),
                               # 将输出设置为"message"格式
                               result_format='message')
    if response.status_code == HTTPStatus.OK:
        content=response["output"]["choices"][0]["message"]["content"]
        print("结果",content)
        return content
    else:
         return prompt