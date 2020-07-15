import numpy as np
import matplotlib.pyplot as plt

def takeData(fileName):
	Hasil = []
	file = open(fileName,"r")
	for line in file:
		data = []
		data = line.split(",")
		Hasil.append(data)
	file.close()
	return Hasil
	
def makeInferensiDict(Data):
	for i in range(len(Data)):
		inferensi[Data[i][0]]=[]
		

def toFloat(Data):
	for i in range(len(Data)):
		Data[i][1] = float(Data[i][1])
		Data[i][2] = float(Data[i][2])
	return Data

def grafKecil(c,d):
	#keluaran berupa [sumbuX,sumbuY] atau [bobot,derajatKebenaran]
	b = 0 #titik awal
	gfKecil = []
	for x in np.arange(b,d+0.1,0.1):
		if x<=c:
			gfKecil.append(round(x,2))
			gfKecil.append(1.)
		elif x>c and x<d:
			gfKecil.append(round(x,2))
			gfKecil.append(round(-(x-d)/(d-c),2))
		else:
			gfKecil.append(round(x,2))
			gfKecil.append(0.)
	return gfKecil

def grafSedang(a,b,c,d):
	#a grafSedang == c grafKecil; d grafKecil == b grafSedang 
	gfSedang = []
	for x in np.arange(a,d+0.09,0.1):
		if	x>a and x<b:
			gfSedang.append(round(x,2))
			gfSedang.append(round((x-a)/(b-a),2))
		elif x>=b and x<=c:
			gfSedang.append(round(x,2))
			gfSedang.append(1.)
		elif x>c and x<d:
			gfSedang.append(round(x,2))
			gfSedang.append(round(-(x-d)/(d-c),2))
		else:
			gfSedang.append(round(x,2))
			gfSedang.append(0.)
	return gfSedang

def grafBesar(a,b):
	c = 100
	gfBesar = []
	for x in np.arange(a,c+0.09,0.1):
		if x<=c and x>=b:
			gfBesar.append(round(x,2))
			gfBesar.append(1.)
		elif x<b and x>a:
			gfBesar.append(round(x,2))
			gfBesar.append(round((x-a)/(b-a),2))
		else:
			gfBesar.append(round(x,2))
			gfBesar.append(0.)
	return gfBesar

def nilaiKebenaran(Data,Nilai,Param):
	if Param == "Kompetensi":
		idx = 1
	elif Param == "Pribadi":
		idx = 2
	for i in range(len(Data)):
		if Data[i][idx] in Nilai["K"]:
			value = [Data[i][0],Data[i][idx],Nilai["K"][Nilai["K"].index(Data[i][idx])+1],"K"]
			kebenaran[Param].append(value)
		if Data[i][idx] in Nilai["S"]:
			value = [Data[i][0],Data[i][idx],Nilai["S"][Nilai["S"].index(Data[i][idx])+1],"S"]
			kebenaran[Param].append(value)
		if Data[i][idx] in Nilai["B"]:
			value = [Data[i][0],Data[i][idx],Nilai["B"][Nilai["B"].index(Data[i][idx])+1],"B"]
			kebenaran[Param].append(value)
	#print(kebenaran[Param])
	
def inferensiFuzzy():
	for i in range(len(kebenaran["Kompetensi"])):
		for j in range(len(kebenaran["Pribadi"])):
			if kebenaran["Kompetensi"][i][0]==kebenaran["Pribadi"][j][0]:
				if kebenaran["Kompetensi"][i][3]=="K":
					if kebenaran["Pribadi"][j][3]=="K":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Tidak",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="S":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Tidak",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="B":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Ya",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
				elif kebenaran["Kompetensi"][i][3]=="S":
					if kebenaran["Pribadi"][j][3]=="K":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Tidak",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="S":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Ya",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="B":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Ya",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
				elif kebenaran["Kompetensi"][i][3]=="B":
					if kebenaran["Pribadi"][j][3]=="K":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Tidak",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="S":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Ya",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
					elif kebenaran["Pribadi"][j][3]=="B":
						val = min(kebenaran["Kompetensi"][i][2],kebenaran["Pribadi"][j][2])
						value = ["Ya",val]
						inferensi[kebenaran["Kompetensi"][i][0]].append(value)
				
def nilaiKelayakan():
	for i in range(1,(len(inferensi)+1)):
		idx = "P" + str(i)
		tidak = []
		ya = []
		for j in range(len(inferensi[idx])):
			if "Tidak" in inferensi[idx][j]:
				tidak.append(inferensi[idx][j][1])
			elif "Ya" in inferensi[idx][j]:
				ya.append(inferensi[idx][j][1])
		if len(ya)>0:
			if len(tidak)>0:
				inferensi[idx]=[["Ya",max(ya)],["Tidak",max(tidak)]]
			else:
				inferensi[idx]=[["Ya",max(ya)]]
		else:
			if len(tidak)>0:
				inferensi[idx]=[["Tidak",max(tidak)]]
			else:
				continue
				
def defuzzifikasi():
	Hasil=[]
	for i in range(1,(len(inferensi)+1)):
		idx = "P"+str(i)
		if len(inferensi[idx])==2:
			pembilang = []
			acakya = np.linspace(60,100,10)
			acakya = acakya.tolist()
			acakya = [round(x,1) for x in acakya]
			indeksya = list(map(kelayakan["Ya"].index,acakya))
			layakya = list(map(lambda x: kelayakan["Ya"][x+1],indeksya))
			for i in range(len(layakya)):
				if layakya[i]>inferensi[idx][0][1]:
					layakya[i]=inferensi[idx][0][1]
			acaktdk =  np.linspace(0,60,10)
			acaktdk = acaktdk.tolist()
			acaktdk = [round(x,1) for x in acaktdk]
			indekstdk = list(map(kelayakan["Tidak"].index,acaktdk))
			layaktdk = list(map(lambda x: kelayakan["Tidak"][x+1],indekstdk))
			for i in range(len(layaktdk)):
				if layaktdk[i]>inferensi[idx][1][1]:
					layaktdk[i]=inferensi[idx][1][1]
			acak = acakya + acaktdk
			layak = layakya + layaktdk
			for i in range(len(layak)):
				pembilang.append(acak[i]*layak[i])
			hsl = sum(pembilang)/sum(layak)
			Hasil.append([hsl,idx])
			inferensi[idx] = [hsl]			
		elif len(inferensi[idx])==1:
			pembilang = []
			if inferensi[idx][0][0] == "Ya":
				acak = np.linspace(60,kelayakan[inferensi[idx][0][0]][(len(kelayakan[inferensi[idx][0][0]])-2)],10)
			elif inferensi[idx][0][0] == "Tidak":
				acak = np.linspace(kelayakan[inferensi[idx][0][0]][0],60,10)
			acak = acak.tolist()
			acak = [round(x,1) for x in acak]
			indeks = list(map(kelayakan[inferensi[idx][0][0]].index,acak))
			layak = list(map(lambda x: kelayakan[inferensi[idx][0][0]][x+1],indeks))
			for i in range(len(layak)):
				if layak[i]>inferensi[idx][0][1]:
					layak[i]=inferensi[idx][0][1]
			for i in range(len(layak)):
				pembilang.append(acak[i]*layak[i])
			hsl = sum(pembilang)/sum(layak)
			Hasil.append([hsl,idx])
			inferensi[idx] = [hsl]
	Hasil.sort()
	Hasil.reverse()
	makeDecision(Hasil,11)
	
def makeDecision(hasil,take):
	for i in range(len(hasil)):
		if i < take:
			inferensi[hasil[i][1]].append("Ya")
		else:
			inferensi[hasil[i][1]].append("Tidak")

kebenaran = {
	"Kompetensi":[],
	"Pribadi":[]
}

kompetensi = {
	"K":grafKecil(60,70),
	"S":grafSedang(60,70,70,80),
	"B":grafBesar(70,80)
}

pribadi = {
	"K":grafKecil(50,60),
	"S":grafSedang(50,60,80,90),
	"B":grafBesar(80,90)
}

kelayakan = {
	"Tidak":grafKecil(50,70),
	"Ya":grafBesar(50,70)
}

inferensi = {}

if __name__ == "__main__":
	file = "DataTrain.csv"
	files = "DataTest.csv"
	DataTrain = takeData(file)
	DataTrain = toFloat(DataTrain)
	DataTest = takeData(files)
	DataTest = toFloat(DataTest)
	Data = DataTrain + DataTest
	
	makeInferensiDict(Data)
	
	nilaiKebenaran(Data,kompetensi,"Kompetensi")
	nilaiKebenaran(Data,pribadi,"Pribadi")
	
	makeInferensiDict(Data)
	
	inferensiFuzzy()
	
	nilaiKelayakan()
	
	defuzzifikasi()
	
	print(inferensi)
	
	file = open("TebakanTugas3.csv","w")
	for i in range(1,31):
		idx = "P"+str(i)
		val = idx+","+inferensi[idx][1]+"\n"
		file.write(val)
	file.close()
	
	plt.title("FK KOMPETENSI")
	plt.plot(kompetensi["K"][0::2],kompetensi["K"][1::2],label="Kecil")
	plt.plot(kompetensi["S"][0::2],kompetensi["S"][1::2],label="Sedang")
	plt.plot(kompetensi["B"][0::2],kompetensi["B"][1::2],label="Besar")
	plt.legend()
	plt.draw()
	plt.figure()
	
	plt.title("FK KEPRIBADIAN")
	plt.plot(pribadi["K"][0::2],pribadi["K"][1::2],label="Kecil")
	plt.plot(pribadi["S"][0::2],pribadi["S"][1::2],label="Sedang")
	plt.plot(pribadi["B"][0::2],pribadi["B"][1::2],label="Besar")
	plt.legend()
	plt.draw()
	plt.show()