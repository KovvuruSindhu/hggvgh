# recipe_finder.py
# Simple web app to find meals using ingredients.
# Author: Kovvuru Sindhu

import streamlit as st
import requests

# App title
st.title("🍽️ Taylor's Recipe Finder")
st.write("Find delicious meals based on ingredients you have!")

# User input
ingredient = st.text_input("Enter an ingredient (e.g., chicken, egg, tomato):")

# When user clicks the button
if st.button("Find Recipes"):
    if ingredient.strip() == "":
        st.warning("⚠️ Please enter an ingredient to search for recipes.")
    else:
        # API endpoint
        api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
        
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
            data = response.json()

            # If meals found
            if data["meals"]:
                st.success(f"🍳 Here are some recipes with '{ingredient}':")
                for meal in data["meals"]:
                    st.image(meal["strMealThumb"], width=250)
                    st.subheader(meal["strMeal"])
                    meal_url = f"https://www.themealdb.com/meal.php?c={meal['idMeal']}"
                    st.markdown(f"[👉 View Full Recipe]({meal_url})")
                    st.markdown("---")
            else:
                st.error(f"❌ No recipes found for '{ingredient}'. Try another ingredient.")
        except requests.exceptions.RequestException as e:
            st.error(f"Network error: {e}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
