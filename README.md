**Flight Deal Finder**

Flight Deal Finder is a Python application designed to help users find and monitor the best flight deals. 
The program integrates with the Amadeus API to search for both direct and indirect flights, comparing current prices to 
find the most cost-effective options. It automatically updates airport codes in a Google Sheet and sends notifications to 
users when a flight deal below their specified threshold is detected.

**Features**

- Dynamic Flight Search: Retrieves and compares flight options from a specified origin to various destinations, including direct and indirect flights.
- Google Sheets Integration: Updates airport codes in a Google Sheet and retrieves customer email addresses for notifications.
- Notification System: Sends notifications via email and WhatsApp when a flight deal is found. Customizable messages are sent based on whether the flight is direct or has stopovers.
- Rate Limiting: Implements delay intervals between API requests to avoid hitting rate limits and ensure reliable operation.

**How It Works**

- Setup: Initializes the connection with Google Sheets and the Amadeus API.
- Airport Code Update: Checks and updates the IATA codes for destinations in the Google Sheet.
- Flight Search: Searches for direct flights first; if none are found, searches for indirect flights.
- Price Comparison: Compares found flight prices with existing data to determine if a new deal is available.
- Notifications: Sends notifications to users via email and WhatsApp if a better deal is found.
-
![1](https://github.com/user-attachments/assets/69f7cc29-2413-45dc-8303-e9265f8084d9)

![2](https://github.com/user-attachments/assets/f5894cbc-dbde-4aa1-afd1-a1a9291db831)

![3](https://github.com/user-attachments/assets/9df40426-49ff-4cc6-8b34-ec1117ab9615)

![4](https://github.com/user-attachments/assets/31d38d39-e8ef-4ae1-8801-7cc0b7b513d3)

![5](https://github.com/user-attachments/assets/7cbd071a-d208-4df1-8893-64492fcf5dcf)
