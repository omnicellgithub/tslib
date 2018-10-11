######################################################
#
# Generate ARMA data
#
######################################################
import numpy as np

def generate(arLagsArray, maLagsArray, startingArray, timeSteps, noiseMean, noiseSD, sdfunc):

	p = len(arLagsArray)
	q = len(maLagsArray)
	prevPoints = len(startingArray)

	if (p > prevPoints):
		raise Exception('startingArray must be of length >= arLagsArray.')

	if (q > prevPoints):
		raise Exception('startingArray must be of length >= maLagsArray.')


	maxLags = np.max([p, q])
	outputArray = np.zeros(timeSteps + maxLags)
	outputArray[0: maxLags] = startingArray

	errorArray = np.random.normal(noiseMean, noiseSD, timeSteps + maxLags)
	for i in range(len(errorArray)):
		if i==len(sdfunc): break
		errorArray[i]=errorArray[i]*sdfunc[i]
	meanArray = np.zeros(timeSteps + maxLags)

	for i in range(maxLags, timeSteps):
		value = 0.0
		for j in range(0, p):
			value += (outputArray[i-j] * arLagsArray[j])

		for k in range(0, q):
			value += (errorArray[i-k] * maLagsArray[k])

		outputArray[i] = value + errorArray[i]
		meanArray[i] = value

	return (outputArray[maxLags:], meanArray[maxLags:], errorArray[maxLags:])
