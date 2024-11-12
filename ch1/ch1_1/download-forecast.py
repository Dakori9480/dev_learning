import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL에 인코딩
values = {
    # 지역번호 : 부산
    'stnID' : '159'
}

# 위의 딕셔너리를 URL 형태로 변환
params = urllib.parse.urlencode(values)

# 요청 전용 URL을 생성

url = API + "?" + params
print('url=',url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)