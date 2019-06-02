from selenium import webdriver as wb

driver = wb.Firefox("C:\\Users\\raj.thootkuri\\Desktop\\pranam_apr18")

driver.get("http://www.facebook.com")
driver.pade_load_timeout(30)
driver.maximize_window()
driver.implicit_wait(20)
driver.get_screenshot_as_file("facebook.png")
driver.quit()