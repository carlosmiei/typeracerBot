import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def play():
    driver = webdriver.Chrome("./chromedriver")
    #Opens typeracer
    driver.get("https://play.typeracer.com")
    time.sleep(5)
    
    #Entering a race
    root = driver.find_element_by_tag_name("html")
    root.send_keys(Keys.CONTROL,Keys.ALT,'i')

    # Finds the text
    time.sleep(3)
    text = driver.find_element_by_class_name("gameView").text
    text = text.split("\n")
    finalText = text[-3]
    
    #Injects the text on the input char by char
    time.sleep(10)
    myInput = driver.find_element_by_class_name("txtInput")
    for elem in finalText:
        myInput.send_keys(elem)
        time.sleep(0.01)
    
    # Waits a bit so you can contemplate the winning message :D
    time.sleep(20)
    print("Finished")
    driver.quit() 

if __name__ == "__main__":
    play()


    
    
    
    