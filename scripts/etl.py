import pandas as pd
from db_connector import get_connection

# EXTRACT
# Load the raw data
raw_data_path = "data/raw/Online_Retail.xlsx"
data = pd.read_excel(raw_data_path)

# TRANSFORM
# Clean and preprocess the data
data = data.dropna(subset=["CustomerID", "Description"])
data["TotalAmount"] = data["Quantity"] * data["UnitPrice"]


data['InvoiceNo'] = data['InvoiceNo'].astype(str)
data['StockCode'] = data['StockCode'].astype(str)
data['Description'] = data['Description'].str.strip()
data['Quantity'] = data['Quantity'].astype(int)
data['UnitPrice'] = data['UnitPrice'].round(2)
data['CustomerID'] = data['CustomerID'].astype('Int64') 
data['Country'] = data['Country'].str.strip()
data['TotalAmount'] = (data['Quantity'] * data['UnitPrice']).round(2)

print(data.dtypes)
print(data.head())

# Save cleaned data 
data.to_csv("data/processed/cleaned_data.csv", index=False)


# Connect to the database
conn = get_connection()
cursor = conn.cursor()

# LOAD
# Insert data into Products table
products = data[['StockCode', 'Description', 'UnitPrice']].drop_duplicates(subset=['StockCode'])
for _, row in products.iterrows():
    cursor.execute(
        """
        INSERT INTO Products (product_id, product_name, unit_price)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            product_name = VALUES(product_name),
            unit_price = VALUES(unit_price)
        """,
        (row['StockCode'], row['Description'], row['UnitPrice'])
    )

# Insert data into Customers table
customers = data[['CustomerID', 'Country']].drop_duplicates(subset=['CustomerID'])
for _, row in customers.iterrows():
    cursor.execute(
        """
        INSERT INTO Customers (customer_id, country)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE
            country = VALUES(country)
        """,
        (row['CustomerID'], row['Country'])
    )

# Insert data into Orders table
orders = data[['InvoiceNo', 'CustomerID', 'InvoiceDate']].drop_duplicates(subset=['InvoiceNo'])
for _, row in orders.iterrows():
    cursor.execute(
        """
        INSERT INTO Orders (order_id, customer_id, order_date)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            customer_id = VALUES(customer_id),
            order_date = VALUES(order_date)
        """,
        (row['InvoiceNo'], row['CustomerID'], row['InvoiceDate'])
    )

# Insert data into OrderDetails table
for _, row in data.iterrows():
    cursor.execute(
        """
        INSERT INTO OrderDetails (order_id, product_id, quantity, total_amount)
        VALUES (%s, %s, %s, %s)
        """,
        (row["InvoiceNo"], row["StockCode"], row["Quantity"], row["TotalAmount"])
    )

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully into all tables!")


