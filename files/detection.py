import math

from pox.core import core

log = core.getLogger()

class Entropy(object):
	count = 0
	entDic = {}
	ipList = []
	dstEnt = []
	value = 1

	def statcolect(self, element):
		l = 0
		self.count +=1
		self.ipList.append(element)
		if self.count == 50:
			for i in self.ipList:
				l +=1
				if i not in self.entDic:
					self.entDic[i] =0
				self.entDic[i] +=1
			self.entropy(self.entDic)
			log.info(self.entDic)
			self.entDic = {}
			self.ipList = []
			l = 0
			self.count = 0

	def entropy (self, lists):
		l = 50
		elist = []
		for k,p in lists.items():
			c = p/float(l)
			c = abs(c)
			elist.append(-c * math.log(c, 10))
			#log.info('Entropy = ')
			#log.info(sum(elist))
			self.dstEnt.append(sum(elist))
		if(len(self.dstEnt)) == 80:
			print self.dstEnt
			self.dstEnt = []
                self.value = sum(elist)

	def __init__(self):
		pass