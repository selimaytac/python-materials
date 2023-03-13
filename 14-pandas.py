import pandas as pd

# Bir DataFrame oluşturma
data = {'isim': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
        'yaş': [23, 45, 31, 29],
        'ülke': ['TR', 'US', 'DE', 'FR']}

df = pd.DataFrame(data)

# DataFrame'i yazdırma
print(df)

# Output:
#     isim  yaş  ülke
# 0   Ahmet   23   TR
# 1  Mehmet   45   US
# 2    Ayşe   31   DE
# 3   Fatma   29   FR

# CSV dosyasından veri okuma
df = pd.read_csv('veriler.csv')

# Excel dosyasından veri okuma
df = pd.read_excel('veriler.xlsx')

# Verileri CSV dosyasına yazma
df.to_csv('veriler.csv', index=False)

# Verileri Excel dosyasına yazma
df.to_excel('veriler.xlsx', index=False)


# Bir DataFrame oluşturma
data = {'isim': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
        'yaş': [23, 45, 31, 29],
        'ülke': ['TR', 'US', 'DE', 'FR']}

df = pd.DataFrame(data)

# 'isim' sütununa erişme
isimler = df['isim']
print(isimler)

# İlk satıra erişme
ilk_satir = df.loc[0]
print(ilk_satir)

# İlk iki satıra erişme
ilk_iki_satir = df.iloc[:2]
print(ilk_iki_satir)

#--------------------------------------------

# Log dosyasını bir DataFrame'e yükleme
log_df = pd.read_csv("server_logs.csv")

# Tarih aralığı seçimi
start_date = '2022-01-01'
end_date = '2022-01-31'
date_filter = (log_df['timestamp'] >= start_date) & (log_df['timestamp'] <= end_date)

# Kelime arama
search_word = 'error'
word_filter = log_df['message'].str.contains(search_word)

# Filtreleme işlemlerinin birleştirilmesi
result_df = log_df[date_filter & word_filter]

#--------------------------------------------

# Veri kümesini bir DataFrame'e yükleme
data_df = pd.read_csv("server_data.csv")

# Sütundaki benzersiz değerlerin sayısı
unique_count = data_df['server_name'].nunique()

# Değerlerin sıklığı
freq_count = data_df['server_name'].value_counts()

# Değerlerin ortalaması
mean_value = data_df['response_time'].mean()

#--------------------------------------------

# Tarih aralığı belirleme
start_date = '2022-01-01'
end_date = '2022-01-31'

# Zaman serisini bir DataFrame'e yükleme
traffic_df = pd.read_csv("traffic_data.csv", parse_dates=['timestamp'], index_col='timestamp')

# Tarih aralığına göre filtreleme
filtered_df = traffic_df.loc[start_date:end_date]

# Ortalama trafik miktarını hesaplama
average_traffic = filtered_df['traffic'].mean()

#--------------------------------------------

def count_logs_by_endpoint(start_date, end_date, filename):
    # read log file into a pandas dataframe
    df = pd.read_csv(filename, delimiter=' ', header=None, usecols=[3, 5], names=['endpoint', 'datetime'])

    # filter the dataframe by start_date and end_date
    mask = (df['datetime'] >= start_date) & (df['datetime'] <= end_date)
    filtered_df = df.loc[mask]

    # group by endpoint and count the number of occurrences
    count_df = filtered_df.groupby(['endpoint']).size().reset_index(name='count')

    return count_df

#--------------------------------------------

import pandas as pd
import numpy as np

# orders table
orders_data = {'order_id': [1001, 1002, 1003, 1004],
               'customer_id': [101, 102, 103, 104],
               'order_date': ['2022-02-01', '2022-02-02', '2022-02-02', '2022-02-03']}
orders_df = pd.DataFrame(orders_data)

# customers table
customers_data = {'customer_id': [101, 102, 103, 104],
                  'customer_name': ['Alice', 'Bob', 'Charlie', 'Dave'],
                  'customer_email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'dave@example.com']}
customers_df = pd.DataFrame(customers_data)

# products table
products_data = {'product_id': [1, 2, 3, 4],
                 'product_name': ['Product A', 'Product B', 'Product C', 'Product D'],
                 'product_price': [10.0, 20.0, 30.0, 40.0]}
products_df = pd.DataFrame(products_data)

# order details table
order_details_data = {'order_id': [1001, 1001, 1002, 1002, 1002, 1003, 1004, 1004],
                      'product_id': [1, 2, 2, 3, 4, 1, 3, 4],
                      'quantity': [1, 2, 1, 3, 1, 2, 1, 2]}
order_details_df = pd.DataFrame(order_details_data)

# join orders and customers tables on customer_id
orders_customers_df = pd.merge(orders_df, customers_df, on='customer_id')

# join order details and products tables on product_id
order_details_products_df = pd.merge(order_details_df, products_df, on='product_id')

# join orders_customers and order_details_products on order_id
order_history_df = pd.merge(orders_customers_df, order_details_products_df, on='order_id')

# calculate the total price for each order
order_history_df['total_price'] = order_history_df['quantity'] * order_history_df['product_price']

# group by customer and calculate the total spent
customer_spending_df = order_history_df.groupby('customer_id')['total_price'].sum().reset_index()

# sort by total spent in descending order
customer_spending_df = customer_spending_df.sort_values('total_price', ascending=False)

print(customer_spending_df)

