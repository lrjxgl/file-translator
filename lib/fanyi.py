import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
import  fanyi_qianwen
def fanyi(text):
    return fanyi_qianwen.fanyi(text)

