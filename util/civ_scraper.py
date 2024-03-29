from bs4 import BeautifulSoup
import requests
import shutil

def scrape_imgs_from_tables(url, dir, width=None):

    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", class_="article-table")

    for i, table in enumerate(tables):

        imgs = table.find_all("img")

        print(f"\nSearching table {i+1} of {len(tables)}\n")

        for j, img in enumerate(imgs):

            if img["width"] != str(width):
                print(f"Image {j+1} ({img["alt"]}) skipped")
                continue
            
            if img.has_attr("data-src"):
                src = "data-src"
            else:
                src = "src"

            end = img[src].index("scale-to-width-down")
            img_url = img[src][:end]

            img_response = requests.get(img_url, stream=True)
            img_response.raw.decode_content = True

            filename = f"static/img/{dir}/{img["alt"]}.png"
            with open(filename, "wb") as file:
                shutil.copyfileobj(img_response.raw, file)
            
            print(f"Scraping image {j+1} of {len(imgs)} ({img["alt"]})")

def scrape_imgs_from_lists(url, dir, width=None):

    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    lists = soup.find_all("ul")

    for i, list_ in enumerate(lists):

        imgs = list_.find_all("img")

        print(f"\nSearching list {i+1} of {len(lists)}\n")

        for j, img in enumerate(imgs):

            if not img.has_attr("width") or img["width"] != str(width):
                print(f"Image {j+1} ({img["alt"]}) skipped")
                continue
            
            if img.has_attr("data-src"):
                src = "data-src"
            else:
                src = "src"

            end = img[src].index("scale-to-width-down")
            img_url = img[src][:end]

            img_response = requests.get(img_url, stream=True)
            img_response.raw.decode_content = True

            filename = f"static/img/{dir}/{img["alt"]}.png"
            with open(filename, "wb") as file:
                shutil.copyfileobj(img_response.raw, file)
            
            print(f"Scraping image {j+1} of {len(imgs)} ({img["alt"]})")

def scrape_imgs_from_divs(url, dir, width=None):

    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    divs = soup.find_all("div")

    for i, list_ in enumerate(divs):

        imgs = list_.find_all("img")

        print(f"\nSearching div {i+1} of {len(divs)}\n")

        for j, img in enumerate(imgs):

            if not img.has_attr("width") or img["width"] != str(width):
                print(f"Image {j+1} ({img["alt"]}) skipped")
                continue
            
            if img.has_attr("data-src"):
                src = "data-src"
            else:
                src = "src"

            end = img[src].index("scale-to-width-down")
            img_url = img[src][:end]

            img_response = requests.get(img_url, stream=True)
            img_response.raw.decode_content = True

            filename = f"static/img/{dir}/{img["alt"]}.png"
            with open(filename, "wb") as file:
                shutil.copyfileobj(img_response.raw, file)
            
            print(f"Scraping image {j+1} of {len(imgs)} ({img["alt"]})")

# scrape_imgs_from_tables("https://civilization.fandom.com/wiki/Leaders_(Civ6)", "leaders", height=44)
# scrape_imgs_from_tables("https://civilization.fandom.com/wiki/Map_(Civ6)", "maps", width=48)
# scrape_imgs_from_lists("https://civilization.fandom.com/wiki/Game_mode_(Civ6)", "modes", width=32)
scrape_imgs_from_divs("https://civilization.fandom.com/wiki/Victory_(Civ6)", "victories", width=60)
