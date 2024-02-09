from bs4 import BeautifulSoup
import requests
import shutil

url = "https://civilization.fandom.com/wiki/Leaders_(Civ6)"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="article-table")

for i, table in enumerate(tables):

    imgs = table.find_all("img", attrs={"alt": True, "data-src": True})

    print(f"\nSearching table {i+1} of {len(tables)}\n")

    for j, img in enumerate(imgs):

        if img["height"] != "44":
            print(f"Image {j+1} skipped")
            continue

        end = img["data-src"].index("scale-to-width-down")
        img_url = img["data-src"][:end]

        img_response = requests.get(img_url, stream=True)
        img_response.raw.decode_content = True

        filename = f"static/img/{img["alt"]}.png"
        with open(filename, "wb") as file:
            shutil.copyfileobj(img_response.raw, file)
        
        print(f"Scraping image {j+1} of {len(imgs)} ({img["alt"]})")
