import math

def get_cosine_similarity(vec1, vec2):
    intersection = set(vec1) & set(vec2)
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1])
    sum2 = sum([vec2[x] ** 2 for x in vec2])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def cosine_similarity(vec1: list[float], vec2: list[float]):
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(x**2 for x in vec1))
    magnitude2 = math.sqrt(sum(y**2 for y in vec2))

    if magnitude1 * magnitude2 == 0:
        return 0.0
    else:
        return dot_product / (magnitude1 * magnitude2)

def euclidean_distance(vec1: list[float], vec2: list[float]) -> float:
    return 1 - math.sqrt(sum((x - y)**2 for x, y in zip(vec1, vec2)))



def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

def dtw_distance(seq1, seq2):
    """Function to calculate Dynamic Time Warping distance.
        This distance metric (normally used for time series) can be useful when 
        distance between 2 sequences that are 'out of sync' 
        needs to be calculated."""
    n, m = len(seq1), len(seq2)
    max_dist = max(n,m)
    # Create a 2D list for the distance matrix
    dtw_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the first row and column of the matrix
    for i in range(1, n + 1):
        dtw_matrix[i][0] = float('inf')
    for j in range(1, m + 1):
        dtw_matrix[0][j] = float('inf')

    # Populate the distance matrix using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if seq1[i - 1] == seq2[j - 1] else 1
            dtw_matrix[i][j] = cost + min(
                dtw_matrix[i-1][j],
                dtw_matrix[i][j-1],
                dtw_matrix[i-1][j-1]
            )
    # Calculate the DTW distance
    dtw_distance = dtw_matrix[n][m]
    normalized_distance = (max_dist - dtw_distance)/float(max_dist)

    return normalized_distance
