import random

def normalizeValues(dictionary):
	divisor = 0.0
	for key in dictionary:
		divisor += dictionary[key]

	for key in dictionary:
		dictionary[key] /= divisor

n = 3
inputText = "a a b a b b c d b a a b c"		# I like to use random samples from Gutenberg
splitter = " "
inputText = inputText.replace("\n", splitter)

recentValues = ("b", "a")
toGenerate = 100

unitList = inputText.split(splitter)

unitNGramProbabilities = {}

for i in range(len(unitList) - (n - 1)):
	nValues = tuple(unitList[i:i + n])
	unitNGramProbabilities[nValues] = unitNGramProbabilities.get(nValues, 0) + 1

outString = splitter.join(recentValues) + splitter

for i in range(toGenerate):
	relevantNGramProbabilities = {}

	for key in unitNGramProbabilities:
		if key[0:n-1] == recentValues:
			relevantNGramProbabilities[key] = unitNGramProbabilities[key]

	normalizeValues(relevantNGramProbabilities)

	randomNumber = random.random()
	counter = 0
	for key in relevantNGramProbabilities:
		counter += relevantNGramProbabilities[key]
		if randomNumber < counter:
			outString += key[n-1] + splitter
			recentValues = recentValues[1:] + (key[n-1],)
			break

print outString
