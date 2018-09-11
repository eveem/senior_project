from bs4 import BeautifulSoup
import requests

page_link = 'https://www.peesirilaw.com/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A1%E0%B8%A7%E0%B8%A5/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A1%E0%B8%A7%E0%B8%A5%E0%B8%81%E0%B8%8E%E0%B8%AB%E0%B8%A1%E0%B8%B2%E0%B8%A2%E0%B8%AD%E0%B8%B2%E0%B8%8D%E0%B8%B2.html'

page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, 'html.parser')

with open('criminal_code.html', 'a') as f:
    for line in page_content:
        f.write(str(line))