# rebbus
Redbus Data Scraping and Analysis This project involves scraping bus travel data from Redbus, cleaning the data, storing it in a SQL database, and visualizing it through an interactive Streamlit dashboard. The objective is to provide a comprehensive tool for analyzing and filtering bus travel information.

Project Structure bus_routes.ipynb: Jupyter notebook for scraping bus route data. busdetails.ipynb: Jupyter notebook for scraping detailed bus information. data_cleaning.ipynb: Jupyter notebook for cleaning and preprocessing the scraped data. store_data_to_sql.py: Python script for storing cleaned data into a MySQL database. streamlit.py: Streamlit application for visualizing and interacting with the data. Installation Prerequisites Python 3.x: Ensure you have Python installed on your machine.

MySQL Server: Make sure MySQL Server is installed and running.

Required Python Libraries: Install the required libraries using pip.

pip install pandas selenium mysql-connector-python sqlalchemy streamlit ChromeDriver: Download and install ChromeDriver compatible with your Chrome version.

Setting Up Clone the Repository git clone <reposiRedbus Data Scraping and Analysis This project involves scraping bus travel data from Redbus, cleaning the data, storing it in a SQL database, and visualizing it through an interactive Streamlit dashboard. The objective is to provide a comprehensive tool for analyzing and filtering bus travel information.

Project Structure bus_routes.ipynb: Jupyter notebook for scraping bus route data. busdetails.ipynb: Jupyter notebook for scraping detailed bus information. data_cleaning.ipynb: Jupyter notebook for cleaning and preprocessing the scraped data. store_data_to_sql.py: Python script for storing cleaned data into a MySQL database. streamlit.py: Streamlit application for visualizing and interacting with the data. Installation Prerequisites Python 3.x: Ensure you have Python installed on your machine.

MySQL Server: Make sure MySQL Server is installed and running.

Required Python Libraries: Install the required libraries using pip.

pip install pandas selenium mysql-connector-python sqlalchemy streamlit ChromeDriver: Download and install ChromeDriver compatible with your Chrome version.

Setting Up Clone the Repository git clone cd Prepare the Database Ensure MySQL Server is running. Update store_data_to_sql.py with your database credentials. Create the database by running the store_data_to_sql.py script: python store_data_to_sql.py

Usage Data Scraping Run bus_routes.ipynb: This notebook scrapes the basic bus route information.

Run busdetails.ipynb: This notebook extracts detailed information for each bus route.

Data Cleaning Run data_cleaning.ipynb: This notebook cleans and preprocesses the data. Storing Data Run store_data_to_sql.py: This script loads the cleaned data into the MySQL database.

python store_data_to_sql.py Data Visualization Run streamlit.py: This script starts the Streamlit application.

streamlit run streamlit.py Visit http://localhost:8501 in your web browser to access the interactive dashboard.

Acknowledgments Selenium: For web scraping automation. Pandas: For data manipulation and analysis. MySQL: For relational database management. Streamlit: For interactive web applications. For any questions or feedback, please open an issue or contact the project maintainer.tory-url> cd Prepare the Database Ensure MySQL Server is running. Update store_data_to_sql.py with your database credentials. Create the database by running the store_data_to_sql.py script: python store_data_to_sql.py

Usage Data Scraping Run bus_routes.ipynb: This notebook scrapes the basic bus route information.

Run busdetails.ipynb: This notebook extracts detailed information for each bus route.

Data Cleaning Run data_cleaning.ipynb: This notebook cleans and preprocesses the data. Storing Data Run store_data_to_sql.py: This script loads the cleaned data into the MySQL database.

python store_data_to_sql.py Data Visualization Run streamlit.py: This script starts the Streamlit application.

streamlit run streamlit.py Visit http://localhost:8501 in your web browser to access the interactive dashboard.

Acknowledgments Selenium: For web scraping automation. Pandas: For data manipulation and analysis. MySQL: For relational database management. Streamlit: For interactive web applications. For any questions or feedback, please open an issue or contact the project maintainer.
