import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euclideanDistance(pointOne, pointTwo):
    totalDistance = 0
    for i in range(len(pointOne) - 1): 
        totalDistance += (pointOne[i] - pointTwo[i]) ** 2
    return totalDistance ** 0.5  

def getNeighbors(trainingData, testInstance, k):
    distanceList = []
    for trainInstance in trainingData:
        distance = euclideanDistance(trainInstance, testInstance)
        distanceList.append((trainInstance, distance))
    
    # Sort by distance / ascending order
    distanceList.sort(key=lambda x: x[1])
    neighbors = [distanceList[i][0] for i in range(k)]
    return neighbors

def predictClassification(trainingData, testInstance, k):
    neighbors = getNeighbors(trainingData, testInstance, k)
    classVotes = {}
    
    for neighbor in neighbors:
        label = neighbor[-1] 
        if label in classVotes:
            classVotes[label] += 1
        else:
            classVotes[label] = 1
    
    # The most voted class
    sortedVotes = sorted(classVotes.items(), key=lambda x: x[1], reverse=True)
    return sortedVotes[0][0]

# Genre Score, Duration (minutes), Rating, Category
dataset = [
    [8.5, 120, 7.5, 'Action'],
    [7.0, 150, 8.0, 'Drama'],
    [6.5, 90, 6.0, 'Comedy'],
    [9.0, 110, 8.5, 'Action'],
    [8.0, 130, 7.8, 'Drama'],
    [5.5, 100, 5.0, 'Comedy']
]

testInstance = [7.8, 125, 7.6]  #New movie
k = 3

#Prediction
predictedCategory = predictClassification(dataset, testInstance, k)
print("===================")
print(f"Predicted movie category: {predictedCategory}")

#Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

colors = {'Action': 'red', 'Drama': 'blue', 'Comedy': 'green'}

for data in dataset:
    ax.scatter(data[0], data[1], data[2], color=colors[data[3]], label=data[3])

ax.scatter(testInstance[0], testInstance[1], testInstance[2], color='black', marker='X', s=100, label='New Movie')

ax.set_xlabel('Genre Score')
ax.set_ylabel('Duration (minutes)')
ax.set_zlabel('Rating')
ax.set_title('k-NN Movie Classification')
ax.legend()
plt.show()
