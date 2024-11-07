import streamlit as st

# Set a title for the app
st.title("Main Form App")

# Define options for the first dropdown
first_dropdown_options = {
    'Fruits': ['Apple', 'Banana', 'Cherry'],
    'Vegetables': ['Carrot', 'Lettuce', 'Tomato'],
    'Dairy': ['Milk', 'Cheese', 'Yogurt']
}

# Initialize session state for category and item selection
if 'category' not in st.session_state:
    st.session_state.category = None
if 'item' not in st.session_state:
    st.session_state.item = None

# First dropdown for selecting category
st.session_state.category = st.selectbox('Select a Category:', list(first_dropdown_options.keys()))

# Second dropdown updates based on the first dropdown selection
if st.session_state.category:
    st.session_state.item = st.selectbox('Select an Item:', first_dropdown_options[st.session_state.category])

# Submit button to navigate to `form_app.py`
if st.button('Submit'):
    # Mark form as submitted and navigate to `form_app.py`
    st.session_state.submitted = True
    st.experimental_rerun()
