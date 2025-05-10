# Main execution
if _name_ == "_main_":
    product_name = input("Enter the product you want to get the details of: ")
    
    flipkart_results = fetch_flipkart_data(product_name)
    amazon_results = fetch_amazon_data(product_name)

    # Display results
    if flipkart_results:
        flipkart_product = flipkart_results[0]  # Assuming you want the first match
        print(f"\nFlipkart: {flipkart_product['Product']} - Price: ₹{flipkart_product['Price']}")
    else:
        print("No results found on Flipkart.")
    
    if amazon_results:
        amazon_product = amazon_results[0]  # Assuming you want the first match
        print(f"Amazon: {amazon_product['Product']} - Price: ₹{amazon_product['Price']}")
    else:
        print("No results found on Amazon.")

    # Calculate and display the price difference
    if flipkart_results and amazon_results:
        flipkart_price = flipkart_product['Price']
        amazon_price = amazon_product['Price']
        price_difference = abs(flipkart_price - amazon_price)
        
        if flipkart_price > amazon_price:
            cheaper_platform = "Amazon"
        else:
            cheaper_platform = "Flipkart"
        
        print(f"\nPrice Difference: ₹{price_difference}")
        print(f"{cheaper_platform} has the lower price.")
