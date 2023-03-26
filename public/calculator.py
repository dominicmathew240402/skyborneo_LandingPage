# Define the pricing model
PRICE_PER_REQUEST = 0.10  # Price per API request in USD
TOKENS_PER_REQUEST = 10  # Number of tokens consumed per API request

# Define the user's token usage
num_tokens = int(input("Enter the number of tokens used: "))

# Calculate the number of API requests
num_requests = num_tokens / TOKENS_PER_REQUEST

# Calculate the total price in USD
price_usd = num_requests * PRICE_PER_REQUEST

# Convert the price to MYR (assuming an exchange rate of 4.00 MYR per USD)
price_myr = price_usd * 4.00

# Display the results
print("Number of API requests:", num_requests)
print("Price in USD:", price_usd)
print("Price in MYR:", price_myr)
