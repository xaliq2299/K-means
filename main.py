import numpy as np
import random as rnd

class Cluster:
	def __init__(self):
		self.set=[]
		#self.centroid=[0,0,0,0]

	def findCentroid(self):
		self.centroid=[0,0,0,0]
		for i in range(4):
			for j in range(len(self.set)):
				self.centroid[i] += float(self.set[j][i])
		for i in range(4):
			if len(self.set) != 0:
				self.centroid[i] /= len(self.set)
		return self.centroid


def distance(a,b):
	#print(a,b)
	if len(a) != len(b):
		return None
	dist=0
	for i in range(len(a)):
		dist += (float(a[i])-float(b[i]))**2
	return dist

def stillChanges(clusters):
	flag=False
	# if empty sets
	if len(clusters[0].set) == 0 or len(clusters[1].set) == 0 or len(clusters[2].set) == 0:
		flag=True
		return flag
	
	for i in range(len(clusters)):
		for j in range(len(clusters[i].set)):
			distances=np.zeros(3) # precise the place
			for k in range(len(clusters)): # for np array of 0s
				#print(clusters[i].set[j], clusters[k].centroid)
				distances[k]=distance(clusters[i].set[j],clusters[k].centroid)
			
			#print(distances)
			min = distances.argmin() # closest cluster
			if min != i:
				flag=True
				return flag
	return flag

def findCluster(clusters,item):
	for i in range(len(clusters)):
		for j in range(len(clusters[i].set)):
			if clusters[i].set[j] == item:
				return i
	return -1


def main():
	irisData=[]
	k=3 # number of clusters

	file=open("iris_text.data", 'rt')
	line=file.readline()
	while line != "\n":
		# print(line)
		parse=line.split(',')
		# print(parse)
		irisData.append(parse)
		line=file.readline()

	#print(irisData)
	clusters=[]
	for i in range(k):
		clusters.append(Cluster())

	# Step 1: Cluster initialisation

	# Step *needed: appending irisData elements to clusters beforehand
	for i in range(k):
		start=i*len(irisData)//k
		end = start+len(irisData)//k
		for j in range(start,end):
			clusters[i].set.append(irisData[j][:4])

	#clusters[0].set.append(irisData[0][:4])
	for i in range(k):
		index=rnd.randint(0,len(irisData))
		clusters[i].centroid=irisData[index][:4]
		#clusters[0].centroid=irisData[0][:4]

	
	# Step 2: Assigning datapoint to clusters
	'''
	while( stillChanges(clusters) ):
		print("steps=", steps)
		for i in range(0,k):
			for j in range( len(clusters[i].set) ):
				distances=np.zeros(3) # [0, 0, 0]
				for d in range(0,3):
					print(i,j,d)
					print(len(clusters[i].set))
					distances[d]=distance(clusters[i].set[j],clusters[i].centroid)
				
				min = distances.argmin() # closest cluster
				if min != i: # if doesn't to the same cluster
				#print(i,j,min)
					clusters[min].set.append(clusters[i].set[j])
					clusters[i].set.remove(clusters[i].set[j])
		#print(len(clusters[1].set))	
		#print("Hello")
		clusters[0].findCentroid()
		clusters[1].findCentroid()
		clusters[2].findCentroid()

		steps += 1
	'''
	steps=0
	while( steps<10 ):
		for count in range(len(irisData)):
			# Euclidian distance with respect to each centroid
			distances=np.zeros(k) # [0, 0, 0]
			for d in range(k):
				distances[d]=distance(irisData[count][:4],clusters[d].centroid)
			#print(distances)
			min = distances.argmin() # closest cluster
			current = findCluster(clusters,irisData[count][:4])
			if min != current and current != -1: # if doesn't to the same cluster
			#print(i,j,min)
				clusters[current].set.remove(irisData[count][:4])
				clusters[min].set.append(irisData[count][:4])
			
		# Step 3: Updating clusters center
		for i in range(k):
			clusters[i].findCentroid()	
		for i in range(k):
			print( len(clusters[i].set) )
			
		steps += 1
		print("Step ", steps)


	# Summary
	for i in range(k):
		print("Cluster :", i)
		print("Centroid of cluster: ", clusters[i].findCentroid())
		print( "Length of cluster: ", len(clusters[i].set) )
		#print(clusters[i].set)

if __name__== "__main__" :
	main()
