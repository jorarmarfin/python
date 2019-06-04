# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import sys
import csv
from time import sleep

def llenar_formulario(respuestas):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdCCm0EG1GJFROd8-OMIOMbBsWt3m4ewKKeK1PhF7bkYBqVYw/viewform?usp=sf_link")
    driver.find_element_by_css_selector("input[aria-label='Primer pregunta']").send_keys(respuestas[0])
    driver.find_element_by_css_selector("textarea[aria-label='Segunda pregunta']").send_keys(respuestas[1])
    driver.find_element_by_css_selector(u"div[aria-label='{}']".format(unicode(respuestas[2],"utf-8"))).click()
    sleep(1)
    driver.find_element_by_css_selector(u".freebirdFormviewerViewItemsCheckboxChoice div[aria-label='{}']".format(unicode(respuestas[3],"utf-8"))).click()
    sleep(1)
    driver.find_element_by_css_selector("div[role=listbox]").click()
    quinta_selector = u".exportSelectPopup .quantumWizMenuPaperselectOption[aria-label='{}']".format(unicode(respuestas[4],"utf-8"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, quinta_selector)))
    driver.find_element_by_css_selector(quinta_selector).click()
    sleep(1)
    driver.find_element_by_css_selector("div[aria-label='Fila 1, {}']".format(respuestas[5])).click()
    driver.find_element_by_css_selector("div[aria-label='Fila 2, {}']".format(respuestas[6])).click()
    fecha = respuestas[7].split("/")
    driver.find_element_by_css_selector("input[aria-label='Día del mes']").send_keys(fecha[0])
    driver.find_element_by_css_selector("input[aria-label='Mes']").send_keys(fecha[1])
    driver.find_element_by_css_selector("input[aria-label='Año']").clear()
    driver.find_element_by_css_selector("input[aria-label='Año']").send_keys(fecha[2])
    driver.find_element_by_xpath("//span[text()='Enviar']").click()

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

with open('Respuestas.csv', 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        llenar_formulario(row)