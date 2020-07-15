'''##############-_-*-HEADER-*-_-################'''
#***#################IFIK4004###################***#
'''-----------------1301164624-------------------'''

__author__ = "Muhammad Hasbi Ashshiddieqy"
__copyright__ = "Copyright 2019, KNearestNeighbor"

####################################################

'''*PYTHON AI K Nearest Neighbor*'''

import math
import timeit


#==================================================================================class================================================================================================

class Data:
	def __init__(self, attr1, attr2, attr3, attr4, kelas):
		self.attr1 = attr1
		self.attr2 = attr2
		self.attr3 = attr3
		self.attr4 = attr4
		self.kelas = kelas
		
	def addAttr(self, attr1, attr2, attr3, attr4, kelas=None):
		self.attr1.append(attr1)
		self.attr2.append(attr2)
		self.attr3.append(attr3)
		self.attr4.append(attr4)
		self.kelas.append(kelas)
	
	def removeHead(self):
		self.attr1.remove(self.attr1[0])
		self.attr2.remove(self.attr2[0])
		self.attr3.remove(self.attr3[0])
		self.attr4.remove(self.attr4[0])
		self.kelas.remove(self.kelas[0])

	def convertAttr(self):
		self.attr1 = list(map(float,self.attr1))
		self.attr2 = list(map(float,self.attr2))
		self.attr3 = list(map(float,self.attr3))
		self.attr4 = list(map(float,self.attr4))
		
	def convertKelas(self):
		for i in range(len(self.kelas)):
			self.kelas[i] = int(self.kelas[i][0])

		
#================================================================================function===============================================================================================
		
def KNearestNeighbor(K, hasil, kelasUji):
	hsl=[]
	minimum=[]
	satu=0
	for i in hasil:
		hsl.append(i)
	for i in range(K):
		minimum.append(min(hsl))
		hsl.remove(min(hsl))
	idxHasil = list(map(hasil.index,minimum))
	kelas = list(map(lambda x: kelasUji.kelas[x],idxHasil))
	satu = kelas.count(1)
	if satu > (K/2):
		return 1
	else:
		return 0
		
	
def euclideanDistance(kelasTest, kelasUji, K):
	hasil=[]
	for i in range(len(kelasTest.attr1)):
		for j in range(len(kelasUji.attr1)):
			hsl = math.sqrt(((kelasUji.attr1[j]-kelasTest.attr1[i])**2)+((kelasUji.attr2[j]-kelasTest.attr2[i])**2)+((kelasUji.attr3[j]-kelasTest.attr3[i])**2)+((kelasUji.attr4[j]-kelasTest.attr4[i])**2))
			hasil.append(hsl)
		yield KNearestNeighbor(K,hasil,kelasUji)
		hasil=[]
		
def validasiK(kelasTest, kelasUji, K):
	kelas = list(euclideanDistance(kelasTest, kelasUji, K))
	akr=0
	for i in range(len(kelas)):
		if kelas[i]==kelasTest.kelas[i]:
			akr+=1
		else:
			continue
	akurasi = (akr/len(kelas))*100
	file = open("ValidK.csv", "a")
	datum = str(K)+","+str(akurasi)+"\n"
	file.write(datum)
	file.close()
	
def main():
	start = timeit.default_timer()
	DataTrain = Data([],[],[],[],[])
	file = open("DataTrain.csv","r")
	for line in file:
		data = []
		data = line.split(",")
		DataTrain.addAttr(data[0],data[1],data[2],data[3],data[4])
	DataTrain.removeHead()
	DataTrain.convertAttr()
	DataTrain.convertKelas()
	file.close()
	for i in range(3,30,2):
		validasiK(DataTrain,DataTrain,i)
	stop = timeit.default_timer()
	print("Time to run : ", stop-start)
	
if __name__=="__main__":
	main()