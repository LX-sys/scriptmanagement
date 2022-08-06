# -*- coding:utf-8 -*-
# @time:2022/8/416:40
# @author:LX
# @file:js_path.py
# @software:PyCharm

# from core.card import Card

from core.utility import copy,compare_path

class Card:
    def __init__(self,number,jspath):
        self.__test={"number":number,"jspath":jspath}

    def number(self):
        return self.__test["number"]

    def jspath(self):
        return self.__test["jspath"]

# 脚本路径
class JSPath:
    def __init__(self):
        # 统计脚本路径
        '''
        {
        # 卡片编号:脚本路径,共享路径卡片编号
        "1":{"path":"xxx","number":["1","2"]},
        }
        '''
        self.___script_path = dict()

    def scriptPathAll(self)->dict:
        return self.___script_path

    # 判断编号是否存在
    def is_number(self,number:str):
        if number in self.scriptPathAll():
            return True

        for n in self.scriptPathAll():
            if number in self.scriptPathAll()[n]["number"]:
                return True

        return False

    # 判断路径是否存在
    def is_jspath(self,jspath:str):
        for number in self.scriptPathAll():
            if compare_path(self.scriptPathAll()[number]["path"],jspath):
                return True
        return False

    # 获取路径对应的最外层卡片编号
    def getPathID(self,jspath):
        for number in self.scriptPathAll():
            if compare_path(self.scriptPathAll()[number]["path"],jspath):
                return number
        return None

    # 添加脚本路径
    def addJSPath(self,card:Card):
        if self.is_number(card.number()):
            print("编号重复")
            return

        if not self.is_jspath(card.jspath()):
            self.___script_path[card.number()] = {"path":card.jspath(),"number":[card.number()]}
        else:
            self.___script_path[self.getPathID(card.jspath())]["number"].append(card.number())

    # 根据脚本路径获取卡片编号列表
    def getNumberList(self,jspath:str):
        number_list = []
        for number in self.scriptPathAll():
            if compare_path(self.scriptPathAll()[number]["path"],jspath):
                number_list.extend(self.scriptPathAll()[number]["number"])
        return number_list

    # 判断某个编号对应的路径是否唯一
    def isOnly(self,jspath:str):
        if len(self.getNumberList(jspath)) == 1:
            return True
        return False

    # 删除脚本路径编号
    def removeNumber(self,number:str):
        if not self.is_number(number):
            return

        # 先判断编号是否为最外层主主编号
        if number in self.scriptPathAll():
            if len(self.scriptPathAll()[number]["number"]) == 1:
                del self.___script_path[number]
                return
            else:
                # 获取次级ID列表
                secondary_number = self.___script_path[number]["number"][1:]
                # 路径
                jspath = self.___script_path[number]["path"]
                # 删除编号
                del self.___script_path[number]
                # 次级编号1号位,添加到最外层
                self.___script_path[secondary_number[0]]=dict()
                self.___script_path[secondary_number[0]]["path"] = jspath
                self.___script_path[secondary_number[0]]["number"]=secondary_number
        else:
            tmep_number = ""
            for n in self.scriptPathAll():
                if number in self.scriptPathAll()[n]["number"]:
                    tmep_number = n
                    break
            if tmep_number:
                self.___script_path[tmep_number]["number"].remove(number)

    # 修改路径
    def updateJSPath(self,number:str,jspath:str):
        if not self.is_number(number):
            return

        self.removeNumber(number)

        # 先判断编号是否为最外层主主编号
        if self.is_jspath(jspath):
            w_number = self.getPathID(jspath)
            self.___script_path[w_number]["number"].append(number)
        else:
            # 不存在
            print("--")
            self.___script_path[number] = {"path":jspath,"number":[number]}

    # 修改编号
    def updateNumber(self,old_number:str,new_number:str):
        if not self.is_number(old_number):
            return

        if self.is_number(new_number):
            print("编号重复")
            return
        else:
            # 先判断这个编号是否在最外层
            if old_number in self.scriptPathAll():
                temp_copy = copy.deepcopy(self.scriptPathAll()[old_number])
                del self.___script_path[old_number]
                self.___script_path[new_number]=temp_copy
                self.___script_path[new_number]["number"].insert(0,new_number)
            else: # 内层
                for wn in self.scriptPathAll():
                    if old_number in self.scriptPathAll()[wn]["number"]:
                        index = self.___script_path[wn]["number"].index(old_number)
                        self.___script_path[wn]["number"][index] = new_number
                        break
            self.removeNumber(old_number)

if __name__ == '__main__':
    #  测试
    js_path = JSPath()
    js_path.addJSPath(Card("1","xxx"))
    js_path.addJSPath(Card("2","xxx"))
    js_path.addJSPath(Card("3","xxx"))
    js_path.updateNumber("1","5")
    # js_path.removeNumber("1")
    print(js_path.scriptPathAll())
    # print(js_path.getNumberList("xxx"))
