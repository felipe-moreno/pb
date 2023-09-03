from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
import cv2
import numpy as np

motor = webdriver.Chrome()
motor.get('https://the-internet.herokuapp.com/challenging_dom')

canvas = motor.find_element(By.ID, 'page-footer')
localizacao = canvas.location
tamanho = canvas.size
png = motor.get_screenshot_as_png()

im = Image.open(BytesIO(png))

left = localizacao['x']
top = localizacao['y']
right = localizacao['x'] + tamanho['width']
bottom = localizacao['y'] + tamanho['height']

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image

botao = motor.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/a[1]')
id_botao = botao.get_attribute('id')
botao.click()

canvas = motor.find_element(By.ID, 'page-footer')
localizacao = canvas.location
tamanho = canvas.size
png = motor.get_screenshot_as_png()

im = Image.open(BytesIO(png))

left = localizacao['x']
top = localizacao['y']
right = localizacao['x'] + tamanho['width']
bottom = localizacao['y'] + tamanho['height']

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot2.png') # saves new cropped image

motor.quit()

img1 = cv2.imread('screenshot.png')
img2 = cv2.imread('screenshot2.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error = mse(img1, img2)

error, diff = mse(img1, img2)

print("Image matching Error between the two images:", error)

cv2.imshow("difference", diff)