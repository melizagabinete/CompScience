# Problem: A web designer wants to optimize images by reducing their file sizes while preserving visual quality.  
# Given an image with a large number of unique colors, the designer will use the k-Means clustering algorithm  
# to group similar colors and reduce the total number of colors.  
# With k = 3 clusters, determine the representative colors that best represent the image.

def initializeCentroids(pixels, k):
    """Initialize k centroids by selecting the first k unique pixels"""
    return pixels[:k]

def calculateDistance(pixelOne, pixelTwo):
    """Calculate Euclidean distance between two pixels"""
    return sum((pixelOne[i] - pixelTwo[i]) ** 2 for i in range(len(pixelOne))) ** 0.5

def assignClusters(pixels, centroids):
    """Assign each pixel to the nearest centroid"""
    clusters = {i: [] for i in range(len(centroids))}
    
    for pixel in pixels:
        distances = [calculateDistance(pixel, centroid) for centroid in centroids]
        closestCentroid = distances.index(min(distances))
        clusters[closestCentroid].append(pixel)
    
    return clusters

def updateCentroids(clusters):
    """Calculate new centroids as the mean of the assigned pixels"""
    newCentroids = []
    for cluster in clusters.values():
        if cluster:
            newCentroids.append(tuple(sum(p[i] for p in cluster) // len(cluster) for i in range(len(cluster[0]))))
        else:
            newCentroids.append((0, 0, 0))  # Default value if no points are assigned
    
    return newCentroids

def kMeansClustering(pixels, k, maxIterations=10):
    """Perform k-Means clustering on pixel data"""
    centroids = initializeCentroids(pixels, k)
    
    for _ in range(maxIterations):
        clusters = assignClusters(pixels, centroids)
        newCentroids = updateCentroids(clusters)
        
        if newCentroids == centroids:
            break  # Stop if centroids do not change
        
        centroids = newCentroids
    
    return centroids, clusters

# Example dataset (pixel colors in RGB format)
pixels = [
    (255, 0, 0), (250, 5, 5), (245, 10, 10),  # Red shades
    (0, 255, 0), (5, 250, 5), (10, 245, 10),  # Green shades
    (0, 0, 255), (5, 5, 250), (10, 10, 245),  # Blue shades
    (200, 200, 200), (220, 220, 220), (240, 240, 240)  # Gray shades
]

k = 3  # Number of colors to reduce to
centroids, clusters = kMeansClustering(pixels, k)

print("Reduced Colors (Centroids):", centroids)
