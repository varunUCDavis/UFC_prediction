import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from model_page import UFCModelPredictor

def show_home():
    st.title("Home Page")
    st.write("Welcome to the UFC Prediction Tool!")

def show_model_page():
    st.title("UFC Prediction Tool 🥊")
    predictor = UFCModelPredictor(file_path='finalufcdataset.csv')
    predictor.load_and_prepare_data()
    predictor.test_models()

def show_prediction_page():
    st.title("Fight Prediction")

    fighter_names = [
        "B.J. Penn", "Royce Gracie", "Antonio Rodrigo Nogueira", "Dominick Cruz", "Max Holloway",
        "Junior Dos Santos", "Frankie Edgar", "Henry Cejudo", "Michael Bisping", "Randy Couture",
        "Kamaru Usman", "Alistair Overeem", "Dan Henderson", "Matt Hughes", "Chuck Liddell",
        "José Aldo", "Conor McGregor", "Israel Adesanya", "Khabib Nurmagomedov",
        "Demetrious Johnson", "Daniel Cormier", "Stipe Miocic", "Georges St-Pierre",
        "Jon Jones", "Anderson Silva"
    ]
    fighter_attributes = ["Height", "Weight", "Reach"]
    
    fighters = pd.DataFrame(fighter_names)
    attributes = pd.DataFrame(fighter_attributes)





    predictor = UFCModelPredictor(file_path='finalufcdataset.csv')
    predictor.load_and_prepare_data()

    # Fighter selection
    fighters = predictor.fighters

    col1, col2 = st.columns(2)

    with col1:
        fighter_r_name = st.selectbox("Select Red Fighter", options=fighter_names)
        fighter_r_index = fighter_names.index(fighter_r_name)
        fighter_r = fighters.iloc[fighter_r_index].values[:].tolist()

        st.write("Adjust Red Fighter's Attributes")
        for i, attr in enumerate(fighter_r):
            if isinstance(attr, (int, float)):
                if i < 3:
                    fighter_r[i] = st.slider(f'Attribute {fighter_attributes[i]}', min_value=0, max_value=100, value=int(attr))

    with col2:
        fighter_b_index = st.selectbox("Select Blue Fighter", options=range(len(fighter_names)), format_func=lambda x: fighter_names[x])
        fighter_b = fighters.iloc[fighter_b_index].values[15:].tolist()
        #st.image('path/to/blue_fighter_image.jpg')  # Replace with actual image path

        st.write("Adjust Blue Fighter's Attributes")
        for i, attr in enumerate(fighter_b):
            if isinstance(attr, (int, float)):
                if i < 3:
                    fighter_b[i] = st.slider(f'Attribute {fighter_attributes[i]}', min_value=0, max_value=100, value=int(attr), key=f'blue_{i}')

    if st.button('Predict Winner'):
        winner = predictor.predict_winner(fighter_r, fighter_b)
        st.write(f'The predicted winner is: {winner}')

def main():
    # Navigation bar
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Model Page", "Prediction"],  # required
        icons=["house", "bar-chart", "bullseye"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )

    if selected == "Home":
        show_home()
    elif selected == "Model Page":
        show_model_page()
    elif selected == "Prediction":
        show_prediction_page()

if __name__ == "__main__":
    main()