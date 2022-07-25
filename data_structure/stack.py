# -*- coding:utf-8 -*-
# @time:2022/7/2311:48
# @author:LX
# @file:stack.py
# @software:PyCharm
'''
    列表实现堆栈
'''


class StructData:
    def __init__(self,*args):
        self.setData(*args)

    # 无法修改属性的值，只能通过方法修改属性的值
    def setData(self, id: int, number: str, task: str, view, count: int, schedule,
                create_time: str, update_time: str, participator, history):
        self.__id = id
        self.__number = number
        self.__task = task
        self.__view = view
        self.__count = count
        self.__schedule = schedule
        self.__create_time = create_time
        self.__update_time = update_time
        self.__participator = participator
        self.__history = history
        self.__data = self.structData(self.__id, self.__number, self.__task, self.__view, self.__count, self.__schedule,
                                    self.__create_time, self.__update_time, self.__participator, self.__history)
        return self.__data

    def __str__(self):
        return str(self.__data)

    # 返回属性的值
    def getKeyobj(self, key: str):
        return self.__data[key]

    def getNumber(self):
        return self.__number

    def getTask(self):
        return self.__task

    def getView(self):
        return self.__view

    def getCount(self):
        return self.__count

    def getSchedule(self):
        return self.__schedule

    def getCreateTime(self):
        return self.__create_time

    def getUpdateTime(self):
        return self.__update_time

    def getParticipator(self):
        return self.__participator

    def getHistory(self):
        return self.__history

    def getID(self):
        return self.__id

    def getData(self)->dict:
        return self.__data

    def dataToList(self)->list:
        return list(self.__data.values())

    # 构建数据
    def structData(self, id: int, number: str, task: str, view, count: int, schedule,
                   create_time: str, update_time: str, participator, history):
        # 组成字典
        data = {
            "id": id,
            "number": number,
            "task": task,
            "view": view,
            "count": count,
            "schedule": schedule,
            "create_time": create_time,
            "update_time": update_time,
            "participator": participator,
            "history": history
        }
        return data


class Stack:
    def __init__(self):
        self.s = StructData(0, "", "", "", 1, "", "2021.1.21 10:30", "2021.1.21 10:31", "刘璇", "")
        self.items = []

    def isEmpty(self)->bool:
        return self.items == []

    def push(self, *args):
        self.items.append(StructData(*args))

    def pop(self) -> StructData:
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()
# s.push(1,2,3,4,5,6,7,8,9,10)
# s.push(11,12,13,14,15,16,17,18,19,20)
print(s.items)
# print(s.pop())

