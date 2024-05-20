import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch.cuda as cuda
dir="Helsinki-NLP/opus-mt-en-zh"
tokenizer_en2zh = AutoTokenizer.from_pretrained(dir)
model_en2zh = AutoModelForSeq2SeqLM.from_pretrained(dir)
def en2zh(text):
    print("翻译",text)
    try:
        tokenized_text = tokenizer_en2zh([text], return_tensors='pt')
        translation = model_en2zh.generate(**tokenized_text, max_new_tokens=1024)
        cuda.empty_cache()
        con= tokenizer_en2zh.batch_decode(translation, skip_special_tokens=True)[0]
        print("结果",con)
    except:
        con=text
    return con



def fanyi(text):
    if not  re.search(r'[a-zA-Z]', text):
        print(text)
        return text
    
    # 按行翻译
    lines = text.split("\n")
    content=""
    for i in range(len(lines)):
        line=lines[i]
        if(len(line)>200):
            arr2=line.split(".")
            for j in range(len(arr2)):
                s2=arr2[j].strip()
                if re.search(r'[a-zA-Z]', s2)==False:
                    continue
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
  

 