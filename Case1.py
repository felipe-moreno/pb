from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# logging.basicConfig(filename="log.txt", 
#                     format='%(asctime)s %(message)s', 
# 					filemode='a',
#                     level=logging.INFO)
# logger = logging.getLogger()

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/challenging_dom")

for i in range(1,4):
    botao = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
    id_botao = botao.get_attribute('id')
    # logger.info(botao.text)
    botao.click()
    botao = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
    id2_botao = botao.get_attribute('id')

    if (id_botao != id2_botao):
        print('Botao {} ok.'.format(i))
    else:
        print('Botao nao mudou.')

print('')

for i in range(1,11):
    table1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr[{}]/td[1]'.format(i))
    print(table1.text)
    if (table1.text[-1] == str(i-1)):
        print('Linha {}:'.format(i-1))
        for j in range(1,3):
            table2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td/a[{}]'.format(j))
            table2.click()
            if (j == 1):
                if (driver.current_url == 'https://the-internet.herokuapp.com/challenging_dom#edit'):
                    print('Edit {} ok.'.format(i-1))
                else:
                    print('Edit {} nao esta funcionando.'.format(i-1))
            else:
                if (driver.current_url == 'https://the-internet.herokuapp.com/challenging_dom#delete'):
                    print('Delete {} ok.'.format(i-1))
                else:
                    print('Delete {} nao esta funcionando.'.format(i-1))
    print('')

driver.quit()