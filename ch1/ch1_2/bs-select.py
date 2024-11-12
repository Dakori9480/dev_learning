from bs4 import BeautifulSoup

html = """

<html><body>
    <div id="meigen">
        <h1>위키북스 도서</h1>
        <ul class="items">
            <li>유니티 게임 이펙트 입문</li>
            <li>차현진 괴롭히기</li>
            <li>1000층 햄버거 빨리 쌓는 방법</li>
        </ul>
    </div>
</body></html>    
"""

soup = BeautifulSoup(html, "html.parser")

# 타이틀 추출하기
h1 = soup.select_one("div#meigen > h1").string
print("h1 = ", h1)

# 목록 추출하기
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li = ", li.string)