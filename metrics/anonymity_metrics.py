import math
import numpy as np
from scipy import stats

def getEntropy(data, num_target_packets):
	columnsNames = ['Entropy'+str(x) for x in range(num_target_packets)]
	entropies = []
	for column in columnsNames:
		dist = data.iloc[0][column]
		# suma = sum([float(x) for x in dist])
		# print("For column %s the sum is %f" % (column, suma))
		# entropies.append()
		entropies.append(dist)
	return np.mean(entropies)

# def getEntropy(data):
# 	tmp = data[data["Type"] == "ENTROPY"]
# 	entropy = np.mean(tmp["Entropy"].tolist())
# 	return entropy

def log_privacy_metrics(epsilon, delta, noise):
    """Logs the differential privacy metrics and the noise applied.
    
    Parameters:
    epsilon (float): The epsilon value used for differential privacy.
    delta (float): The delta value used for differential privacy.
    noise (float): The noise value applied based on the privacy settings.
    """
    print(f"Applied Gaussian Noise: {noise:.6f}")
    print(f"Epsilon (ε): {epsilon}")
    print(f"Delta (δ): {delta}")
    print(f"This indicates (ε, δ)-differential privacy with the specified noise distribution.")

def getUnlinkability(data):
	epsilon = []
	dlts = 0
	est_senderA = data["PrSenderA"]
	est_senderB = data["PrSenderB"]
	realSenderLabel = data["RealSenderLabel"]

	for (prA, prB, label) in zip(est_senderA, est_senderB, realSenderLabel):
		if label == 1:
			if not float(prB) == 0.0:
				ratio = float(prA) / float(prB)
				if not ratio == 0.0:
					epsilon.append(math.log(ratio))
			else:
				dlts += 1
		elif label == 2:
			if not float(prA) == 0.0:
				ratio = float(prB) / float(prA)
				if not ratio == 0.0:
					epsilon.append(math.log(ratio))
			else:
				dlts += 1
		else:
			pass
	meanEps = None
	if epsilon != []:
		meanEps = np.mean(epsilon)
	delta = float(dlts) / float(len(est_senderA))
	return (meanEps, delta)


def computeE2ELatency(df):
	travelTime = []
	for i, r in df.iterrows():
	    timeSent = r['PacketTimeSent']
	    timeDelivered = r['PacketTimeDelivered']
	    travelTime.append(timeDelivered - timeSent)
	return np.mean(travelTime)
