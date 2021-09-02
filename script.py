from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class Robot(object):
    def __init__(self, path="C:\\Users\\joang\\OneDrive\\Documentos\\Desarrollo\\Python\\SofomJage\\geckodriver.exe"):
        self.path = path
        self.targets = []
        self.driver = None
    def createBrowser(self):
        self.driver = webdriver.Firefox(executable_path = self.path)
    def close(self):
        self.driver.quit()


username = sys.argv[1]
password = sys.argv[2]
robot = Robot()
robot.createBrowser()
robot.driver.get("https://ie.service-now.com/sm?id=sc_cat_item&sys_id=2b6ac6e6dba4d010c6e77dad6896195c")
WebDriverWait(robot.driver, 10).until(EC.presence_of_element_located((By.ID, "userNameInput")))
usernameInput = robot.driver.find_element_by_id("userNameInput")
usernameInput.send_keys(username)
robot.driver.find_element_by_id("passwordInput").send_keys(password)
robot.driver.find_element_by_id("submitButton").click()
WebDriverWait(robot.driver, 10).until(EC.element_to_be_clickable((By.ID, "sp_formfield_u_no_symptoms")))
robot.driver.find_element_by_id("sp_formfield_u_no_symptoms").click()
robot.driver.find_element_by_id("sp_formfield_u_contacto_estrecho").click()
robot.driver.find_element_by_id("sp_formfield_u_sin_situacion_alto_riesgo").click()
robot.driver.find_element_by_xpath("/html/body/div[1]/section/main/div[1]/div/sp-page-row/div/div/span/div/div/div[1]/div[2]/div/div[1]/div[3]/button").click()
robot.close()