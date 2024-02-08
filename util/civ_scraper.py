from bs4 import BeautifulSoup
import requests
import shutil

url = "https://civilization.fandom.com/wiki/Leaders_(Civ6)"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

imgs = soup.find_all("img", attrs={"alt": True, "data-src": True, "data-relevant": 1})
for i, img in enumerate(imgs):
    end = img["data-src"].index("scale-to-width-down")
    url = img["data-src"][:end]
    img_response = requests.get(url, stream=True)
    img_response.raw.decode_content = True

    filename = f"static/img/{img["alt"]}.png"
    with open(filename, "wb") as file:
        shutil.copyfileobj(img_response.raw, file)
    
    print(f"Scraping image {i} of {len(imgs)} ({img["alt"]})")
    
"""
tables = soup.find_all("table", class_="article-table")

for table in tables:
    for tr in table.tbody:
        tr[0]
        
        for td in tr:
            print(td)
            print("--------------------------------------")
        print("\n########################################\n")
    break

print(len(soup.find_all("table", class_="article-table")))
"""
# response = requests.get("https://civilization.fandom.com/wiki/Civilization_VI?file=Frederick_Barbarossa_%28Civ6%29.png")

"""
while response["data"]:
    for post in response["data"]:
        im_urls = []
        if "media_metadata" in post:
            for media_id, metadata in post["media_metadata"].items():
                for p in metadata.get("p", []):
                    if p["x"] == 108:
                        im_urls.append(p["u"])       
        elif "preview" in post:
            for im in post["preview"]["images"]:
                for resolution in im["resolutions"]:
                    if resolution["width"] == 108:
                        im_urls.append(resolution["url"])
        for i, im_url in enumerate(im_urls):
            im_url = re.sub("amp;", "", im_url)
            im_response = requests.get(im_url, stream=True)
            im_response.raw.decode_content = True
            filename = f"data/{post['created_utc']}_{i}.png"
            with open(filename, "wb") as file:
                shutil.copyfileobj(im_response.raw, file)
    params["after"] = response["data"][-1]["created_utc"]
    response = requests.get(url, params=params)
    response = json.loads(response.text)
"""