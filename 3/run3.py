import csv
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver
from selenium.webdriver.support.ui import Select

driver = Driver(uc=True)

with open('pincode3.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        pin_code = row[0]
        print(pin_code)

        driver.get("https://www.viewlogies.net/locate")
        input_boxs = driver.find_elements(By.CSS_SELECTOR, 'div.react-code-input > input')
        for k in range(len(input_boxs)):
            input_box = input_boxs[k]
            input_box.send_keys(pin_code[k])

        time.sleep(1)
        try:
            submit_btn = driver.find_elements(By.CLASS_NAME, 'viewlogies-button')[0]
            submit_btn.click()

            time.sleep(1)
            try:
                image_url = driver.find_element(By.CSS_SELECTOR, '.client-header img').get_attribute('src')
            except:
                image_url = ""
            current_page = driver.current_url
            slug = "/" + current_page.split("/")[3]
            try:
                company_name = driver.find_elements(By.CSS_SELECTOR, '.contact-us-content p')[1].text.split('video')[0]
            except:
                company_name = ""
            try:
                service_time = driver.find_elements(By.CSS_SELECTOR, '.subheader h3')[0].text.split(":")[1].strip()
                service_clock = service_time.split(" ")[-1]
                service_date = service_time.replace(service_clock, "").strip()
            except:
                service_date = ""

            result_data = [image_url, company_name, slug, current_page, pin_code, service_date]
            with open('result3.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(result_data)

        except:
            pass

driver.quit()
