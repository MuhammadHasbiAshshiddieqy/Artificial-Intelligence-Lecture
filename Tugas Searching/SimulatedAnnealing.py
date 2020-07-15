'''##############-_-*-HEADER-*-_-################'''
#***#################IFIK4004###################***#
'''-----------------1301164624-------------------'''

__author__ = "Muhammad Hasbi Ashshiddieqy"
__copyright__ = "Copyright 2019, SimulatedAnnealing"

####################################################

'''*PYTHON AI Simulated Annealing*'''

import math
import random
import matplotlib.pyplot as graph

######################################################################---CLASS---####################################################################################################

class nodes:
	def __init__(self, x1, x2, value, position, minimum, minPosition):
		self.x1 = x1
		self.x2 = x2
		self.value = value
		self.position = position
		self.minimum = minimum
		self.minPosition = minPosition
		
	def addNode(self, x, y, val, pos):
		self.x1.append(x)
		self.x2.append(y)
		self.value.append(val)
		self.position.append(pos)
		
	def addMin(self, minVal, minPos):
		self.minimum.append(minVal)
		self.minPosition.append(minPos)
		
	def minSearchSA(self, point):
		temp = 1000
		final_temp = 0.0001
		alpha = 0.9999
		currentE = random.choice(point)
		bestE = currentE
		while temp > final_temp:
			nextE = random.choice(point)
			dE = nextE - currentE
			if dE < 0:
				currentE = nextE
				if currentE < bestE:
					bestE = currentE
				else:
					continue
			elif math.exp(-(float(dE))/(random.randrange(100,150))) > random.uniform(0,1):
				currentE = nextE
			else:
				continue
			temp = temp*alpha
		return bestE
	
	def minSearchActual(self):
		return min(self.minimum)
		
	def makeGraph(self, point):
		graph.title('SA pada data yang ditentukan (integer or float)')
		graph.plot(self.position, self.value, label = 'Hasil Fungsi', linestyle = '-.')
		graph.scatter(self.value.index(point), point, label = 'Minimum Global', color = 'red', marker = '*')
		graph.legend()
		graph.show()

################################################################################---FUNCTION---#######################################################################################
				
#Fungsi range untuk float. Seperti fungsi range pada python, namun default penambahan adalah 0.1 dan looping hingga stop (range default, looping hingga sebelum batas stop)
def floatRange(start, stop = None, step = None):
	#Pengecekan stop dan step tidak menggunakan else-if karena ada kemungkinan keduanya kosong
	if stop == None:
		stop = start
		start = 0.0
	if step == None:
		if start < stop:
			step = 0.1
		elif start > stop:
			step = -0.1
	while 1==1 :
		if step > 0 and start > stop:
			break
		elif step < 0 and start < stop:
			break
		yield start
		start+=step
		
		
def fungsi(x1, x2):
	return -(math.sin(x1)*math.cos(x2)+(4./5.)*math.exp(1-(math.sqrt((x1**2)+(x2**2)))))
	
###################################################################################---MAIN---########################################################################################
	
if __name__ == "__main__":
	makeNodes=[0,0,0]
	nodeGraph = nodes([],[],[],[],[],[])
	nodePos=0
	while nodePos < 100000:
		i = random.uniform(-10,10)
		j = random.uniform(-10,10)
		makeNodes[2]=makeNodes[1]
		makeNodes[1]=makeNodes[0]
		makeNodes[0]=fungsi(i,j)
		nodeGraph.addNode(i ,j , makeNodes[0],nodePos)
		if makeNodes[0] > makeNodes[1] and makeNodes[1] < makeNodes[2]:
			nodeGraph.addMin(makeNodes[1],nodePos)
		nodePos+=1
	globMinLoc = nodeGraph.value.index(nodeGraph.minSearchActual())
	SAtoAll = nodeGraph.minSearchSA(nodeGraph.value)
	SAtoMin = nodeGraph.minSearchSA(nodeGraph.minimum)
	AllatAll = nodeGraph.value.index(SAtoAll)
	MinatAll = nodeGraph.value.index(SAtoMin)
	x1SAall = nodeGraph.x1[AllatAll]
	x1SAmin = nodeGraph.x1[MinatAll]
	x2SAall = nodeGraph.x2[AllatAll]
	x2SAmin = nodeGraph.x2[MinatAll]
	AkurSAall = (min(nodeGraph.minimum)-SAtoAll)
	AkurSAmin = (min(nodeGraph.minimum)-SAtoMin)
	print("======================================")
	print("---SA pada 100000 data acak (float)---")
	print("======================================\n")
	print("SA dengan seluruh NODE --> ", SAtoAll)
	print("x1 : ", x1SAall)
	print("x2 : ", x2SAall)
	print("Kesalahan --> ", abs(AkurSAall), "\n")
	print("SA dengan minimum lokal --> ", SAtoMin)
	print("x1 : ", x1SAmin)
	print("x2 : ", x2SAmin)
	print("Kesalahan --> ", abs(AkurSAmin))
	print("\n")
	print("Nilai minimum global --> ", nodeGraph.minSearchActual())
	print("x1 : ", nodeGraph.x1[globMinLoc])
	print("x2 : ", nodeGraph.x2[globMinLoc])

	makeNodes=[0,0,0]
	nodeGraphs = nodes([],[],[],[],[],[])
	nodePos=0
	for i in floatRange(-10,10,1):
		for j in floatRange(-10,10,1):
			makeNodes[2]=makeNodes[1]
			makeNodes[1]=makeNodes[0]
			makeNodes[0]=fungsi(i,j)
			nodeGraphs.addNode(i ,j , makeNodes[0],nodePos)
			if makeNodes[0] > makeNodes[1] and makeNodes[1] < makeNodes[2]:
				nodeGraphs.addMin(makeNodes[1],nodePos)
			nodePos+=1
	globMinLoc = nodeGraphs.value.index(nodeGraphs.minSearchActual())
	SAtoAll = nodeGraphs.minSearchSA(nodeGraphs.value)
	SAtoMin = nodeGraphs.minSearchSA(nodeGraphs.minimum)
	AllatAll = nodeGraphs.value.index(SAtoAll)
	MinatAll = nodeGraphs.value.index(SAtoMin)
	x1SAall = nodeGraphs.x1[AllatAll]
	x1SAmin = nodeGraphs.x1[MinatAll]
	x2SAall = nodeGraphs.x2[AllatAll]
	x2SAmin = nodeGraphs.x2[MinatAll]
	AkurSAall = (min(nodeGraphs.minimum)-SAtoAll)
	AkurSAmin = (min(nodeGraphs.minimum)-SAtoMin)
	print("\n====================================================")
	print("---SA pada data yang ditentukan(integer or float)---")
	print("====================================================\n")
	print("SA dengan seluruh NODE --> ", SAtoAll)
	print("x1 : ", x1SAall)
	print("x2 : ", x2SAall)
	print("Kesalahan --> ", abs(AkurSAall), "\n")
	print("SA dengan minimum lokal --> ", SAtoMin)
	print("x1 : ", x1SAmin)
	print("x2 : ", x2SAmin)
	print("Kesalahan --> ", abs(AkurSAmin))
	print("\n")
	print("Nilai minimum global --> ", nodeGraphs.minSearchActual())
	print("x1 : ", nodeGraphs.x1[globMinLoc])
	print("x2 : ", nodeGraphs.x2[globMinLoc])
	nodeGraphs.makeGraph(SAtoAll)