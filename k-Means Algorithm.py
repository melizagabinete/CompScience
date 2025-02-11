import matplotlib.pyplot as plt

def initializeCentroids(pixels, k):
    return pixels[:k]

def calculateDistance(pixelOne, pixelTwo):
    return sum((pixelOne[i] - pixelTwo[i]) ** 2 for i in range(len(pixelOne))) ** 0.5

def assignClusters(pixels, centroids):
    clusters = {i: [] for i in range(len(centroids))}
    
    for pixel in pixels:
        distances = [calculateDistance(pixel, centroid) for centroid in centroids]
        closestCentroid = distances.index(min(distances))
        clusters[closestCentroid].append(pixel)
    
    return clusters

def updateCentroids(clusters):
    newCentroids = []
    for cluster in clusters.values():
        if cluster:
            newCentroids.append(tuple(sum(p[i] for p in cluster) // len(cluster) for i in range(len(cluster[0]))))
        else:
            newCentroids.append((0, 0, 0))  
    return newCentroids

def kMeansClustering(pixels, k, maxIterations=10):
    centroids = initializeCentroids(pixels, k)
    
    for _ in range(maxIterations):
        clusters = assignClusters(pixels, centroids)
        newCentroids = updateCentroids(clusters)
        
        if newCentroids == centroids:
            break  
        centroids = newCentroids
    
    return centroids, clusters

def plotClusters(pixels, clusters, centroids):
    plt.figure(figsize=(6, 6))
    
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'brown', 'pink', 'gray']
    
    for i, cluster in clusters.items():
        clusterPixels = list(zip(*cluster))
        if clusterPixels:
            plt.scatter(clusterPixels[0], clusterPixels[1], color=colors[i % len(colors)], label=f'Cluster {i+1}')
    
    centroidPixels = list(zip(*centroids))
    plt.scatter(centroidPixels[0], centroidPixels[1], color='black', marker='x', s=100, label='Centroids')
    
    plt.xlabel('Red Channel')
    plt.ylabel('Green Channel')
    plt.title('k-Means Clustering for Color Reduction')
    plt.legend()
    plt.show()

pixels = [
    (255, 0, 0), (250, 5, 5), (245, 10, 10),  # Red
    (0, 255, 0), (5, 250, 5), (10, 245, 10),  # Green
    (0, 0, 255), (5, 5, 250), (10, 10, 245),  # Blue 
    (200, 200, 200), (220, 220, 220), (240, 240, 240)  # Gray
]

k = 3  
centroids, clusters = kMeansClustering(pixels, k)

print("Reduced Colors (Centroids):", centroids)
plotClusters(pixels, clusters, centroids)
