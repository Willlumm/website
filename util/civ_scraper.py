from bs4 import BeautifulSoup
import requests
import shutil

url = "https://civilization.fandom.com/wiki/Leaders_(Civ6)"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

imgs = soup.find_all("img", attrs={"alt": True, "data-src": True, "data-relevant": 1})

for i, img in enumerate(imgs):

    end = img["data-src"].index("scale-to-width-down")
    img_url = img["data-src"][:end]

    img_response = requests.get(img_url, stream=True)
    img_response.raw.decode_content = True

    filename = f"static/img/{img["alt"]}.png"
    with open(filename, "wb") as file:
        shutil.copyfileobj(img_response.raw, file)
    
    print(f"Scraping image {i} of {len(imgs)} ({img["alt"]})")
