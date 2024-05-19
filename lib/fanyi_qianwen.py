import re
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto
 
dir="Qwen/Qwen1.5-14B-Chat-GPTQ-Int4"
model = AutoModelForCausalLM.from_pretrained(
    dir,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(dir)
def chat(messages):
    
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=20480
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return response
    
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
    try:
        messages=[]
        messages.append({"role": "user", "content": "现在请当作一个英语翻译助手，我输入的英文你翻译成中文，我输入中文你翻译成英文，只返回翻译后的文字。内容："+prompt})
        # messages.append({"role": "assistant", "content": "好的"})
        # messages.append({"role": "user", "content": prompt})
        content=chat(messages)
        print("结果",content)
    except:
        content=prompt
    return content    
