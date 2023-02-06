# dictionary of different skin types and corresponding recommended products
skin_types = {
    "oily": ["oil-free moisturizer", "mattifying primer", "clay mask"],
    "dry": ["hydrating moisturizer", "serum with hyaluronic acid", "sheet mask"],
    "combination": ["lightweight moisturizer", "tinted moisturizer with SPF", "exfoliating scrub"],
    "sensitive": ["gentle cleanser", "soothing face mist", " fragrance-free moisturizer"],
    "acne-prone": ["salicylic acid cleanser", "benzoyl peroxide spot treatment", "non-comedogenic moisturizer"]
}

# dictionary of different skin problems and corresponding recommended products
skin_problems = {
    "wrinkles": ["retinol serum", "anti-aging cream", "face roller"],
    "dull skin": ["brightening serum", "face mask with Vitamin C", "exfoliating scrub"],
    "dark spots": ["Vitamin C serum", "glycolic acid peel", "brightening moisturizer"],
    "uneven skin tone": ["lightening serum", "BB cream with color correction", "face primer"],
    "redness": ["green tinted moisturizer", "soothing face mist", "cica cream"]
}


# function to recommend products based on skin type and skin problems
def recommend_products(skin_type, skin_problem):
    print("Based on your skin type '{}' and skin problem '{}', here are our recommendations:".format(skin_type,
                                                                                                     skin_problem))
    print("Products for skin type:", skin_types[skin_type])
    print("Products for skin problem:", skin_problems[skin_problem])


while True:
    # get user inputs
    user_skin_type = input("Enter your skin type (oily, dry, combination, sensitive, acne-prone): ").lower()
    if user_skin_type not in skin_types:
        print("Invalid skin type. Please enter a valid skin type.")
        continue

    user_skin_problem = input("Enter your skin problem (wrinkles, dull skin, dark spots, uneven skin tone, redness): ").lower()
    if user_skin_problem not in skin_problems:
        print("Invalid skin problem. Please enter a valid skin problem.")
        continue

    # call the recommendation function
    recommend_products(user_skin_type, user_skin_problem)
    break
