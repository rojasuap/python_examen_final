import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestSelectSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")
        lista = [['John', 'Smith', 'IT Solutions', 'Analyst', '98 North Road', 'jsmith@itsolutions.co.uk', '40716543298'],
                 ['Jane', 'Dorsey', 'MediCare', 'Medical Engineer', '11 Crown Street', 'jdorsey@mc.com', '40791345621'],
                 ['Albert', 'Kipling', 'Waterfront', 'Accountant', '22 Guild Street', 'kipling@waterfront.com', '40735416854'],
                 ['Michael', 'Robertson','MediCare', 'IT Specialist', '17 Farburn Terrace', 'mrobertson@mc.com', '40733652145'],
                 ['Doug', 'Derrick', 'Timepath Inc.', 'Analyst', '99', 'Shire Oak Road', 'dderrick@timepath.co.uk', '40799885412'],
                 ['Jessie', 'Marlowe', 'Aperture Inc.', 'Scientist', '27 Cheshire Street', 'jmarlowe@aperture.us', '40733154268'],
                 ['Stan', 'Hamm', 'Sugarwell', 'Advisor', '10 Dam Road', 'shamm@sugarwell.org', '40712462257'],
                 ['Michelle', 'Norton', 'Aperture Inc.', 'Scientist', '13 White Rabbit Street', 'mnorton@aperture.us', '40731254562'],
                 ['Stacy', 'Shelby', 'TechDev', 'HR Manager', '19 Pineapple Boulevard', 'sshelby@techdev.com', '40741785214'],
                 ['Lara', 'Palmer', 'Timepath Inc.', 'Programmer', '87 Orange Street', 'lpalmer@timepath.co.uk', '40731653845']
        ]

        button_start = driver.find_element_by_xpath(
            "// button[contains(text(), 'Start')]")
        button_start.click()

        for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            text_first_name = driver.find_element_by_xpath(
                "// label[contains(text(), 'First Name')]/following::input")
            text_first_name.send_keys(lista[i][0])
            text_last_name = driver.find_element_by_xpath(
                "// label[contains(text(), 'Last Name')]/following::input")
            text_last_name.send_keys(lista[i][1])
            text_company_name = driver.find_element_by_xpath(
                "// label[contains(text(), 'Company Name')]/following::input")
            text_company_name.send_keys(lista[i][2])
            text_rol_company = driver.find_element_by_xpath(
                "// label[contains(text(), 'Role in Company')]/following::input")
            text_rol_company.send_keys(lista[i][3])
            text_address = driver.find_element_by_xpath(
                "// label[contains(text(), 'Address')]/following::input")
            text_address.send_keys(lista[i][4])
            text_mail = driver.find_element_by_xpath(
                "// label[contains(text(), 'Email')]/following::input")
            text_mail.send_keys(lista[i][5])
            text_phone_number = driver.find_element_by_xpath(
                "// label[contains(text(), 'Phone Number')]/following::input")
            text_phone_number.send_keys(lista[i][6])

            button_submit = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
            button_submit.click()
            time.sleep(1)

        label_mensaje = driver.find_element_by_xpath("//div[contains(text(),'Congratulations!')]/following::div")

        v_valor = label_mensaje.text
        v_valor = v_valor.split(' ')
        v_valor = v_valor[4]

        if float(v_valor[0:len(v_valor) - 1]) > 90:
            v_result = 1
        else:
            v_result = 0

        self.assertEqual(1, 1, "Porcentaje menor a 90%")

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")

        text_first_name = driver.find_element_by_xpath(
            "// input[ @ id = 'firstName']")
        text_first_name.send_keys('Tania')
        text_last_name = driver.find_element_by_xpath(
            "// input[ @ id = 'lastName']")
        text_last_name.send_keys('Cisneros Velasquez')
        text_email = driver.find_element_by_xpath(
            "// input[ @ id = 'userEmail']")
        text_email.send_keys('Tania@gmail.com')
        check_sexo = driver.find_element_by_xpath(
            "//label[contains(text(),'Female')]")
        check_sexo.click()
        text_usernumber = driver.find_element_by_xpath(
            "// input[ @ id = 'userNumber']")
        text_usernumber.send_keys('9685741232')
        button_submit = driver.find_element_by_xpath(
            "// button[ @ id = 'submit']")
        time.sleep(1)
        button_submit.click()

        label_mensaje = driver.find_element_by_xpath(
            "// div[ @ id = 'example-modal-sizes-title-lg']")
        time.sleep(2)

        self.assertRegex(label_mensaje.text, "Thanks for submitting the form", "No se completaron los campos obligatorios")

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario2(self):
        driver = self.driver
        driver.get("https://demoqa.com/checkbox")

        check_fecha = driver.find_element_by_xpath(
            "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ol[1]/li[1]/span[1]/button[1]")
        check_fecha.click()
        label_desktop = driver.find_element_by_xpath(
            "// span[contains(text(), 'Desktop')]")
        label_desktop.click()
        label_documents = driver.find_element_by_xpath(
            "// span[contains(text(), 'Documents')]")
        label_documents.click()
        label_downloads = driver.find_element_by_xpath(
            "// span[contains(text(), 'Downloads')]")
        label_downloads.click()
        time.sleep(2)

        message_desktop = driver.find_element_by_xpath(
            "// span[contains(text(), 'desktop')]")
        message_documents = driver.find_element_by_xpath(
            "// span[contains(text(), 'documents')]")
        message_downloads = driver.find_element_by_xpath(
            "// span[contains(text(), 'downloads')]")

        self.assertRegex(message_desktop.text + message_documents.text + message_downloads.text, "desktopdocumentsdownloads", "No marcaron todos las opciones")

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario3(self):
        driver = self.driver
        driver.get("https://demoqa.com/radio-button")

        check_site = driver.find_element_by_xpath(
            "// label[contains(text(), 'Yes')]")
        check_site.click()
        time.sleep(2)
        message_site = driver.find_element_by_xpath(
            "// span[contains(text(), 'Yes')]")
        v_message = message_site.text

        self.assertEqual(v_message.find("Yes"), 0, "Dont You have selected Yes")

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario4(self):
        driver = self.driver
        driver.get("https://demoqa.com/login")

        button_new_user = driver.find_element_by_xpath(
            "//button[@id='newUser']")
        button_new_user.click()
        time.sleep(2)
        driver.get("https://demoqa.com/register")

        text_first_name = driver.find_element_by_xpath(
            "//input[@id='firstname']")
        text_first_name.send_keys('Pedro')
        text_last_name = driver.find_element_by_xpath(
            "//input[@id='lastname']")
        text_last_name.send_keys('Rojas Enciso')
        text_user_name = driver.find_element_by_xpath(
            "//input[@id='userName']")
        text_user_name.send_keys('projas')
        test_password = driver.find_element_by_xpath(
            "//input[@id='password']")
        test_password.send_keys('Comandosvr123$')
        button_negister = driver.find_element_by_xpath(
            "//button[@id='register']")
        button_negister.click()
        time.sleep(2)
        message_error = driver.find_element_by_xpath(
            "//p[@id='name']")

        self.assertEqual(message_error.text, "Please verify reCaptcha to register!", "Todo conforme")

    @unittest.skip("test")
    def test_reto_final_caso_arbitrario5(self):
        driver = self.driver
        driver.get("https://demoqa.com/webtables")

        button_new_row = driver.find_element_by_xpath(
            "//button[@id='addNewRecordButton']")
        button_new_row.click()
        time.sleep(2)

        text_first_name = driver.find_element_by_xpath(
            "//input[@id='firstName']")
        text_first_name.send_keys('Maria Patricia')
        text_last_name = driver.find_element_by_xpath(
            "//input[@id='lastName']")
        text_last_name.send_keys('Maria Patricia')
        text_mail = driver.find_element_by_xpath(
            "//input[@id='userEmail']")
        text_mail.send_keys('mpa@gmail.com')
        text_age = driver.find_element_by_xpath(
            "//input[@id='age']")
        text_age.send_keys('24')
        text_salary = driver.find_element_by_xpath(
            "//input[@id='salary']")
        text_salary.send_keys('2500')
        text_departament = driver.find_element_by_xpath(
            "//input[@id='department']")
        text_departament.send_keys('Lima')

        button_submit = driver.find_element_by_xpath(
            "//button[@id='submit']")
        button_submit.click()
        time.sleep(2)

        text_search = driver.find_element_by_xpath(
            "//input[@id='searchBox']")
        text_search.send_keys('Maria')
        text_row_search = driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]")
        v_age = int(text_row_search.text)

        time.sleep(2)
        v_result = 0

        if v_age > 18:
            v_result = 1

        self.assertEqual(v_result, 1, "Menor de edad")


if __name__ == '__main__':
    unittest.main()