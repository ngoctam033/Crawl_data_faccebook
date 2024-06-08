from scraper import Scraper
#Tạo một mảng chứa các đường link facebook
links = [
    "https://www.facebook.com/groups/868753816571574/members",
    "https://www.facebook.com/groups/congdongquangcaovietnam/members",
    "https://www.facebook.com/groups/917329955115021/members",
    "https://www.facebook.com/groups/916173878480785/members",
    "https://www.facebook.com/groups/230606407429489/members",
    "https://www.facebook.com/groups/728477237566746/members",
    "https://www.facebook.com/groups/524388087709763/members",
    "https://www.facebook.com/groups/1489527087847033/members",
    "https://www.facebook.com/groups/1229863860381268/members",
    "https://www.facebook.com/groups/denledvietnam/members",
    "https://www.facebook.com/groups/2262941230610853/members",  
]
for link in links:
    try:
        # Create an instance of the web scraper
        scraper = Scraper(link)
        print('đang thực hiện đăng nhập...')
        #truyền tham số là tên đăng nhập và mật khẩu
        scraper.login("0377289656", "*#0303*#@@")
        # scraper.login("0773792653", "*#0303*#")
        print('đang thực hiện cuộn trang...')
        scraper.scroll_page(2000)
        print('hoàn thanh!')
    except Exception as e:
        print(f"An error occurred with link {link}: {e}")
        continue