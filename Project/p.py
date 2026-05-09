import requests

def convert_currency(api_key, base_currency, target_currency, amount):
    # The URL for the API request
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}"

    try:
        # Making the 'GET' request (Like a browser fetching a page)
        response = requests.get(url)
        
        # In C++, you'd check status codes manually. Here:
        response.raise_for_status() 

        # Convert the JSON response into a Python Dictionary (std::map style)
        data = response.json()

        if data['result'] == 'success':
            converted_amount = data['conversion_result']
            rate = data['conversion_rate']
            
            print("-" * 30)
            print(f"Base: {amount} {base_currency}")
            print(f"Target: {converted_amount:.2f} {target_currency}")
            print(f"Exchange Rate: 1 {base_currency} = {rate} {target_currency}")
            print("-" * 30)
        else:
            print("Error: API request failed.")

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")

if __name__ == "__main__":
    # --- CONFIGURATION ---
    # Replace 'YOUR_API_KEY_HERE' with the key from the website
    MY_API_KEY = "aecb39f0f86ec6323ab1000f"
    
    print("=== Real-Time Currency Converter ===")
    
    # Input handling
    base = input("Enter base currency (e.g., USD, PKR): ").upper()
    target = input("Enter target currency (e.g., EUR, GBP): ").upper()
    
    try:
        qty = float(input(f"Enter amount in {base}: "))
        convert_currency(MY_API_KEY, base, target, qty)
    except ValueError:
        print("Invalid input. Please enter a numerical amount.")