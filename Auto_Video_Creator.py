#//*[@id="root"]/main/section/div[2]/article/div/div[1]/div[3]/div/div/div[1]
#/html/body/div[1]/main/section/div[2]/article/div/div[1]/div[3]/div/div/div[1]
#/html/body/div[1]/main/section/div[2]/article/div/div[1]/div[3]/div/div/div[1]

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# ChromeDriver'ı otomatik olarak indirip kur
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  # Selenium izlerini gizler
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")




caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

current_directory = os.path.join(os.getcwd(), "Videos")
prefs = {
    "download.default_directory": current_directory,  # Varsayılan indirme konumu
    "download.prompt_for_download": False,             # İndirme için onay sormayı devre dışı bırak
}
options.add_experimental_option("prefs", prefs)


def getlist():
    lst = (open("listofvideos.txt","r").read()).split("\n")
    return lst


class Auto_Download:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, desired_capabilities=caps,options=options)


        self.driver.execute_script("Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });")
        self.driver.execute_script("Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });")

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })

    def StartAndWait(self,lstofvideos):
        self.driver.get("https://www.veed.io/")
        while True:
            crturl = self.driver.current_url
            if "workspaces" in crturl:
                print("Loged In...")


                for sub in lstofvideos:
                    self.Create_Video(sub)
                break


    def ClickToXpath(self,xpaths,waittime = 5):
        x = 0
        while True:
            try:
                time.sleep(0.3)
                button = self.driver.find_element("xpath", xpaths)
                button.click()
                break
            except:
                print(x)
                x += 0.3
                if x >= waittime:
                    print(f"FIND ERROR : {xpaths}")
                    break
        try:
            return button.text
        except:
            print("Text ERROR")

    def Create_Video(self,subject):

        self.driver.get("https://www.veed.io/workspaces/805277a0-b739-492e-a878-0f8cac8b9934/home")

        self.ClickToXpath("//*[@id='root']/main/section/div[2]/article/div/div[1]/div[3]/div/div/div[1]")

        self.ClickToXpath("//*[@data-testid='@upload-modal/start_with_ai_card']")


        try:
            self.ClickToXpath("//*[@data-testid='@upload-modal/start-with-ai/input']")
            input_field = self.driver.find_element("xpath", "//*[@data-testid='@upload-modal/start-with-ai/input']")
            input_field.send_keys(subject)
            print(f"INPUT OK : {subject}")

        except:
            print("INPUT ERROR")



        self.ClickToXpath("//*[@data-testid='@upload-modal/start-with-ai/generate-button']") 
        time.sleep(5)

        while True:

            try:
                time.sleep(5)
                self.driver.find_element("xpath", "//*[@class='sc-fBluuK kPkugO']")
            except:
                time.sleep(5)
                print("### Video Ready ###")
                break

                


                #
        


        self.ClickToXpath("//*[@data-testid='@header-controls/publish-button']")

        self.ClickToXpath("//*[@data-testid='@export/export-button']")


        while True:

            try:
                time.sleep(5)
                self.driver.find_element("xpath", "//*[@class='sc-8b9b2c6f-4 hfVxhh']")
            except:
                time.sleep(5)

                break

                
        
        self.ClickToXpath("//*[@data-testid='@referral/rejectCTA']")

        time.sleep(5)

        action = ActionChains(self.driver)
        action.move_by_offset(1, 2).click().perform() 

        self.ClickToXpath("//*[@class='sc-63291f4c-1 ecmXwx']")

        self.ClickToXpath("/html/body/div[1]/div/div[2]/nav/button[2]")

        
        self.ClickToXpath("//*[@data-testid='MP4 download button']")


        #@header-controls/publish-button
        #@export/export-button
        #/html/body/div[1]/div/div[2]/nav/button[2]
        #MP4 download button

    def ext(self):
        self.driver.quit()

X = Auto_Download()
X.StartAndWait(getlist())
    
    