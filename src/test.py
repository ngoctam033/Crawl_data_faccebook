import requests

def get_html(url):
    response = requests.get(url)
    #kiểm tra xem truy cập thành công hay không
  # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Trả về nội dung HTML của trang web
        return response.text
    else:
        print(f"Unable to get URL, status code: {response.status_code}")
        return None
    
# Sử dụng hàm
url = 'https://www.facebook.com/groups/230606407429489/user/100012836956002/'
html = get_html(url)
print(html)