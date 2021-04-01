import time
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

driver.get("https://play.typeracer.com")
time.sleep(10)

pyautogui.hotkey('ctrl','alt','i')
time.sleep(8)

text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")

myInput = driver.find_element_by_class_name("txtInput")

finalText = text[-3]

n = 12 # chunk length
chunks = [finalText[i:i+n] for i in range(0, len(finalText), n)]

print("Chunked String", chunks)
print("Going to sleep")
time.sleep(10)
print("Finished")

for elem in finalText:
    myInput.send_keys(elem)
    time.sleep(0.01)

print("Going to sleep")
time.sleep(20)
print("Finished")
driver.quit()