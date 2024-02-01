#
# def handle_error(response):
#
#     if response.status_code == 400:
#         print(f"Bad Request Error - {response.status_code} - {str(response.json())}")
#
#     elif response.status_code == 500:
#         print(f"Internal Server Error - {response.status_code} - {str(response.json())}")
#
#     else:
#         print(f"An unexpected error occurred - {response.status_code} - {str(response.json())}")
#     return False

import json


def handle_error(response):
    # Check if the response content type is JSON
    if 'application/json' in response.headers.get('Content-Type', ''):
        try:
            # Attempt to parse the JSON response
            error_data = response.json()
            error_message = str(error_data)
        except json.JSONDecodeError:
            # Handle cases where JSON parsing fails
            error_message = "Invalid JSON response"
    else:
        # Handle non-JSON responses
        error_message = f"Non-JSON response received: {response.text[:2000]}"

    print(f"Error - Status Code: {response.status_code} - Message: {error_message}")

    # Optionally, you can return the error message if you want to use it elsewhere
    return error_message
