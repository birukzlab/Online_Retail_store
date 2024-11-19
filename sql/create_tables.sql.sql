-- create database and tables
CREATE DATABASE online_retail;
USE online_retail;

-- Products
CREATE TABLE Products (
    product_id VARCHAR(20) PRIMARY KEY,       
    product_name VARCHAR(255) NOT NULL,      
    unit_price DECIMAL(10, 2) NOT NULL        
);

--  Customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,             
    country VARCHAR(50) NOT NULL              
);


-- Orders
CREATE TABLE Orders (
    order_id VARCHAR(20) PRIMARY KEY,         
    customer_id INT,                         
    order_date DATETIME NOT NULL,             
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);


-- Order Details
CREATE TABLE OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id VARCHAR(20),                    
    product_id VARCHAR(20),                  
    quantity INT NOT NULL,                    
    total_amount DECIMAL(10, 2) NOT NULL,     
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Test
SELECT * from Customers;

SELECT COUNT(*) FROM Products;
SELECT COUNT(*) FROM Customers;
SELECT COUNT(*) FROM Orders;
SELECT COUNT(*) FROM OrderDetails;









