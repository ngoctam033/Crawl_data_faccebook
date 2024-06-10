import pandas as pd

def remove_duplicates():
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(r'G:\My Drive\facebook_group_members_filter.csv')

    # Loại bỏ các dòng trùng lặp
    df = df.drop_duplicates(subset='Name')

    #tạo một lít chứa các từ khóa cần loại bỏ
    keywords = ['anco', 'inuv', 'Vậttư QC ThắngLợi', 'Xạ Thủ Cừ Khôi', 'Xưởng In Bình Dương Giá Tốt',
                'Vật Tư Kim Khí', 'Công Ty Xuất Nhập Khẩu & Sản Xuất Giấy In Nhiệt - Hansol - Sahara'
                'Nam Led Hàn Quốc', 'Vboss Laser','ADV Sự kiện & Quảng Cáo', 'AD-MART Thúy Vi',
                'Thiên Vĩ', 'Dylled', 'QuảngCáo Đức Minh', 'Cô Em Bảng Hiệu', 'ADmart', 'Mi Minh Hiếu',
                'Goodlight', 'Laser Tâm', 'Hiệp Tân','Thu Gom Kính Vụn', 'KD Thiên Nam', 'Phuong Hong', 'Badavision',
                'MÁY IN UV', 'Nguyendanh Nam Khanh', 'Led HomieLives',
                'Skv', 'Shv Thiên Nga', 'Nguyễn Thị Khánh Ly']

    #gọi hàm str.contains để loại bỏ các dòng chứa từ khóa trong cột 'Name'
    #case=False để không phân biệt chữ hoa và chữ thường
    #dấu ~ ở trước df['Name'].str.contains('anco|inuv', case=False) để loại bỏ các dòng chứa từ khóa
    df = df[~df['Name'].str.contains('|'.join(keywords), case=False)]

    # Ghi dữ liệu đã được lọc vào file mới
    df.to_csv(r'G:\My Drive\facebook_group_members_filter.csv', index=False)

if __name__ == '__main__':
    remove_duplicates()