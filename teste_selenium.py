from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import cv2
import numpy as np

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
        

    def capturar_canvas(self,num):
        canvas = self.motor.find_element(By.ID, 'canvas')
        localizacao_canvas = canvas.location
        tamanho_canvas = canvas.size
        print_total = self.motor.get_screenshot_as_png()

        image = Image.open(BytesIO(print_total))

        left = localizacao_canvas['x']
        top = localizacao_canvas['y']
        right = localizacao_canvas['x'] + tamanho_canvas['width']
        bottom = localizacao_canvas['y'] + tamanho_canvas['height']

        image = image.crop((left, top, right, bottom))
        image.save('canvas{}.png'.format(num))


    @staticmethod
    def comparar_imagens():
        image1 = cv2.imread('canvas1.png')
        image2 = cv2.imread('canvas2.png')
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
            
        def mse(img1, img2):
            h, w = img1.shape
            diff = cv2.subtract(img1, img2)
            err = np.sum(diff**2)
            mse = err/(float(h*w))
            return mse     
        
        error = mse(image1, image2)
        return error


    def validar_canvas(self):
        for i in range(1,4):
            self.capturar_canvas(1)

            botao = self.motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[{}]'.format(i))
            botao.click()

            self.capturar_canvas(2)

            diferenca = self.comparar_imagens()

            if (diferenca > 0):
                print('Botao {} alterou o Canvas, portanto está funcionando.'.format(i))
            else:
                print('Botao {} não alterou o Canvas, portanto não está funcionando.'.format(i))


    def sair(self):
        self.motor.quit()