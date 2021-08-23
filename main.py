print('')
print('Welcome to the Nod Hill Brewery Tips Calculator!')
# Create dictionary
staff = dict()
hourscount = 0.0


# User enters valid dollar number of cash tips
cashtips = input('Enter Cash Tips Amount: ')
while True:
    try:
        cashtips = float(cashtips)
        break
    except:
        cashtips = input('Error. Please enter valid Cash Tips Amount (Number only, no $ sign): ')
        continue
print('Cash Tips Amount is:  $', cashtips)
print('')

# User enters valid dollar number of credit card tips
cardtips = input('Enter Credit Card Tips Amount: ')
while True:
    try:
        cardtips = float(cardtips)
        break
    except:
        cardtips = input('Error. Please enter valid Credit Card Tips Amount: ')
        continue
print('Credit Card Tips Amount is:  $', cardtips)
print('')

# User enters names of staff members and how many hours worked
while True:
    try:
        name = input('Write staff member name or press ENTER to continue: ')
        if name == '':
            print('')
            break
        else :
            while True:
                try:
                    print('Enter', name, 'hours: ')
                    namehours = input()
                    namehours = float(namehours)
                    break
                except:
                    print('Error. Enter valid number of hours worked: ')
                    continue
            staff[name] = namehours
            #print(staff.items())
            hourscount = hourscount + namehours
            print('')
            print(name, "worked", namehours, "hours")
            print('Total staff hours worked: ', hourscount)
            print('')
    except:
        continue


#print(staff)
cashtipscheck = 0.00
cardtipscheck = 0.00
# Calculate cash tips amount for each staff member
for (k,v) in staff.items():
    v = v/hourscount
    print(k, "Tips Percentage: ", round(v*100, 2), '%', sep='')
    staffcashtips = v*cashtips
    cashtipscheck = cashtipscheck + staffcashtips
    staffcardtips = v*cardtips
    cardtipscheck = cardtipscheck + staffcardtips
    print(k, 'Cash tips:  $', round(staffcashtips, 2))
    print(k, 'Card tips:  $', round(staffcardtips, 2))
    print('')

print("Total staff hours worked: ", round(hourscount, 2), "hours")
print("Total staff cash tips:  $", round(cashtipscheck, 2), sep='')
print("Total staff cash tips:  $", round(cardtipscheck, 2), sep='')

