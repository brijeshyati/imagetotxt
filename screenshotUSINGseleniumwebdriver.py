""""
this scipt access the web page using selenium python and take screeshot and save it at the particular path.
using size of file read the particular error messages and print it in log file
""""

# -*- coding: utf-8 -*-
import os
import sys
import time
from selenium import webdriver
import pandas as pd
from os import listdir
from os.path import isfile, join
from PIL import Image
from io import BytesIO

orig_stdout = sys.stdout
f = open('C:\\Users\\XXXXXXXXXX\\python_learning\\LOG\\filelist_test.log', 'w')
sys.stdout = f


def filelist():

	## reading the details from csv files
        data = pd.read_csv("C:/Users/XXXXXXXXXX/python_learning/filelistdetails.csv",sep=',')
        data.headername


        # get the path of ChromeDriverServer , keep chromedriver and script in same folder.
        dir = os.path.dirname(__file__)
        print(dir)
        chrome_driver_path = dir + "\chromedriver.exe"        
        # create a new Chrome session
        driver = webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.get("http://google.com:8080/n.o-14.2/login.jsp")
        driver.find_element_by_id("loginName").send_keys("username")
        driver.find_element_by_id("password").send_keys("password")
        driver.find_element_by_xpath('//*[@id="gwt-debug-Login-button"]').click()        
        print("after login in FS=",driver.current_url)

        count=0
        
        for opt in data.headername:
                
                    AA=len(data.headername)
                    count +=1
                    #print("filenu:",opt,count,"\\",AA)
                    print("===================== LOGIN",opt,count,"\\",AA,"=============================================")
                    url ="http://google.com:8080/n.o-14.2/integration/view/?preId=119904&maObe=" + str(opt)
                    print("current url:", url)
                    driver.get(url)
                    time.sleep(5)
                    #print("Report folder path first=",driver.current_url)
                    #driver.set_window_size(480, 320)
                    #driver.set_window_size(1024, 768)
                    driver.set_window_size(1080,800)
                    #driver.set_window_size(1366, 728) # optional
                    
                    scrname ="C:/Users/XXXXXXXXXX/python_learning/pic/1/" + str(opt) + ".png"
                    #driver.save_screenshot(scrname)
                    print ("Executed Succesfull")
                    
                    screen = driver.get_screenshot_as_png()
                    # Crop it back to the window size (it may be taller)
                    #box = (0, 0, 1366, 728)
                    box = (0, 0, 480, 320)
                    #im = Image.open(StringIO.StringIO(screen))
                    #Image.open('old.jpeg').convert('RGB').save('new.jpeg')
                    im = Image.open(BytesIO(screen)).convert('RGB')
                    region = im.crop(box)
                    region.save(scrname, 'PNG', optimize=True, quality=95)
                    #print("===================== LOGOUT",count,"\\",AA,"=============================================")
		driver.close()
        driver.quit() 
        
def filesize():
    mypath ="C:/Users/XXXXXXXXXX/python_learning/pic/1/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print("=================================================================")
    for opt in onlyfiles:
        ff =mypath + opt
        fsize=os.stat(ff)
        #print('size:' + fsize.st_size.__str__())
        if fsize.st_size <= 7085:     
            print(opt.strip('.png'),fsize.st_size,"failed",sep=',')
        else:
            print(opt.strip('.png'),fsize.st_size,"working",sep=',')


if __name__ == "__main__":
    filelist()
    filesize()
sys.stdout = orig_stdout
f.close()  
