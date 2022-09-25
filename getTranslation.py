from requests import get
import json


def Translation(s):
    j = json.loads(get("http://fanyi.youdao.com/translate?&doctype=json&i="+s).text)
    result = j['translateResult'][0][0]['tgt']
    return result

print("翻译后的结果:"+Translation(input("请输入需要翻译的文字:")))
