# About the Project

## Project Goals

The goal of this project is to perform data analysis to identify .


## Project Description

A home is often the largest and most expensive purchase a person makes in his or her lifetime. Ensuring homeowners have a trusted way to monitor this asset is incredibly important. One considers several aspects while purchasing a home, the size, how many rooms are available, and many more.

Zillow is a popular estimator for house evaluation available online.  Zillow's Zestimate allows the homebuyers to search for a home that satisfies their location, area, budget, etc.

In this project we want to uncover what the drivers of the error are in Zillow's Zestimate. The focus will be the single unit properties that had a transaction during 2017.


### Initial Questions

- Is there a relationship between logerror and longitude and latitude?

- What is the relationship between What is the relationship between bedroom count and logerror?
    
- What is the relationship between square feet and logerror?

- How different are the logerrors for the three counties in the dataset?


### Data Dictionary

| Variable            |     Description     |     
| ----------------    | ------------------  |
|order_id          | Order ID of sale at give date                |
|order_date           | Date of order placed by custoemr                | 
|ship_date             | Shipment date by Superstore                |
|ship_mode            | Shipment method to customer                |
|customer_id    | Customer individual ID                |
|customer_name           | Customer name                |
|segment          | Type of customer                |
|city              | Customer's city                |
|state            | Customer's state                |
|postal_code| Customer's zip code                |
|region    | Customer's region                |
|product_id| Individual product ID                |
|category            | Type of product sold                |
|subcategory   | A sub-type of product sold, more specific than category                |
|product_name             | Name of product sold                |
|sales               | Sales made by order, target variable                |




## Steps to Reproduce

- Store (download/pull) the contents of this repository and save them to your hard-drive.
- Libraries used are pandas, matplotlib, seaborn, numpy, sklearn, datetime, geopandas, plotly and statsmodels.
- Follow along the report notebook for a concise representation of the report or feel free to refer to the WIP file for a scratchpad of the report as it was being analyzed.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

### Plan

Wrangle- Prepare - Explore - Model - Deliver

- Wrangle
    - Acquire dataset from repository and follow along the notebook to prepare the dataset for analyis
- Explore
    - Create visualizations of data to pin point areas of interest in relation to sales
    - Exploration through various features such as segment, state, product category and subcategory provide good visuals
- Analysis
    - Ensure the dataset is ready for forecasting by ensuring the index is the appropriate data type
    - train, validate and test split accordingly, and preferably manually.
- Delivery
    - Final Report in Jupyter Notebook
    - README with project details
    - Python wrangle functions

### Conclusions, Takeaways and Next Steps

 - After performing different models, the model with the lowest RMSE was the 104d moving average model with a score of 2112.
 - As we can see through the visualizations, total sales are going up but average sales are slightly decreasing. 
 - Most popular product category is office supplies with over 60%.
 - The top three products in each category are as follows:
     - office supplies: binders, paper, storage
     - furniture: furnishings, chairs, tables
     - technology: phones, accessories, machines
 - Products with highest sales by category:
     - OS: storage - 219K, binders - 200K, and appliances - 105K
     - F: chairs - 322K, tables - 203K, bookcases - 114K
     - T: phones - 328K, machines - 189K, accesories: 164K
 - When looking at sales by category:
     - Office Supplies: follows overall sales trends however, it looks like office supplies are generally bought toward the end of the year
     - furniture: average sales are in decline, there is an uptick in sales at the end of the year
     - technology: sales by year are going up, average sales have a downward trend
- Sales are generated only in continental US, with the exception of Alaska.
     - Hawaii and Alaska do not generate sales for the company
     - District of Columbia does generate sales for the company
 - States with highest sales are:
     - CA, NY, TX, WA, and PA
 - States with lowest sales are:
     - WY, SD, ME, WV, ND
 - Regions east and west make up the majority of sales:
     - central: 492K
     - east: 670K
     - south: 389K
     - west: 710K
 - There are three segments:
     - consumer: biggest segment at 1,148K sales or 50.76% of their customers
     - corporate: second biggest segment at 688K or 30.44% of their customers
     - home office: third biggest segment at 425K or 18.79% of their customers
     
Next Steps

 - With more time, it'd be interesting to look into the reason average sales are on decline (although the decline is small)
 - Analyze if there to see if the remaining categorical variables show anything interesting in relation to sales:
     - in this case, postal_code, customer ID (to identify key customers), etc.
 - Play around further with predicing sales.
 - Drop unnecessary columns (customer id, city, order id, ship date, customer name) and take those categorical variables and encode them into booleans and perform a regresion analysis.
