#Expense traceker App
#App Requirements 
#1.User enters expenses
#2.Save expenses to CSV file
#3.Show remaining budget

from expense_class import Expense
import calendar
import datetime

def main():
    pass
    #get user input for expenses
    expense = get_user_expense()# this executes the function and stores the result in expenses (is used () so it excuties orelse just storee)
    expense_file_path="expense.csv" # name of the file where user expenses are going to get stored
    budget= 2000

    #write thier expense to a file.
    save_to_file(expense,expense_file_path)#add the expense file path and expense as arguments

    #read file and summarize expenses.

    summarize_expenses(expense_file_path,budget)

def get_user_expense():
    print("getting user expenses")
    expense_name=input("enter a expense name: ")
    expense_amount=float(input("enter expense amount: "))
    

    expense_categories = ["Food","Home","Work","Fun","Music"]

    while True:
        print("selected category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
        value_range = f"[1-{len(expense_categories)}]"#value range for user starts from 1 to len of the expnese categoris
        selected_index = int(input(f"enter a category number {value_range} :")) - 1#if user enter 5 it should selected 4th index bcz index starts from 0 we are subtracting it by 1 

        if selected_index in range(len(expense_categories)):#if selceted index is in expense category then u can go forward
            selcted_Category=expense_categories[selected_index]# we created this for seclted catorgry using expense catrgory and selected index
            new_expense = Expense(name=expense_name,category=selcted_Category,amount=expense_amount)# IMP: We are importing class Expense from expense_class.py file and using keyword argument we can assign them
            return new_expense #returing this as output for get_user_Expenses 
        else:
            print("Invalid category , please try again")

def save_to_file(expense: Expense,expense_file_path):#arguments are expense and expense file path by adding expense: Expense it gives hints about the class and help us not to make mistakes
    print(f"save user expense : {expense} to {expense_file_path}") 
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
def summarize_expenses(expense_file_path,budget):
    print("summarize user expenses")
    expenses:list[Expense] =[] # we are using python 3.11 so we can tell list[Expense] tht the type of list we are creating 
    with open(expense_file_path,"r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_category,expense_amount = line.strip().split(',')#we are using split which returns tuples so we can unpack it ryt away instead of saving it in the single variable 
            line_expense = Expense(#we are creeating object from the Expense class and name,category,amount went under split and strip
                name=expense_name,category=expense_category,amount=float(expense_amount)#convert to amount to float because u cant add valus if it is string it was converted to string when we used split on it
            )
            expenses.append(line_expense)
    print(expenses)
#Group the category by amount
    amount_by_category = {} # key is the category and the  value is amount spent for tht category
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key]+= expense.amount # if the category ex(food) alreay exist and u add one more item then u are going to add it 
        else:
             amount_by_category[key]= expense.amount# if the category doesnt exist then u are going to add the  amount as the amount of that category ,ex if music doesnt exist then u give it for first time then amount spend is eqaul to the amount whcih u gave 
    print("Expense By category")
    for key,amount in amount_by_category.items():#give key and the amount for each category
        print(f"{key}: ${amount:}")

#Track the remaining Budget
    total_spent = sum([expense.amount for expense in expenses ])
    print(f"Total Spent: ${total_spent:.2f} this month!")
    remainging_budget = budget - total_spent
    print(f"Budget remaining: $ {remainging_budget:.2f}")

    #get the current date
    now = datetime.datetime.now()
    #get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    #calculate the remaaning number of days in the current month
    remainging_days = days_in_month - now.day
    print("Remaining days in the current month is ", remainging_days)

    daily_budget = remainging_budget/remainging_days
    print("budger per day: $", daily_budget)
if __name__ =="__main__":  #"Only run the main() function if this file is being run directly, not when it is being imported into another file."
    main() 