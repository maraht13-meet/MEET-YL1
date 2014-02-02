class Integer(object):
	def __init__(self, number="" , dis=True):
		self.num = number
		self.d = dis


	def display(self):
		if self.d == False :
			print "-" + str(self.num)
		else:
			print self.num
		
class NegativeInteger(Integer):
	def __init__(self, number=""):
		super(NegativeInteger, self).__init__(number , False)
	
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"

if __name__=="__main__":
	print "Michele"
	
	number = raw_input("Give me a positive number :) ")
	print number
	number1 = raw_input("Give me a negative number :) ")	
	print number1


	test = Integer(number)
	test2 = NegativeInteger(number1)
	
	m = [test , test2]
	for tests in m :
		tests.display()

 
	

