# Import necessary libraries
# pandas for data manipulation
# pickle for serializing and de-serializing Python object structures
# numpy for numerical operations
# sklearn.metrics.pairwise for calculating cosine similarity
# sklearn.feature_extraction.text for converting collection of text documents to a matrix of token counts
# sklearn.neighbors for unsupervised neighbors-based learning methods

import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# Load the customer interactions, product details, and purchase history data
customer_interactions = pd.read_csv('customer_interactions_dummy.csv', delimiter=",")
product_details = pd.read_csv('product_details_dummy.csv', delimiter=";")
purchase_history = pd.read_csv('purchase_history_dummy.csv', delimiter=";")

# Remove duplicates from the data
customer_interactions = customer_interactions.drop_duplicates()
product_details = product_details.drop_duplicates()
purchase_history = purchase_history.drop_duplicates()

# Merge the purchase history and product details data on the 'product_id' column
purchase_history = purchase_history.merge(product_details, on='product_id', how='left')

# Create a pivot table from the purchase history data
# The pivot table has customers as rows, products and categories as columns, and the size of each group as values
interaction_matrix = purchase_history.pivot_table(index='customer_id', 
                                                  columns=['product_id', 'category'], 
                                                  aggfunc='size', 
                                                  fill_value=0)

# Fit a NearestNeighbors model on the pivot table
# The model uses cosine similarity as the distance metric and brute force search as the algorithm
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(interaction_matrix)

# For each customer, find the 100 nearest neighbors in the interaction matrix
distances, indices = model.kneighbors(interaction_matrix, n_neighbors=100)

# For each customer, recommend the products that the nearest neighbors have purchased but the target customer has not
recommendations = []
for idx, customer_id in enumerate(list(interaction_matrix.index)):
    record = interaction_matrix.iloc[idx].values
    neighbors = indices[idx][1:]
    neighbor_records = interaction_matrix.iloc[neighbors].values
    recommended_products = (neighbor_records.sum(axis=0) - record).argsort()[-5:][::-1]
    recommendations.append([interaction_matrix.columns[i] for i in recommended_products])

# If the script is run as the main module, serialize the recommendations to a pickle file
if __name__ == '__main__':
    pickle.dump(recommendations, open('recommendations_2.pkl', 'wb'))