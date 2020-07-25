# Dpendencies 
###################################################
#1. Selenium
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

#2. bs4 for Beautifull Soup
from bs4 import  BeautifulSoup
import requests

#3. json for conversion of data into json
import json

#4. Calculating execution time
import datetime
#####################################################
execution_starts=datetime.datetime.now()




#Chrome driver setup 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
 options.add_argument('--headless')     # Making the script headless


# Update path of webdriver that matches with current installed chrome version
# example : driver = webdriver.Chrome("C:/Vaibhaw/Project/scrapping/cbse/chromedriver.exe", options=options)
driver = webdriver.Chrome("__Path__of__webdriver__", options=options)


# Selecting regiion from dropdown
m=['M','G','A','C','D','R','P','B','T','U','K','L','N','E','H','W']
Regionals=['Chennai','Guwahati','Ajmer','chandigarh','Delhi','prayagraj','Patna','Bhubaneswar','Trivendram','Dehradun','BANGALURU','Bhopal','Noida','PUNE','PANCHKULA','DELHI WEST']



#temprorary Data 
affilation_record={}
affilation_record['Affilation_No']=[]

zones=0


# Iterating through each DropDown
for i in m:
    
    #Loading and storing up the session
    driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")

    # Selecting region radioButton
    Region_wise = driver.find_elements_by_css_selector("input[type='radio'][value='Region Wise']")[0].click()
    
    # Selecting Region
    time.sleep(1)
    select = Select(driver.find_element_by_id("ddlitem"))
    select.select_by_value(i)   # Region selected
    
    print("------------------------------",Regionals[zones],' Zone '," ---------------------------------- ")

    # Searching data for each zone
    search=driver.find_element_by_id('search')
    search.click()

    # Loading data
    time.sleep(1)
    
    # Couting total nos of schools
    pages=int(driver.find_element_by_id('tot').text)
    
    
    # Iterating to each page of selected region
    while pages>0:
        try:
            
            # Scrolling dow to get the next Button
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next=driver.find_element_by_id('Button1')
            next.click()
            print(Regionals[zones], " -->  "," Pages left ::  ",pages//25)
            pages-=25


        #     -------------------------------Scrapping Affilation number -------------------------------
            
            res=driver.execute_script("return document.documentElement.outerHTML")
            soup=BeautifulSoup(res,'lxml')
            box=soup.find('table',{'id':'T1'})
            all_schools=box.find_all('td',{'class':'repItem'})

            #filtering and storing afilation no. locally 
            for i in all_schools:
                affilation_data=list(map(str,(i.text).split(' ')))

                if 'Affiliation' in affilation_data:
                    affilation_record['Affilation_No'].append(affilation_data[1].split('.')[1])
#                    print('Affilation number : ',affilation_data[1].split('.')[1])      # to print extracting data    



        except Exception as err:
            print(err)
            break

    print("Completed ")
    zones+=1
    print()

#     Dumping data into JSON file

with  open('Affilation_number.json','w') as output:
    json.dump(affilation_record,output)


execution_end=datetime.datetime.now()

print("Total time taken  : ",execution_end-execution_starts)



# Cheking fetched data
#
# with open('Affilation_number.json') as json_file:
#     data = json.load(json_file)
#     for p in data['Affilation_No']:
#         print(p)


