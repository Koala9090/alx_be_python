weather = input("What's the weather like today? (sunny/rainy/cold):")
if weather == "sunny".lower():
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy".lower() :
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold".lower() :
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
