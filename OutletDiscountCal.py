# Used for U.S. Outlet 2 times Discount calculate

price=eval(input('Enter price: '))
f_off=eval(input('Enter 1st off: '))/100
s_off=eval(input('Enter 2nd off: '))/100
f_discount=price*(1-f_off)
s_discount=f_discount*s_off
f_price=f_discount-s_discount
perc=f_price/price
print(f_off*100,'% off price is ', f_discount)
print('After 30% off again is ',f_discount,'-',s_discount,'=>',f_price)
print('The discount percentage is ',int(perc*100)/100.0*100,'%' )
