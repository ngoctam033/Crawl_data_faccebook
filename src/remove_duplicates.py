import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv(r'G:\My Drive\facebook_group_members_filter.csv')

# Loại bỏ các dòng trùng lặp
df = df.drop_duplicates(subset='Name')

# Ghi dữ liệu đã được lọc vào file mới
df.to_csv(r'G:\My Drive\facebook_group_members_filter.csv', index=False)