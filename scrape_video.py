from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def downloadVideo(link, id): 
    cookies = {
        '__cflb': '02DiuEcwseaiqqyPC5qr2kcTPpjPMVimuJkzQS9rFAvhy',
        '_ga': 'GA1.2.1338233632.1672162654',
        '_gid': 'GA1.2.1487521326.1672162654',
        '__gads': 'ID=08166b4d15a4b40a-221ca0e9a5d900c4:T=1672162652:RT=1672162652:S=ALNI_Ma48KkZwyIBAhGC-rLzdSTvxKjWLw',
        '__gpi': 'UID=0000091b87ab1327:T=1672162652:RT=1672162652:S=ALNI_MaNOdlY6HVPr_i8Zfak3j6uO2MtpA',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=02DiuEcwseaiqqyPC5qr2kcTPpjPMVimuJkzQS9rFAvhy; _ga=GA1.2.1338233632.1672162654; _gid=GA1.2.1487521326.1672162654; __gads=ID=08166b4d15a4b40a-221ca0e9a5d900c4:T=1672162652:RT=1672162652:S=ALNI_Ma48KkZwyIBAhGC-rLzdSTvxKjWLw; __gpi=UID=0000091b87ab1327:T=1672162652:RT=1672162652:S=ALNI_MaNOdlY6HVPr_i8Zfak3j6uO2MtpA; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'dGljelRm',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup= BeautifulSoup(response.text,"html.parser")
    
    downloadLink = downloadSoup.a["href"]

    mp4File=urlopen(downloadLink)
    with open(f"videos/{id}.mp4","wb") as output:
        while True:
            data=mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

driver=webdriver.Chrome()
#put the account from which you want to download videos without watermark from
driver.get("https://www.tiktok.com/@placeholder")

time.sleep(1)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup=BeautifulSoup(driver.page_source, "html.parser")
videos=soup.find_all("div",{"class":"tiktok-yz6ijl-DivWrapper"})

print(len(videos))
for index, video in enumerate(videos):
    downloadVideo(video.a["href"], index)
    time.sleep(10)

