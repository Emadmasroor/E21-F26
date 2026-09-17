def stdev(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)
    std_dev = variance ** 0.5
    return std_dev