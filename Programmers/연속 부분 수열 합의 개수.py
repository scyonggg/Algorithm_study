def solution(elements):
    answer = 0
    
    num_elements = len(elements)
    long_elements = elements
    long_elements.extend(elements)
    seq = []
    
    for length in range(num_elements):
        for idx in range(num_elements):
            seq.append(sum(elements[idx: (idx + length+1)]))
    
    return len(set(seq))
