#import thư viện bs4
from bs4 import BeautifulSoup
#import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

#tạo một class Scraper
class Scraper:
    #khởi tạo hàm constructor
    def __init__(self, url):
        #khởi tạo url
        self.url = url
        # Khởi tạo driver
        self.driver = webdriver.Firefox(service=Service(r"D:\geckodriver.exe"))
        #mở trình duyệt
        self.driver.get(url)

    def login(self, email, password):
        # Khởi tạo WebDriverWait với thời gian chờ là 10 giây
        wait = WebDriverWait(self.driver, 10)
    
        # Tìm đến trường nhập liệu dựa trên id của nó
        # Đầu tiên, nhập sdt/email
        # Chờ cho đến khi phần tử có thể tương tác
        input_field = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    
        # Nhập giá trị vào trường này
        input_field.send_keys(email)
    
        # Nhập mật khẩu
        input_field = wait.until(EC.element_to_be_clickable((By.ID, 'pass')))
    
        # Nhập giá trị vào trường này
        input_field.send_keys(password)
    
        # Tiếp theo, thực hiện click vào nút đăng nhập
        # Chờ cho đến khi phần tử có thể tương tác
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'loginbutton')))
    
        # Click vào nút đăng nhập
        login_button.click()

    def get_page_html(self):
            # Sử dụng JavaScript để lấy nội dung HTML hiện tại của trang web
            html = self.driver.execute_script("return document.documentElement.outerHTML;")
            
            # Trả về nội dung HTML
            return html

    def open_new_tab(self, url):
        # Lưu lại handle của cửa sổ hiện tại
        current_window = self.driver.current_window_handle
    
        try:
            # Mở một tab mới với URL được chỉ định
            self.driver.execute_script("window.open('" + url + "');")
        
            # Chuyển WebDriver sang tab mới
            self.driver.switch_to.window(self.driver.window_handles[-1])
        
            # Đợi 5s
            time.sleep(5)
        
            #cuộn trang xuống dưới cùng
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            # Lấy nội dung HTML của trang web này
            html = self.driver.page_source
        
            #chuyển đổi html sang soup
            html = BeautifulSoup(html, 'html.parser')
        
            # Đóng tab hiện tại
            self.driver.close()
        
            # Chuyển WebDriver trở lại cửa sổ ban đầu
            self.driver.switch_to.window(current_window)
        
            return html.get_text()
    
        except Exception as e:
            print(f"An error occurred: {e}")
            self.driver.switch_to.window(current_window)
            return 'Không có bài viết mới'

    def scroll_page(self, scrolls):
        #tạo một biến để lưu vị trí duyệt
        index = 0
        #tạo một list đê lưu name và link của thành viên
        for _ in range(scrolls):
            try:
                # Cuộn trang xuống dưới cùng
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print('đang cuộn trang lần thứ', _)
                # Đợi một chút để trang tải thêm nội dung
                time.sleep(2) 
                #sử dụng WebDriverWait và expected_conditions để chờ cho đến khi phần tử <a> xuất hiện
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
                # Tìm các thẻ a có thuộc tính data-visualcompletion='ignore-dynamic'
                members = self.driver.find_elements(By.XPATH, "//div[@data-visualcompletion='ignore-dynamic']")
                #duyêt qua từng phần tử trong mảng members
                for member in members[index:]:
                    try:
                        #tạo một biến lưu html của thành viên
                        html = member.get_attribute('outerHTML')
                        #tạo một đối tượng soup từ html
                        soup = BeautifulSoup(html, 'html.parser')
                        #tìm các thẻ a trong soup
                        a_tag = soup.find('a')
                        #kiểm tra xem a_tag có tồn tại không
                        if a_tag:
                            #lấy giá trị của thuộc tính aria-label
                            aria_label = a_tag.get('aria-label')
                            if aria_label is None:
                                continue
                            #lấy giá trị của thuộc tính href
                            href = a_tag.get('href')
                            if href:
                                #goi hàm open_new_tab
                                text = self.open_new_tab('https://www.facebook.com'+href)
                                #tìm trong text nội dung "Không có bài viết mới"
                                if "Không có bài viết mới" not in text:
                                    if "Tải lại trang" not in text:
                                        #thêm name và link vào file csv
                                        with open(r'G:\My Drive\facebook_group_members_filter.csv', 'a', newline='', encoding='utf-8') as f:
                                            writer = csv.DictWriter(f, fieldnames=['name', 'link'], lineterminator='\n')
                                            writer.writerow({'name': aria_label, 'link': 'https://www.facebook.com'+href})
                                        # print('Thành viên:', aria_label, 'hợp lệ')
                                        # print('link:', 'https://www.facebook.com'+href)
                                    else:
                                        #Tạm dừng 2 tiếng
                                        print('Tạm dừng 30 phút...')
                                        #in ra thoiwf gian hieenj taij
                                        print('Thời gian hiện tại:', time.strftime('%H:%M:%S'))
                                        time.sleep(1800)
                        
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        continue  # Bỏ qua phần tử này và tiếp tục với phần tử tiếp theo
                index = len(members)        
            except Exception as e:
                print(f"An error occurred: {e}")
                continue         
            print(index)


    



