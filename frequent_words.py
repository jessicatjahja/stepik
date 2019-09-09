from pattern_count import pattern_count

def frequent_words(text, pattern_length):
    count = 0
    kmer_patterns = {}
    for i in range(0, len(text)-pattern_length):
        pattern = text[i:i+pattern_length]
        count = pattern_count(text, pattern)
        
        if pattern in kmer_patterns:
            kmer_patterns[pattern] += 1
        else:
            kmer_patterns[pattern] = count
    
    max_count = max(kmer_patterns.values())
    max_patterns = [k for k, v in kmer_patterns.items() if v == max_count]
    
    print(" ".join(max_patterns))
    return " ".join(max_patterns)

with open('./datasets/dataset_2_10.txt', 'r') as f:
    dataset = f.readlines()
dataset = [x.strip() for x in dataset]

frequent_words(dataset[0], int(dataset[1]))