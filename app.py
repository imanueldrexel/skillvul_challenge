# Import the necessary libraries
# streamlit for creating the web app
# pickle for loading the pre-calculated recommendations
import streamlit as st
import pickle

# Load the pre-calculated recommendations from a pickle file
# The pickle file contains a matrix where each row corresponds to a customer
# and each column corresponds to a product. The value in each cell is the 
# predicted rating that the customer would give to the product.
pre_calculated_matrix = pickle.load(open('recommendations.pkl', 'rb'))

# Define the function to generate recommendations for a given customer
def generate_recommendation(customer_id):
    # Get the recommendations for the given customer
    # The customer_id is subtracted by 1 because Python uses zero-based indexing
    recommendation = pre_calculated_matrix[customer_id-1]
    
    # Loop through the recommendations and print each one
    # The enumerate function is used to get both the index and the value in the loop
    for idx, x in enumerate(recommendation):
        # Print the recommendation with its corresponding number
        # The index is incremented by 1 because Python uses zero-based indexing
        st.write(f'The Recommendation Number {idx}: {x[0]} With Category {x[1]}')

# Create a Streamlit app
st.title('Recommendation App')

# Get the customer id from the user
# The number input widget is used to get a number input from the user
# The min_value, max_value, value, and step parameters are used to control the range and increment of the input
input_number = st.number_input('Enter Customer ID', min_value=1, max_value=11824, value=1, step=1, format='%d')

# Call the generate_recommendation function with the user's input
# The result is printed in the Streamlit app
generate_recommendation(input_number)