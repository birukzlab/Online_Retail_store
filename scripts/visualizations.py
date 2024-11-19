import pandas as pd
import matplotlib.pyplot as plt
from db_connector import get_connection

# Query the database
conn = get_connection()
query = "SELECT o.order_date, SUM(od.total_amount) AS revenue FROM Orders o INNER JOIN OrderDetails od USING(order_id) GROUP BY order_date"
data = pd.read_sql(query, conn)

# Plot revenue over time
plt.plot(data["order_date"], data["revenue"])
plt.title("Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

query = """
    SELECT P.product_name, SUM(OD.total_amount) AS total_revenue
    FROM OrderDetails OD
    JOIN Products P ON OD.product_id = P.product_id
    GROUP BY P.product_name
    ORDER BY total_revenue DESC
    LIMIT 10;
"""
data = pd.read_sql(query, conn)
conn.close()

# Plot the data
plt.bar(data['product_name'], data['total_revenue'])
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()


