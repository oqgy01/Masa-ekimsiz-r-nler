import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/spreadsheets/d/1AP9EFAOthh5gsHjBCDHoUMhpef4MSxYg6wBN0ndTcnA/edit#gid=0"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
first_cell = soup.find("td", {"class": "s2"}).text.strip()
if first_cell != "Aktif":
    exit()
first_cell = soup.find("td", {"class": "s1"}).text.strip()
print(first_cell)







import pandas as pd
url = "https://task.haydigiy.com/FaprikaXls/UR15LT/1/"
try:
    df = pd.read_excel(url)
except Exception as e:
    print("Hata:", e)
    exit()
keep_columns = ["UrunAdi", "AmazonKodu"]
df = df[keep_columns]
df = df.drop_duplicates()
output_file = "Masa Çekimsiz İç Giyim Ürünler.xlsx"
try:
    df.to_excel(output_file, index=False)
    print("İşlem tamamlandı. Filtrelenmiş veriler '{}' dosyasına kaydedildi.".format(output_file))
except Exception as e:
    print("Hata:", e)

