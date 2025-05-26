# A script will ask the user about the current weather conditions
# and provide clothing recommendations based on the input

current_weather = input("What's the weather like today? (sunny/rainy/cold):")

if current_weather == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")
