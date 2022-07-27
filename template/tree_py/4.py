# title:LP模板

try:
   a_1 = am.see("xpath",'xxx')[0]
   a_2 = am.see("xpath",'xxx')[0]
   e=random.choice([a_1])
   driver.execute_script("arguments[0].scrollIntoView(false);", e)
   am.click(e)

   if e == a_1:
       win_handles = driver.window_handles
       driver.switch_to.window(win_handles[-1])
except:
    pass
time.sleep(random.randint(10,15))