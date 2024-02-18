# Creating a dictionary of cholesterol medications
# Quantity is 30 day supply (sig: once daily)
my_dict_cholesterol_medications = [
  {"Brand Name": "Lipitor", "Generic Name": "Atorvastatin", "Strength": "40mg", "Quantity": 30},
  {"Brand Name": "Zocor", "Generic Name": "Simvastatin", "Strength": "20mg", "Quantity": 30 },
  {"Brand Name": "Crestor", "Generic Name": "Rosuvastatin", "Strength": "5mg", "Quantity": 30},
  {"Brand Name": "Pravachol", "Generic Name": "Pravastatin", "Strength": "40mg", "Quantity": 30},
  {"Brand Name": "Zetia", "Generic Name": "Ezetimibe", "Strength": "10mg", "Quantity": 30}

]
for medication in my_dict_cholesterol_medications:
  brand_name = medication["Brand Name"]
  generic_name = medication["Generic Name"]
  strength = medication ["Strength"]
  quantity = medication["Quantity"]
  
  print("Brand Name:", brand_name)
  print("Generic Name:", generic_name)
  print("Strength:", strength)
  print("Quantity:", quantity)
  print()
Brand Name: Lipitor
Generic Name: Atorvastatin
Strength: 40mg
Quantity: 30

Brand Name: Zocor
Generic Name: Simvastatin
Strength: 20mg
Quantity: 30

Brand Name: Crestor
Generic Name: Rosuvastatin
Strength: 5mg
Quantity: 30

Brand Name: Pravachol
Generic Name: Pravastatin
Strength: 40mg
Quantity: 30

Brand Name: Zetia
Generic Name: Ezetimibe
Strength: 10mg
Quantity: 30
