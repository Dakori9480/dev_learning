from urllib.parse import urljoin

base = "http://example.com/html/a.html"

# 상대 경로를 절대 경로로 바꿔주는 역할
# 사용법 : urljoin(base, path) 
# path에는 상대 경로를 입력함

print(urljoin(base, "b.html"))

# 상대 경로
print(urljoin(base, "/hoge.html"))