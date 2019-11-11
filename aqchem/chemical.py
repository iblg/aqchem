class Mixture: # a mixture of chemicals
	def __init__(self, T):
		kw = 10**-14
		self.T = T #temperature in Kelvin
		self.c = [] # a list of chemicals in the solution, including concentrations.
		
		self.i = #ionic strength
		#self.en = #electroneutrality
		#self.hn = #hardness
		#self.ph = #ph at equilibrium #given inputs concentrations, temp, system should 
		#			solve for pH and then use alpha to calculate concentration of all components.
		#self.h = 10**(-self.ph) #[H+] at equilibrium
		#self.oh = kw / self.h #[OH-] at equilibrium
	
	def self.add(Chemical, conc):
		self.c.append(Chemical)
		
		return self
		
		
		
class Chemical:
	def __init__(self, pka):
		#self.pka = pka # a function of temperature
		#self.ka = 10**-pka # a function of temperature
		#self.charge 
		#self.ksp = ##		a function of temperature.
		#self.kh #henry's law coefficient. Shouldn't exist for ions or should be exceedingly small.


def main():
	closed_co3 = Mixture(300)
	closed_co3.add('Na2CO3',3) #add 3M sodium carbonate
	closed_co3.add('H2CO3',0.5) #add 0.5M carbonic acid


		
if __name__=="__main__":
	main()


#Forward problem/backward problem. Each statement involves an actor and an action. 
#The first actor is Yip. He wants to know how much DIPA to add to cause precipitation.
#Yip tells the program the composition of his water. Then he tells the program thing X.
#The program tells Yip minimum maximum optimal amount of x