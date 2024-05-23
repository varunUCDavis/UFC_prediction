import streamlit as st
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

    predictor = UFCModelPredictor(file_path='finalufcdataset.csv')
    predictor.load_and_prepare_data()

    # Fighter selection
    fighters = predictor.fighters
    fighter_names = [f'Fighter {i+1}' for i in range(len(fighters))]

    col1, col2 = st.columns(2)

    with col1:
        fighter_r_index = st.selectbox("Select Red Fighter", options=range(len(fighter_names)), format_func=lambda x: fighter_names[x])
        fighter_r = fighters.iloc[fighter_r_index].values[:15].tolist()
        #st.image('path/to/red_fighter_image.jpg')  # Replace with actual image path

        st.write("Adjust Red Fighter's Attributes")
        for i, attr in enumerate(fighter_r):
            if isinstance(attr, (int, float)):
                fighter_r[i] = st.slider(f'Attribute {i+1}', min_value=0, max_value=100, value=int(attr))

    with col2:
        fighter_b_index = st.selectbox("Select Blue Fighter", options=range(len(fighter_names)), format_func=lambda x: fighter_names[x])
        fighter_b = fighters.iloc[fighter_b_index].values[15:].tolist()
        #st.image('path/to/blue_fighter_image.jpg')  # Replace with actual image path

        st.write("Adjust Blue Fighter's Attributes")
        for i, attr in enumerate(fighter_b):
            if isinstance(attr, (int, float)):
                fighter_b[i] = st.slider(f'Attribute {i+1}', min_value=0, max_value=100, value=int(attr))

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