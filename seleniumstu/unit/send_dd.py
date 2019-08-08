import requests
import json

"""发送基本的测试结果到钉钉机器人群"""
url = "https://oapi.dingtalk.com/robot/send?access_token=" \
      "9e7a53cbe9d627d80d5caa0f2566e9028fb81431e994582d115672e0b73cbaab"
headers = {'Content-Type': 'application/json;charset=utf-8'}


def message(text, mobile):
    text_info = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                mobile
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print(requests.post(url, json.dumps(text_info), headers=headers).content)  # 将返回的数据编码成 JSON 字符串


def send(text):
    message(str(text), '')
