# # calcuate the Bill on the basis of units

# # take inout of number of units consumed from the user

# units =int(input("please enter nunber of units you cosumed")

# # cala=culate the amount and surcharge accordingly , surcharge is the tax value

# if (units<50)://uma--->40

# amount=units*2.60//104

# surcharge=25

# # chcek for units less than 100//uma consumnhg 80 //instead of 80*3.25

# elif units<=100:

# //the first 50 units have alreday been carged at 2.60 each

# //50*2.60=130 now caluculat ethe reamaining units(80-50=30) now these 30 units *3.25

# amount=130+((units-50)*3.25)//227.50

# surcharge=35

# ******************* exalining slab biiiling ******************************

# First 50 units ----->2.60 per unit

# next 51-100 units --------------->3.25 per unit

# next 101-200 units --------->5.26 per unit

# total=amount+surcharge 227.50+35

# ********************Super Trick ********************************

# Units Already Paid Formulla

# 0-49 NOthing units*2.60=130

# 50-100 First 50 units =130 130+(units-50)*3.25=162.50

# 101-200 fisrt 100 units=130+ 162.50 130+162.50+(units-100)*5.26=526

# above 200 first 200 units=130+162.50+ 130+162.50+526+(units-200)*8.45

# 526

# *********************************** Golden RUle ************************************

# subtract the units you have alredt paid for

# upto 50 --->subtrcat 50

# add the cost of all previous slabs first

# First 50 units =130

# First 100 units = 130+162.50

# First 200 units = 130+162.50+526