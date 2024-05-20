import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 
import argparse
parser = argparse.ArgumentParser()

parser.add_argument(
        "-e",
        "--engine",
        type=str,
        required=False,
        default="qianwen",
        help="翻译引擎",
    )
args = parser.parse_args()
# 获取命令行 输入参数 fanyiEngine


print(args.engine)

if args.engine=='opus':
    import lib.fanyi_opus  as fyEngine
    print("使用opus")
elif args.engine=='qianwen_online':
    import  lib.fanyi_qianwen_online  as fyEngine
    print("使用qianwen online")
else:
    import lib.fanyi_qianwen as fyEngine
    print("使用qianwen")
def fanyi(text):
    return fyEngine.fanyi(text)

