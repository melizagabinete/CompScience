#Implementation of k-NN algorithm w/o using any libraries

#Problem: A movie streaming service wants to classify a new movie based on its genre score, duration, and rating.
#Given a dataset of existing movies with known categories (Action, Drama, or Comedy), 
# the system will use the k-NN algorithm to predict the category of the new movie.  
# With k = 3 nearest neighbors, determine which genre the new movie most likely belongs to.

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
    
    #Sort by distance / ascending order
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
    
    #The most voted
    sortedVotes = sorted(classVotes.items(), key=lambda x: x[1], reverse=True)
    return sortedVotes[0][0]


#Genre Score, Duration (minutes), Rating, Category
dataset = [
    [8.5, 120, 7.5, 'Action'],
    [7.0, 150, 8.0, 'Drama'],
    [6.5, 90, 6.0, 'Comedy'],
    [9.0, 110, 8.5, 'Action'],
    [8.0, 130, 7.8, 'Drama'],
    [5.5, 100, 5.0, 'Comedy']
]

#Test instance
testInstance = [7.8, 125, 7.6]  #New movie
k = 3  #Number of neighbors to consider

#Prediction
predictedCategory = predictClassification(dataset, testInstance, k)
print("===================")
print(f"Predicted movie category: {predictedCategory}")
