import urllib.request

# URL 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
# 매개 변수로 주소와, 저장할 파일 이름을 받음
print("완료")
