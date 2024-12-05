from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome(executable_path="./chromedriver")

# Acessar a aplicação
driver.get("http://127.0.0.1:5000/")
assert "Task Manager" in driver.title

# Navegar para adicionar tarefa
driver.find_element(By.LINK_TEXT, "Add New Task").click()
time.sleep(2)

# Adicionar nova tarefa
input_field = driver.find_element(By.ID, "title")
input_field.send_keys("Learn Selenium")
input_field.send_keys(Keys.RETURN)
time.sleep(2)

# Verificar se a tarefa foi adicionada
assert "Learn Selenium" in driver.page_source

driver.quit()

