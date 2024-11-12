from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url).read()

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info.point_up > span.value")
print("usd/krw =", price)