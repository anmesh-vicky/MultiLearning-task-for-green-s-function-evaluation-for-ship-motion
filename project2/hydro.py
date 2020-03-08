from pannels import pannels as pt
import numpy as np
class hydro:
	def __init__(self,list,points):
		self.Mass = None
		self.points = points
		self.fr = []
		self.C33 = None
		self.C35 = None
		self.C55 = None
		self.list = list
		self.calulate()
		return 
		#c33 = pgA(Wp)
		#check
		#C55 = intgrate(X^2*Y)
		#C35 = intgrate(X*Y)
		#doubled the value
	def coeff(self):
		oriX = self.fr[0][0]
		oriY = self.fr[1][0]
		self.C33 = 2*1.025*9.81*abs(np.trapz(self.fr[:,1],self.fr[:,0]))
		self.C55 = abs(2*np.trapz(np.multiply((self.fr[:,0])**2,abs(self.fr[:,1])),self.fr[:,0]))           	
		self.C35 = abs(2*np.trapz(np.multiply((self.fr[:,0]),abs(self.fr[:,1])),self.fr[:,0]))           	
		return 
		# half used to calculate full value of mass*2
		#[X,Z,Y]
	def mass(self):
		self.Mass = 0
		for i in self.list:
			self.Mass = self.Mass + 2*9.81*1.025*i.Area*i.Cg[1]*i.Normal[1]
		return 
	def calulate(self):
		## calulates points on the surface
		##
		for i in self.points:
			if(i[2]==0):
				self.fr.append(i)
		self.fr.sort(key=lambda x: (x[0],x[1]))
		self.fr = np.array(self.fr)
		self.coeff()
		self.mass()
		return 
