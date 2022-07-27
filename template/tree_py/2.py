# title:获取当前年龄

def getAge():
    from datetime import datetime as dt
    Birth = Year_Of_Birth + "-" + Month_Of_Birth.zfill(2) + "-" + Day_Of_Birth.zfill(2)
    return (dt.now()-dt.strptime(Birth,"%Y-%m-%d")).days//365