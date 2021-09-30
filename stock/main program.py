#while True:
print('''enter 1 for billing
enter 2 for stock check''')


a=int(input('enter your choice:'))
if a==1:
    import bill
elif a==2:
    import stock_ui

else:
    print('invalid input')

