import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = 'kgh9480'
PASS = 'kang1311@'

session = requests.session()

login_info = {
    "m_id" : USER,
    "m_passwd" : PASS
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 페이지에 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 코인 가져오기
soup = BeautifulSoup(res.text, 'html.parser')
mileage = soup.select_one(".mileage_section1 dd span").get_text()
coin = soup.select_one(".mileage_section2 dd span").get_text()
print("마일리지:", mileage)
print("코인:", coin)
