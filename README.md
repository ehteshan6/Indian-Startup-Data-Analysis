🚀 Indian Startup Funding Dashboard

An interactive data analysis dashboard built using Streamlit and Plotly to explore insights from the Indian startup ecosystem (2015–2017). This project helps identify funding trends, top industries, active cities, and leading investors.

📊 Key Features

Year-wise filtering (2015, 2016, 2017)

Visualize total funding trends over time

Top 10 most funded industries

Top cities with the highest funding received

Top investors based on amount funded

KPIs: Total Funding, Total Deals, Unique Startups

📁 Dataset Information

The dataset includes funding details of Indian startups between 2015 and 2017.

Column Name - Description
Date - Date of funding
Startup Name - Name of the startup
Industry Vertical - Industry sector of the startup
SubVertical - Sub-sector within the main industry
City Location - City where the startup is based
Investors Name - Name(s) of investor(s)
Investment Type - Type of investment (e.g., Seed, Series A, etc.)
Amount in USD - Total funding amount in US dollars
Remarks - Additional remarks if any

🛠️ Tech Stack

Python

Pandas

Plotly (for interactive charts)

Streamlit (for building the dashboard)

Jupyter Notebook (for initial EDA and preprocessing)

🖥️ How to Run Locally

Clone the repository or download the code files.

Open your terminal and navigate to the project directory.

Install the required packages:

pip install streamlit pandas plotly

Launch the Streamlit app:

streamlit run app.py

📌 Folder Structure

indian-startup-funding/
│
├── data/
│ └── cleaned_startup.csv
│
├── app.py
├── README.txt
└── requirements.txt

🙋 Author

Ehteshan Alam
Aspiring Data Analyst & BI Developer
LinkedIn: https://www.linkedin.com/in/your-profile
Email: ehteshanalam1@gmail.com

✅ Future Scope

Add machine learning model to predict funding amount

Recommend investors based on startup profile

Add monthly and quarterly analysis

Host the dashboard using Streamlit Cloud
