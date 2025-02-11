# Problem: A web designer wants to optimize images by reducing their file sizes while preserving visual quality.  
# Given an image with a large number of unique colors, the designer will use the k-Means clustering algorithm  
# to group similar colors and reduce the total number of colors.  
# With k = 3 clusters, determine the representative colors that best represent the image.

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

pixels = [
    (255, 0, 0), (250, 5, 5), (245, 10, 10),  # Red
    (0, 255, 0), (5, 250, 5), (10, 245, 10),  # Green
    (0, 0, 255), (5, 5, 250), (10, 10, 245),  # Blue
    (200, 200, 200), (220, 220, 220), (240, 240, 240)  # Gray
]

k = 3 
centroids, clusters = kMeansClustering(pixels, k)

print("Reduced Colors (Centroids):", centroids)
