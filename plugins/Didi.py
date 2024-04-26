# -*- coding: utf-8-*-
# 插件的基类 robot.sdk.AbstractPlugin 引入
import requests

from robot.sdk.AbstractPlugin import AbstractPlugin


class Plugin(AbstractPlugin):
    # handle() 用于执行处理
    def handle(self, text, parsed):
        self.say('好的，我来帮你打车，您要去哪里？')

        response = requests.get("http://localhost:9090/control?name=didi&action=start&text=")
        if response != 'true':
            self.say(f"打车功能出现了一些问题呢。")
            return

            # 询问出发地点
        word = self.activeListen()  # 用于连续对话
        if "取消打车" in word:
            self.say("好的。取消打车")
            return
        else:
            # 根据word解析出地址
            self.say(f"请确认，是否现在打车去{word}")
            check = self.activeListen()
            if "确认" in check:
                self.say("好的。正在帮您打车，请耐心等待！")
                # 具体打车操作。。。
                response = requests.get(f"http://localhost:9090/control?name=didi&action=search&text={word}")
                num = response.text
                if num != '':
                    self.say(f"已经帮您打到车了，车牌号是{num}")
                    return
            else:
                self.say(f"已取消打车。")

    # isValid() 用于判断用户的指令是否适合交给这个插件处理
    def isValid(self, text, parsed):
        return "打车" in text or "打个车" in text
