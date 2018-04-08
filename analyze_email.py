class Analyzer:
	def __init__(self, filename):
		self.counter = {}
		line = 1
		with open(filename) as f:
			for word in f:
				word = word.lower()
				try:
					self.counter[word] += 1
				except:
					self.counter[word] = 0
		
	def filter(self, top):
		self.top_words = {}
		print "There are %d unique words" % len(self.counter)
		counts = sorted(self.counter.values(), reverse=True)
		topth = counts[top - 1]
		for word in self.counter:
			if self.counter[word] >= topth:
				self.top_words[word] = self.counter[word]
		return self.top_words

	def vizualize(self):
		import numpy as np
		import matplotlib.pyplot as plt
		words = self.top_words.keys()
		counts = self.top_words.values()
	
		indexes = np.arange(len(words))
		width = 0.5
		plt.figure(figsize=(16, 6))
		plt.bar(indexes, counts, align='edge', width=width)
		plt.xticks(indexes + width * 0.5, words)
		plt.tight_layout()
		plt.savefig('word-count.png')
		plt.show()


if __name__ == "__main__":
	import sys
	a = Analyzer(sys.argv[1])
	a.filter(int(sys.argv[2]))
	a.vizualize()



