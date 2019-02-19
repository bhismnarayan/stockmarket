import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support import expected_conditions as EC
import time
def downloadFile():
      options = Options()
    #  options.add_argument('--headless')
     # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
      options.add_experimental_option("prefs", {
     "download.default_directory": "C:\\Users\\Bhism\\downloads\\sanjay",
      "download.prompt_for_download": True,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
      })
      driver = webdriver.Chrome('C:\\Users\\Bhism\\Downloads\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
      driver.get("https://www.indiabondinfo.nsdl.com/bds-web/jsps/home/download.jsp#")
      driver.set_page_load_timeout(3000)
      downloadlink = driver.find_element_by_class_name('report-link')
      downloadlink.click()
      filetype=driver.find_element_by_xpath('//*[@id="rows"]/tbody/tr[5]/td[2]/select/option[4]')
      filetype.click()
      downloadbutton=driver.find_element_by_xpath('//*[@id="downloadReport"]')
      downloadbutton.click()


def downloadFileBhavCopy():
      options = Options()
      options.add_argument('--headless')
      options.add_argument('--disable-gpu')  # Last I checked this was necessary.
      options.add_experimental_option("prefs", {
    # "download.default_directory": "C:\\Users\\Bhism\\downloads\\sanjay",
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing.enabled": True
      })
      driver = webdriver.Chrome('C:\\Users\\Bhism\\Downloads\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
      driver.get("https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm")
      driver.set_page_load_timeout(3000)
      #downloadlink = driver.find_element_by_class_name('report-link')
      #downloadlink.click()
      filetype=driver.find_element_by_xpath('//*[@id="h_filetype"]/option[2]')
      filetype.click()
      datefield=driver.find_element_by_xpath('//*[@id="date"]')
      datefield.send_keys('15-02-2019')
      datefield.send_keys(Keys.TAB);
      downloadbutton=driver.find_element_by_xpath('//*[@id="wrapper_btm"]/div[1]/div[4]/div/div[1]/div/div[4]/input[3]')
      downloadbutton.click()
      driver.implicitly_wait(10) # seconds
      #wait = WebDriverWait(driver, 10)
      downloadfile=driver.find_element_by_xpath('//*[@id="spanDisplayBox"]/table/tbody/tr/td/a')
      downloadfile.click()
      driver.implicitly_wait(10000) 
      time.sleep(60)
downloadFileBhavCopy()