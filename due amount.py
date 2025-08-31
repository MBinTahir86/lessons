def calculate_due_amount():
    # Get the total bill amount from the user
    total_bill = float(input("Enter the total bill amount: $"))

    
    amount_paid = float(input("Enter the amount paid: $"))

    
    if amount_paid < total_bill:
        due_amount = total_bill - amount_paid
        print(f"Customer still owes: ${due_amount:.2f}")
    elif amount_paid > total_bill:
        change = amount_paid - total_bill
        print(f"Customer has overpaid. Return change: ${change:.2f}")
    else:
        print("The bill is fully paid. No amount due.")


calculate_due_amount()
