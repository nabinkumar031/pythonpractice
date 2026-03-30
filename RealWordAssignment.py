'''Grocery Bill Generator'''


'''return Tuple'''
''' 
def _getItemsDetails():
    itemName=input("Enter Item Name: ")
    qty=float(input("Enter Quantity: "))
    rate=float(input(f"Rate of {itemName}: "))
    #total = qty * rate
    return itemName , qty, rate

def _generateBill(items):
    print("\n------------Bill-------------")
    for itemName, qty, rate in items:
            print(f"{itemName}\t{qty}\t{rate}\t{rate*qty}")


items = []
done=False
while not done:
    nextItem=input("Enter new Item Details(Y/N):")
    if nextItem.lower() == 'y':
        item = _getItemsDetails()
        items.append(item)
    else:
        _generateBill(items)
        done = True
''' 

''' Attendence Percentage'''
'''
totalNumOfClasses = int(input("Enter total number of classes:"))
attendedClasses = int(input("Enter total class attended:"))

attendencePercentage= 0.0
attendencePercentage = attendedClasses/totalNumOfClasses * 100

print(f"Attendence Percentage={attendencePercentage}")
if attendencePercentage < 75.0:
    print("Poor attendence")
    
    
    
'''

'''Expense Tracker (Mini)'''



def enterAllExpenses():
    expenses=[]
    while True:
        expenseName=input("ExpenseName: ")
        expenseAmount=float(input("ExpenseAmount: "))
        expense=(expenseName,expenseAmount)
        expenses.append(expense)
        moreExpense=input("Enter more expenses(Y/N)")
        if moreExpense.lower() == "n":
            break
    return expenses

def highestExpense(expenses):
    highestExpense=expenses[0]
    for expenseName,expenseAmount in expenses:
        if expenseAmount > highestExpense[1]:
            highestExpense=(expenseName,expenseAmount)

    return highestExpense

def lowestExpense(expenses):
    lowestExpense=expenses[0]
    for expenseName,expenseAmount in expenses:
        if expenseAmount < lowestExpense[1]:
            lowestExpense=(expenseName,expenseAmount)

    return lowestExpense
            
enteredExpenses= enterAllExpenses()
print(f"highest expense: {highestExpense(enteredExpenses)}")
print(f"lowest expense: {lowestExpense(enteredExpenses)}")
        

