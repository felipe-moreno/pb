from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(filename="log.txt", 
                    format='%(asctime)s %(message)s', 
					filemode='a',
                    level=logging.INFO)
logger = logging.getLogger()

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/challenging_dom")

for i in range(1,4):
    botao = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
    logger.info(botao.text)
    botao.click

table = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td/a')

for element in table:
    logger.info(element.text)
    element.click

logger.info('\n')

driver.quit()