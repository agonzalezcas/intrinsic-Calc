csp = float (input( ' Current Share Price ($per share) : '))
so = float(input('Shares Outstanding (million) :'))
fcf = float (input ('Free Cash Flow (million) :'))
dcf = float(input ('Discount Rate :'))
lgr = float (input('Long-Term Growth Rate (%):'))
pgr=float(input('Perpetuity Growth Rate (%) :'))
cash=float(input('Total cash &Cash equivalent (million):'))
debt=float(input('Total Liabilities :'))
wacc= float (input('WACC (%) :'))

lgrr = lgr /100
dcfr = dcf /100
pgrr = pgr/100

#to change the percentage into decimals

pfcfr=0
discountedfcfr =0 
#pfcf = projected free cash flow
for n in range(1,11):
    pfcf=fcf*(1+lgrr)**n
    discountf= 1/(1+dcfr)**n
    discountedfcf = pfcf*discountf
    print('The discounted Free Cash flow of year', n ,'=', discountedfcf)
    pfcfr =discountedfcf +pfcfr
    n+=1

print('Perpetuity Value of 10y Discounted FCF (million) = ', pfcfr)

#Formula of intrinsic value :
pfcf=fcf*(1+lgrr)**10
pv=pfcf*(1+ pgrr)/(dcfr-pgrr)

discountf= 1/(1+dcfr)**10
print(discountf)
print(pv)
#change it into decimals 
tv=pv*discountf
#terminal value
print('The terminal value =',tv)

intrinsicv=(pfcfr+tv+cash-debt)/so
print('The Intrinsic Value =', intrinsicv)

if intrinsicv >= csp:
    print('The price is currently undervalued !!!! BUY')
else :
    print ('The Stock is currently overprized !!!!')
