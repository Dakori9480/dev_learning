from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# find_all()로 추출하기
links = soup.find_all("a")

for a in links:
    # a의 데이터를 딕셔너리로 반환
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)