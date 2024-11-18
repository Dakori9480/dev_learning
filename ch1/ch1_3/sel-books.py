from bs4 import BeautifulSoup

fp = open("ch1/ch1_3/books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel('#nu')                           # id가 nu인 것을 추출
sel('li#nu')                         # li의 nu인 것을 추출
sel("ul > li#nu")                    
sel('#bible li#nu')                   
sel('#bible > #nu')
sel('ul#bible > li#nu')
sel("li[id='nu']")
sel("li:nth-of-type(4)")