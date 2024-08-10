{
  "Mahek": {
    "balance": 3000.00,
    "transactions": [
      {"amount": -9000.00, "category": "Creatives"},
      {"amount": 7000.00, "category": "Sponsor"},
      {"amount": -2000.00, "category": "Prize-Money"}
    ]
  },
  "Arham": {
    "balance": 5000.00,
    "transactions": [
      {"amount": 8000.00, "category": "Stalls"},
      {"amount": 7500.00, "category": "Seminars"}
    ]
  },
  "Unnati": {
    "balance": 3500.00,
    "transactions": [
      {"amount": -5000.00, "category": "Attraction"},
      {"amount": 2500.00, "category": "Promo"},
      {"amount": -900.00, "category": "Lighting"},
      {"amount": -3000.00, "category": "Games"}
    ]
  },
  "Gaurang": {
    "balance": 2000.00,
    "transactions": [
      {"amount": 1500.00, "category": "Website"},
      {"amount": -1000.00, "category": "C2C"},
      {"amount": -500.00, "category": "Posters"}
    ]
  }
}

def total_spending(request_spending, account_id, category):
 
  account_data = request_spending.get(account_id)
  if not account_data:
    return 0.0

  total_spent = 0.0
  for transaction in account_data['transactions']:
    if transaction['category'] == category:
      total_spent += abs(transaction['amount'])
  return total_spent

def account_balance(request_spending, account_id):


  account_data = request_spending.get(account_id)
  if not account_data:
    return 0.0

  initial_balance = account_data['balance']
  total_transactions = sum(transaction['amount'] for transaction in account_data['transactions'])
  return initial_balance + total_transactions

def money_owed(request_spending, account_id):

  return max(0, -account_balance(request_spending, account_id))

    



