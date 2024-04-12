#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("C:/Users/LENOVO/OneDrive - ss.z/Desktop/SEC EDGAR.csv")


# In[3]:


df


# In[4]:


df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100


# In[5]:


df


# In[6]:


df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100


# In[7]:


df['Net Worth'] = df['Total Assets']-df['Total Liabilities']


# In[8]:


df


# In[9]:


df.fillna(0,inplace= True)


# In[10]:


df


# In[11]:


summary = df.groupby('Company').agg({
   'Revenue Growth (%)' : 'mean',
    'Cash Flow from Operating Activities' : 'mean',
    'Net Income Growth (%)' : 'mean',
    'Net Worth':'mean'
}).reset_index()


# In[12]:


summary


# In[13]:


print('Average growth rates - Year wise')
summary


# In[14]:


summary.to_csv('Summary_report.csv')


# In[15]:


get_ipython().run_line_magic('pwd', '')


# In[16]:


df.to_csv('final_report.csv')


# In[20]:


final_report = pd.read_csv('final_report.csv')


# In[21]:


def financial_chatbot():
    print("\nPlease enter your query")
    user_query = input()

    if user_query == "What is the total revenue?":
        revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Total Revenue'].values[0]
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
    elif user_query == "What is the Net Income?":
        net_income  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income'].values[0]
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"

    
    elif user_query == "What is cash flow from operating activities?":
        cash_ops = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
        return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
    
    elif user_query == "What is the revenue growth(%) ?":
        revenue_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
    
    elif user_query == "What is the net income growth(%) ?":
        net_income_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
    
    elif user_query == "What is the assets growth(%) ?":
        assets_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"

    
    elif user_query == "What is the cash flow from operations growth(%) ?":
        cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_ops_growth}(%)"
    
    else:
        return "Sorry, I cannot only provide information on the requested query."


# In[22]:


# Test the chatbot
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter Hi to start the chatbot session; type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "hi":
        print("\nHello! Welcome to AI Driven Financial Chatbot!!!")
        print("\nI can help you with your financial queries")
        print("Please select the company name from below: -")
        print("\n1.Microsoft \n2.Tesla \n3.Apple")
        company_input = input("Enter company name : ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter correct company name by starting the chatbot session again")
            break
        else:
            print("\nThe data for the fiscal year 2023, 2022, and 2021 is currently available")
            fiscal_year = int(input("The fiscal year for the selected company : "))
            if fiscal_year not in [2023, 2022, 2021]:
                print("Please enter a valid fiscal year by starting the chatbot session again")
                break
    else:
        print("Enter 'Hi' Properly!!!!! by starting the chatbot session again")
        break
            
        
    response = financial_chatbot()
    print(response)


# In[ ]:




