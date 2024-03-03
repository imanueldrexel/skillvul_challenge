# Import necessary libraries
# pandas for data manipulation
# numpy for numerical operations

import pandas as pd
import numpy as np

# Define the number of interactions, unique customers, purchase events, unique products, and categories
number_of_interactions = 1e6
number_of_unique_customers = 11824
number_of_purchase_events = 200000
number_of_unique_products = 10000
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Beauty']

# Generate random data for each column in the purchase history
customer_id = np.random.randint(1, number_of_unique_customers+1, number_of_purchase_events)
product_id = np.random.randint(1, number_of_unique_products+1, number_of_purchase_events)
purchase_date_range = pd.date_range(start='2023-01-01', end='2023-12-31').to_series()
purchase_date = np.random.choice(purchase_date_range.dt.strftime('%Y-%m-%d'), number_of_purchase_events)

# Create a DataFrame for the purchase history
purchase_history_dummy = pd.DataFrame({
    'customer_id': customer_id,
    'product_id': product_id,
    'purchase_date': purchase_date
})

# Generate random data for each column in the customer interactions
customer_interactions = purchase_history_dummy[['customer_id','purchase_date']].drop_duplicates()
customer_interactions_dummy = pd.DataFrame()
customer_interactions_dummy['customer_id'] = np.concatenate((customer_interactions['customer_id'], np.random.randint(1, number_of_unique_customers+1, int(number_of_interactions - customer_interactions.shape[0]))))
customer_interactions_dummy['visiting_date'] = np.concatenate((customer_interactions['purchase_date'], np.random.choice(purchase_date_range.dt.strftime('%Y-%m-%d'), int(number_of_interactions - customer_interactions.shape[0]))))
customer_interactions_dummy['page_view'] = np.random.randint(1, 30, int(number_of_interactions))
customer_interactions_dummy['time_spent_in_minute'] = np.random.randint(1, 120, int(number_of_interactions))

# Generate random data for each column in the product details
product_id = np.arange(1, number_of_unique_products + 1)
category = np.random.choice(categories, number_of_unique_products)
price = np.random.randint(10, 1000, number_of_unique_products)
ratings = np.round(np.random.uniform(1.0, 5.0, number_of_unique_products), 1)

# Create a DataFrame for the product details
product_details_dummy = pd.DataFrame({
    'product_id': product_id,
    'category': category,
    'price': price,
    'ratings': ratings
})

# Write the DataFrames to CSV files
product_details_dummy.to_csv('product_details_dummy.csv', sep=';', index=False)
customer_interactions_dummy.to_csv('customer_interactions_dummy.csv', sep=";",index=False)
purchase_history_dummy.to_csv('purchase_history_dummy.csv', sep=';', index=False)