def reverse_complement(text):
    complement_strand = ""
    for i in range(len(text)-1, -1, -1):
        if text[i] == 'A':
            complement_strand += 'T'
        elif text[i] == 'C': 
            complement_strand += 'G'
        elif text[i] == 'T':
            complement_strand += 'A'
        elif text[i] == 'G':
            complement_strand += 'C'
    
    print(complement_strand)
    return complement_strand

with open('./datasets/dataset_3_2.txt', 'r') as f:
    dataset = f.readlines()
dataset = [x.strip() for x in dataset]

reverse_complement(dataset[0].upper())