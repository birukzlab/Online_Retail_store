# Online Retail Data Analysis Project

This project involves processing and analyzing e-commerce transaction data from the UCI Machine Learning Repository. The primary goal is to clean, transform, and load the data into a MySQL database, enabling efficient querying and visualization of insights such as top-selling products and customer behavior.

Project Overview

## Dataset:

* Source: UCI Machine Learning Repository.

    * Contains transaction details such as:

    * InvoiceNo: Unique order ID.

    * StockCode: Product code.

    * Description: Product name.

    * Quantity: Number of items purchased.

    * InvoiceDate: Purchase date and time.

    * UnitPrice: Price per unit.

    * CustomerID: Unique customer identifier.

    * Country: Customer’s country.


## Objective:

Transform raw data into a structured relational database format.
Enable analysis of sales trends, customer patterns, and product performance.
Steps

## Data Cleaning:

Removed duplicates and handled missing values.
Converted data types to align with the database schema.
Calculated additional metrics like TotalAmount (Quantity × UnitPrice).


## Database Setup:

Created a MySQL database with four main tables:
Products
Customers
Orders
OrderDetails

Established relationships between tables for efficient querying.


## ETL Process:

Used Python scripts to extract, clean, and load the data into the database.
Handled errors like duplicate entries and type mismatches.
Querying and Visualization:
Wrote SQL queries to analyze sales trends and customer behavior.
Visualized key insights using Python (e.g., matplotlib) and BI tools like Tableau.


## Setup Instructions

1. Clone the Repository

* git clone https://github.com/birukzlab/Online_Retail_store.git

2. Install Dependencies

* pip install -r requirements.txt

3. Run the ETL Script

* python scripts/etl.py

4. Analyze Data

Use the SQL queries in the sql/ folder for analysis.
Optionally, connect the MySQL database to Tableau for interactive dashboards.

## Technologies Used

Programming: Python (Pandas, MySQL Connector, Matplotlib)
Database: MySQL
Visualization: Matplotlib


## Future Enhancements

Automate the ETL process for continuous data updates.
Build predictive models for sales forecasting and customer churn.


## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Contact

For questions or contributions, feel free to reach out via GitHub Issues.