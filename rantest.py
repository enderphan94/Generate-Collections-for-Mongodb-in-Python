from datetime import datetime
import random
import string
import names



def before_80():
	inc =3901
	patt_name = "Tom"
	for i in range(100):
		
		ex_name = "Tom"	
		year = random.choice(range(1945, 1980))
       		month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		
		print "db.clients.insert({name:"+"\""+ex_name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"
		

	for i in range(0,inc):
                name = names.get_first_name()
		year = random.choice(range(1945, 1980))
       	 	month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)
		
		if patt_name in name:
			
			inc = inc +1
		else:				
			print "db.clients.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

before_80()

def after_90():
	inc =3901
	patt_name = "Tom"
	
	for i in range(100):
		lastname = names.get_last_name()
		year = random.choice(range(1990, 2017))
        	month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
        	birth_date = datetime(year, month, day)

		if lastname != 'Tom':
			full_name = "Tom"+ " " + lastname
			print  "db.clients.insert({name:"+"\""+full_name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

	for i in range(0,inc):

		name = names.get_first_name()
		year = random.choice(range(1990, 2017))
	        month = random.choice(range(1, 13))
        	day = random.choice(range(1, 29))
       	 	birth_date = datetime(year, month, day)
		
		if patt_name in name:
			
			inc = inc +1
		else:				
			print "db.clients.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"
after_90()

def betw_80_90():
	inc=2001
	patt_name = "Tom"
	for i in range(0,inc):
		name = names.get_first_name()
                year = random.choice(range(1980, 1990))
                month = random.choice(range(1, 13))
                day = random.choice(range(1, 29))
                birth_date = datetime(year, month, day)

		if patt_name in name:
			
			inc = inc +1
		else:				
			print "db.clients.insert({name:"+"\""+name+"\""+","+"birthdate:"+"\""+str(birth_date.strftime('%Y-%m-%d'))+"\"});"

betw_80_90()
