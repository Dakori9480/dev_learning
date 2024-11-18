from bs4 import BeautifulSoup

fp = open("ch1/ch1_3/fruits-vegetables.html", encoding='utf-8')
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("li:nth-of-type(8)").string)                     # 8번째 요소 추출
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)          # ve-list에서 4번째 요소 추출

cond = {"data-lo" : "us", "class" : "black"}                           # 조건이 될 객체를 생성
print(soup.find("li", cond).string)                                    # 그 조건에 맞는 정보 추출