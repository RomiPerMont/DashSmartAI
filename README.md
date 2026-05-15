# DashSmartAI
AI-Driven Predictive Analytics System for Logistics Operations and Delivery Delay Monitoring  


## Project overview  

This project focuses on the design and development of an AI driven predictive analytics system for logistics operations and delivery delay monitoring.  
The system is a web-based dashboard that allows users to upload logistics datasets in CSV format and generate insights through data visualization and predictive analytics.  
The main goal of this project is to support data driven decision making by transforming raw logistics data into meaningful information that can help identify inefficiencies and predict potential delays.  


## Core features implemented (MVP)  

The current MVP includes the following core features:  

- Upload logistics data in CSV format  
- Automatic data reading and preparation  
- Display of dataset preview  
- Basic dataset analysis 
- Initial dashboard structure using Streamlit  

These features represent the foundation of the system and will be extended in future development stages.  


## System flow  

The system follows a simple process:  

1. User opens the application  
2. User uploads a CSV file  
3. System validates and reads the file  
4. Data is processed and prepared  
5. Results are displayed to the user  

This flow ensures the system is easy to use and follows a clear structure for both technical and non technical users.  



## Objectives  

The objectives of this project are:  

- To design and develop a web based logistics analytics dashboard  
- To allow users to upload logistics data in CSV format  
- To clean and process the uploaded data automatically  
- To create clear and interactive visualizations  
- To develop a machine learning model to predict delivery delays  
- To integrate data processing, visualization and prediction into one system  


## Key features  

- Data upload  
- Data cleaning and processing  
- Data visualization  
- KPI dashboard including on time delivery rate and average delay  
- Predictive delay model  
- Export of results  
- User friendly interface  


## Technologies used  

The system is developed using the following technologies:  

- Python  
- Streamlit  
- Pandas  
- Plotly  
- Scikit-learn
- Matplotlib

## How to run the system  

1. Clone the repository  

git clone https://github.com/RomiPerMont/DashSmartAI.git
cd DashSmartAI

2. Install the required libraries  

pip install -r requirements.txt

3. Run the application  

streamlit run app.py
