'''
    Let us say your expense for every month are listed below,
        January - 2200
        February - 2350
        March - 2600
        April - 2130
        May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expense = {
    'january': 2200,
    'february': 2350,
    'march': 2600,
    'april': 2130,
    'may': 2190
}

def task1():
    extra_exp = expense.get('february') - expense.get('january')
    return extra_exp

def task2():
    total_expense = expense.get('february') + expense.get('january') + expense.get('march')
    return total_expense

def task3():
    for key,value in expense.items():
        if value == 2000:
            return key
    
def task4():
    june_exp = {
        'june': 1980
    }
    expense.update(june_exp)
    return expense

def task5():
    apl_exp_ref = expense.get('april') - 200
    expense.update(april=apl_exp_ref)
    return expense

def main():
    print(task1())
    print(task2())
    print(task3())
    print(task4())
    print(task5())

main()
