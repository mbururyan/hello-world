#VAT calculator:

#Inputs saved as promts
promt_id = "Enter item ID :"
promt_name = "Enter item's name : "
promt_quantity = "Enter item's quantity : "
promt_price = "Enter the items price :"

count = 1

while True:
    item_ID = input(promt_id)

# Break statement to indicate when cashier does not have any more records to calculate VAT for
    if item_ID == 'done':
        break

    item_name = str(input(promt_name))
    item_amt = float(input(promt_quantity))
    item_price = int(input(promt_price))


#Calculating VAT
    VAT = (0.16 * item_price)
    total_price = VAT + item_price

#printing the item's VAT
    print("The item " +str(item_name) + " VAT is : " +str(VAT) + "Kshs.")

#printing the total amount after tax
    print("The item's total cost after tax is : " +str(total_price) + "Kshs.")



