import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
from fanyi import fanyi
def txt_fanyi(fromFile,toFile):
    with open(fromFile, 'r', encoding='utf-8') as f:
            content = f.read()
            fanyi_content=fanyi(content)
    with open(toFile, 'w', encoding='utf-8') as f:
          f.write(fanyi_content)
    return fanyi_content
