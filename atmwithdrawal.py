def atm_withdrawal(withdrawal_amount):
    current_balance = 5000
    if withdrawal_amount < 0 :
        print("Error: Withdrawal amount must be greater than 0")
        return False
    if withdrawal_amount % 500 != 0 :
        print("Error: Withdrawal amount must be a multiple of 500")
        return False
    if withdrawal_amount > current_balance :
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False

    print(f"Withdrawal Successful. Amount: {withdrawal_amount}")
    remaining_balance = current_balance - withdrawal_amount
    print(f"Remaining balance: {remaining_balance}")
    return True

atm_withdrawal(int(input("Enter amount to withdraw from ATM: ")))


    
