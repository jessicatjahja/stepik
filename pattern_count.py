def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    print(count)
    return count

with open('./datasets/dataset_2_7.txt', 'r') as f:
    dataset = f.readlines()
dataset = [x.strip() for x in dataset]

print(dataset)
pattern_count(dataset[0], dataset[1])