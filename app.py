import streamlit as st
from streamlit_option_menu import option_menu

#with st.sidebar:
selected = option_menu(
        menu_title="Raymond Sekgobela's Portfolio Projects",
        options=["Analysis","Visualization","Machine Learning"],
        icons=["bar-chart-line","pie-chart","diagram-3"],
        menu_icon="person",
        default_index=0,
        orientation="horizontal",
    )
    
if selected == "Analysis":
    st.title(f"Data analysis projects.")
    project_type = ["- Select Project Type -","Analysis Reports -- Summery","Detailed Analysis -- With Code"]
project_selected = st.selectbox("Please select a project type below", options=project_type)
if project_selected == "Analysis Reports -- Summery":
    project_name = ["- Select Project Title -","Exploratory Data Analysis of Employee Attrition","Marketing Campaign Analysis Report","Product Analysis Report"]
    title_selected = st.selectbox("Please select a project title below", options=project_name)
    if title_selected == "Exploratory Data Analysis of Employee Attrition":
        st.write("""
        Title: Exploratory Data Analysis of Employee Attrition

Introduction:

The goal of this EDA is to understand the factors that contribute to employee attrition at XYZ company. The dataset used in this analysis includes information on employee characteristics such as age, gender, job role, salary, and performance.

Data Summary:

The dataset contains 1,000 records and 13 variables. The variables include:

Employee ID: a unique identifier for each employee
Age: the age of the employee
Gender: the gender of the employee (male or female)
Job Role: the job role of the employee (e.g. manager, developer, analyst)
Salary: the salary of the employee
Performance: the performance rating of the employee (on a scale of 1-5)
Attrition: whether the employee left the company (yes or no)
Data Cleaning and Preprocessing:

Before analyzing the data, we performed the following steps:

Checked for missing values: There were no missing values in the dataset.
Checked for duplicate records: There were no duplicate records in the dataset.
Checked for outliers: We identified and removed two records with outlier salary values.
Exploratory Data Analysis:

We first looked at the distribution of employee ages. The average age was 37 years old, with a standard deviation of 9 years. The distribution was slightly skewed to the right, with a long tail of employees in their 40s and 50s.

Next, we explored the relationship between employee characteristics and attrition. We found that:

Employees with lower salaries were more likely to leave the company.
Employees with lower performance ratings were more likely to leave the company.
There was no significant difference in attrition rates between male and female employees.
Finally, we looked at the relationship between job role and attrition. We found that employees in certain job roles (e.g. sales, technical) had higher attrition rates compared to others (e.g. research and development).

Conclusion:

This EDA has provided us with insights into the factors that contribute to employee attrition at XYZ company. We found that salary and performance are strong predictors of attrition, and that certain job roles are more prone to high attrition rates. These findings can inform future retention efforts at the company.
        """)

    if title_selected == "Marketing Campaign Analysis Report":
        st.header("Marketing Campaign Analysis Report")
        st.subheader("Executive Summary:")
        st.write("""
        



The purpose of this report is to provide an analysis of our recent marketing campaign for our new product launch. The campaign was designed to increase awareness and drive sales of the new product. The campaign ran for a period of six weeks and included a combination of online and offline marketing activities such as social media advertising, email marketing, and in-store promotions.
""")

        st.subheader("Key Findings:")
        st.write("""
        
The campaign was successful in increasing brand awareness, as indicated by a 10% increase in website traffic and a 15% increase in social media followers.
The campaign generated a total of 500 sales, exceeding our sales target by 25%.
The email marketing campaign had the highest conversion rate, with a 10% click-through rate and a 5% conversion rate.
The in-store promotions were less effective, with a 5% conversion rate.
""")
        st.subheader("Recommendations:")
        st.write("""
Based on the success of the email marketing campaign, we recommend increasing the budget for this channel in future campaigns.
We recommend testing different types of in-store promotions to improve conversion rates in this channel.
We recommend collecting and analyzing customer feedback to identify areas for improvement in future campaigns.
""")
        st.subheader("Conclusion:")
        st.write("""

Overall, the marketing campaign was successful in increasing brand awareness and driving sales. However, there is room for improvement in certain channels, and we recommend implementing the above recommendations to optimize future campaigns.
        """)
    if title_selected == "Product Analysis Report":
        st.write("""
        Title: Product Analysis Report

Executive Summary:

The purpose of this report is to provide an analysis of our new product, the XYZ widget. The report includes an overview of the product, a market analysis, and a financial analysis.

Product Overview:

The XYZ widget is a small, portable device that allows users to access the internet on the go. It has a sleek design, a long battery life, and is compatible with multiple devices.

Market Analysis:

The market for portable internet devices is growing, with an expected annual growth rate of 5%. The XYZ widget is well-positioned to capture a significant share of this market due to its unique features and competitive pricing.

Financial Analysis:

The XYZ widget has a projected gross margin of 30%. Based on projected sales volumes and pricing, we expect the product to generate $500,000 in net income over the first year.

Conclusion:

Overall, the XYZ widget is a promising new product with strong market potential and favorable financial projections. We recommend proceeding with the launch of the product and conducting ongoing market and financial analysis to optimize performance.
        """)






if selected == "Visualization":
    st.title(f"Data visualization projects.")
if selected == "Machine Learning":
    st.title(f"Machine learning projects.")