import numpy as np
class pannels:
	def __init__(self,points):
		self.Size = 4
		self.Points = points
		self.Area = None
		self.Normal = None
		self.Cg = None
		self.calculate()
		return
	def check(self):
		for i in range(3):
			if(np.array_equal(self.Points[i],self.Points[i+1])):
				self.Size = 3
				self.Points.pop(i)
				break
		return
	def area(self):
		AB = self.Points[1]-self.Points[0]
		BC = self.Points[2]-self.Points[1]
		if(self.Size == 4):
			CD = self.Points[3]-self.Points[2]
			DA = self.Points[0]-self.Points[3]
			product1 = np.cross(AB,BC)
			product2 = np.cross(CD,DA)
		else:
			product1 = np.cross(AB,BC)
			product2 = 0

		self.Area = (np.linalg.norm(product1)+np.linalg.norm(product2))/2
		self.Normal = product1/self.Area
		pass
	def cg(self):
		sum = [0,0,0]
		j = 0
		for i in self.Points:

			sum = np.add(sum,i)
			j = j+1
		sum = sum/j
		self.Cg = sum
		pass

	def calculate(self):
		self.check()
		self.area()
		self.cg()
		pass
