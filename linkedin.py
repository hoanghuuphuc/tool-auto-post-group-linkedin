from tokenize import group
import pyautogui
from selenium import webdriver
import pandas
import time
import pandas

from selenium.webdriver.common.by import By
tk="*********"
mk="*********"
excel_data_df = pandas.read_excel('linkedin.xlsx')
page=excel_data_df['Link'].tolist()
noi_dung=excel_data_df['NoiDung'].tolist()
hinhanh=excel_data_df['hinhanh'].tolist()
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
tai_khoan=driver.find_element("id","username").send_keys(tk)
time.sleep(2)
mat_khau=driver.find_element("id","password").send_keys(mk)
dang_nhap=driver.find_element("xpath","/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
for i in range(len(page)):
    try:
        gr=driver.get(page[i])
        time.sleep(2)
        click_dangbai=driver.find_element("xpath","/html/body/div[5]/div[3]/div/div[2]/div/div/main/div/div[4]/div/div[1]/button/span").click()
        time.sleep(2)
        pyautogui.write(noi_dung[i])
        time.sleep(5)
        hinh_anh=driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[1]/button").click()
        time.sleep(2)
        pyautogui.write(hinhanh[i])
        pyautogui.keyDown("enter")
        time.sleep(2)
        clickk=driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button").click()
        dang_bai=driver.find_element("xpath","/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button/span").click()
        time.sleep(3)
    except:
        thamgia=driver.find_element("xpath","/html/body/div[6]/div[3]/div/div[2]/div/div/main/div/div[1]/section/div/button").click()
    
