# title:移除空白

def reblank(text):
    import re
    import copy

    s="移除空白函数类似下面这种"
    s= "Adasd ASD       1kld Uca     "
    s= r"Adasd ASD\n       1kld Uca     "
    s= "Adasd ASD" + r"\n" + "       1kld Uca     "
    s = "这是注释说明"

    if "\n" in text:
        return re.sub(r"\n.*?\S"," ",text,re.M)
    else:
        text = text.strip().split(" ")
        copy_text = copy.deepcopy(text)
        for t in copy_text:
            if not t:
                text.remove(t)
        return " ".join(text)
