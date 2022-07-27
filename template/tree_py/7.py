# title:基础循环点击模型

# 关闭新打开的网页,再返回原来的网页
def close_to_open_window(driver,index=1):
    all_handles = driver.window_handles
    if len(all_handles) > index:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

while True:
    try:
        els = am.see("xpath", '//button', timeout=7)
    except:
        break
    e = random.choice(els)
    driver.execute_script("arguments[0].scrollIntoView(true);", e)
    am.click(e)
    close_to_open_window(driver, 2)