from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#___________________________________________
#/   import time
#/    from selenium.webdriver.support import expected_conditions as EC
#/  from selenium.webdriver.support.ui import WebDriverWait as wait
#/
#    driver.get("https://www.geeksforgeeks.org/")
#
#   time.sleep(3)
#   wait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(("gsc-i-id2")))
#___________________________________________
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
  
# get element 
element = driver.find_element_by_link_text("Courses")
  
# create action chain object
action = ActionChains(driver)
  
# click the item
action.click(on_element = element)
  
# perform the operation
action.perform()