from requests import get
import json
import sys


def Translation(s):
    j = json.loads(get("http://fanyi.youdao.com/translate?&doctype=json&i=" + s).text)
    return j['translateResult'][0][0]['tgt']

try:
    print("翻译后的结果:" + Translation(sys.argv[1]))
except:
    print("翻译后的结果:"+ Translation(input("请输入需要翻译的文字:")))
