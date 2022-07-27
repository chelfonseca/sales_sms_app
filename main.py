# Steps for solution

# Import libraries:
import pandas as pd
from twilio.rest import Client

# Acount SID from twilio.com/console
account_sid = "AC7c6d4bbe1e4d69bff137a7a82d27f922"

#Auth Token from twilio.com/console
auth_token = "4894720144783a3d68c7b41225709236"
client = Client(account_sid, auth_token)

# Open Excel spreadsheets

list_month = ['january', 'february', 'march', 'april', 'may', 'june']

for month in list_month:
    table_sales = pd.read_excel(f'{month}.xlsx')
    if (table_sales['Sales'] > 55000).any():
        seller = table_sales.loc[table_sales['Sales'] > 55000, 'Seller'].values[0]
        sales = table_sales.loc[table_sales['Sales'] > 55000, 'Sales'].values[0]
        print(f'The seller: {seller} reached the target of 55000 on month {month}')

        message = client.messages.create(
            to="+5511995418955",
            from_="+16513698159",
            body=f'The seller: {seller} reached the target of 55000 on month {month}')
        print(message.sid)
# For each file:
# Verify if there is a value greater than 55.000 in Sales column
# If the value is above -> send a SMS with Name, Month and Seller sales value
# Else do nothing
