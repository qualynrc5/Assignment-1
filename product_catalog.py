from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
]

print("Products available:")
for product in products:
    print(product)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

while True:
    preference = input("Input a preference: ")
    customer_preferences.append(preference)
    
    response = input("Do you want to add another preference? (Y/N): ").strip().upper()
    if response == "N":
        break


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons
converted_products = []
for product in products:
    converted_products.append({"name": product["name"], "tags": set(product["tags"])})


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append({"name": product["name"], "matches": matches})
    return sorted(recommendations, key=lambda x: x["matches"], reverse=True)


# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_tags)
print("\nRecommended products based on your preferences:")
for item in results:
    print(f"{item['name']} ({item['matches']} match(es))")


