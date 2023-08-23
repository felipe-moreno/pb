from selenium import webdriver
from selenium.webdriver.common.by import By

class url():
    
    def __init__(self,endereco) -> None:
        self.motor = webdriver.Chrome()
        self.motor.get(endereco)
        

    def clicar_botoes(self):
        for i in range(1,4):
            botao = self.motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
            id_botao = botao.get_attribute('id')
            botao.click()
            botao = self.motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
            id2_botao = botao.get_attribute('id')

            if (id_botao != id2_botao):
                print('Botao {} ok.'.format(i))
            else:
                print('Botao nao mudou.')

    def clicar_edit_delete(self):
        for i in range(1,11):
            table1 = self.motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr[{}]/td[1]'.format(i))
            print(table1.text)
            if (table1.text[-1] == str(i-1)):
                print('Linha {}:'.format(i-1))
                for j in range(1,3):
                    table2 = self.motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/table/tbody/tr/td/a[{}]'.format(j))
                    table2.click()
                    if (j == 1):
                        if (self.motor.current_url == 'https://the-internet.herokuapp.com/challenging_dom#edit'):
                            print('Edit {} ok.'.format(i-1))
                        else:
                            print('Edit {} nao esta funcionando.'.format(i-1))
                    else:
                        if (self.motor.current_url == 'https://the-internet.herokuapp.com/challenging_dom#delete'):
                            print('Delete {} ok.'.format(i-1))
                        else:
                            print('Delete {} nao esta funcionando.'.format(i-1))
            print('')
        
    def sair(self):
        self.motor.quit()