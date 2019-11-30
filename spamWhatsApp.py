#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text='Eu sou um Bot! Obrigado pela atenção' # Mensagem
no_of_message=1 # Quantidade de vezes que a msg será enviada para o mesmo numero
moblie_no_list=[556199240XXXX, 5511XXXXXXXXX, "Bonde do Pesadao"] # lista com os numeros que receberão as msg, separar por ",", caso for enviar para grupos inserir o nome entre "".

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')
sleep(10) # tempo de espera para digitalizar o QRCode

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        assert isinstance(driver.switch_to_alert().accept, object)
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("Número invalido :"+str(phone_no))
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(10)
        is_connected()