# write your code here
import random

print("Enter the number of friends joining (including you):")
people_amount = int(input())
bill = []
if people_amount <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(0, people_amount):
        bill.append(input())
    big_bill = dict.fromkeys(bill, 0)
    print("Enter the total bill value:")
    total = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()
    if lucky == 'No':
        print('No one is going to be lucky')
        total = round(total / people_amount, 2)
        for k, val in big_bill.items():
            big_bill[k] = total
        print(big_bill)
    elif lucky == 'Yes':
        lucky_person = random.choice(bill)
        print(f"{lucky_person} is the lucky one")
        total = round(total / (people_amount - 1), 2)
        for k, val in big_bill.items():
            if k == lucky_person:
                big_bill[k] = 0
            else:
                big_bill[k] = total
        print(big_bill)

