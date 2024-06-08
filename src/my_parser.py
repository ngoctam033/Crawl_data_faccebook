#import thư viện dùng để phân tích cú pháp html
from bs4 import BeautifulSoup

#tạo một class Parser
class Parser:
    #khởi tạo hàm constructor
    def __init__(self, html):
        #khởi tạo html
        self.html = html
        #khởi tạo soup
        self.soup = BeautifulSoup(html, 'html.parser')
    def write_members_to_file(self, members):
        with open('facebook_group_members1.html', 'w', encoding='utf-8') as f:
            for member in members:
                f.write(member.prettify() + '\n')

    def get_group_members(self):
        members = self.soup.find_all('div', {'data-visualcompletion': 'ignore-dynamic'})
        #kiểm tra xem có bao nhiêu phần tử trong mảng members
        print(len(members))
        return members
    def get_member_info(self, members):
        #tạo một mảng để lưu tên và link của các thành viên
        member_info = []
        #duyệt qua từng phần tử trong mảng members
        for member in members:
            #tìm thẻ a đầu tiên trong member
            #nếu không tìm thấy thẻ a thì thông báo và trả về nône
            a_tag = member.find('a')
            if a_tag:
                #lấy giá trị của thuộc tinh aria-label trong thẻ a
                aria_label = a_tag.get('aria-label')
                if aria_label is None:
                    continue
                #tìm thuộc tính href trong a_tag
                href = a_tag.get('href')
                if href:
                    #lưu tên và link vào mảng member_info
                    member_info.append({'name': aria_label, 'link': 'https://www.facebook.com'+href})
        return member_info