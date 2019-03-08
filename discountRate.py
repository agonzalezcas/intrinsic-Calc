rfr = float(input ('Risk Free Rate (%):'))
mrp = float (input('Market Risk premium (%):'))
mvt = mve + mvd


taxd = taxr/100
interesty = interest /100
cod = interesty *(1 - taxd)
cod = cod*100
str(cod)
    
print ('The Cost of Debt is ', cod,'%' )


coe = rfr + (sbeta * mrp)
str(coe)
print ('The Cost of Equity is ' , coe,'%')
                         


wacc = (mve/mvt)* coe + (mvd/mvt)* cod
print ('The percentage of WACC (discount rate ) is :',wacc,'(%)')

    
yor =input ('Please enter "yes" to do this again ,"no" to exit ')
for y in yor :
    interest = float(input('Interest rate (%):'))
    taxr = float(input('Tax Rate (%):'))
    mve = float(input('Market value of Equity(Million) :'))
    mvd = float(input('Market value of Debt(Million) :'))
    sbeta = float (input('Stock beta :'))
    rfr = float(input ('Risk Free Rate (%):'))
    mrp = float (input('Market Risk premium (%):'))
    ccoe()
    ccod()
    yor =input ('Please enter "yes" to do this again ,"no" to exit ')

