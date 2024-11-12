import urllib.request

# URL 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

# urlopen() 함수로 주소에 접근 후 read()로 데이터 읽기
mem = urllib.request.urlopen(url).read()

# 그 후 파일을 작성하는 함수 작성
with open(savename, mode='wb') as f:
    f.write(mem)
    print("완료")