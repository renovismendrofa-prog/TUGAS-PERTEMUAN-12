def selection_sort_ascending(data):
    n = len(data)
    print("Data awal:", data)
    
    for i in range(n-1):
        min_idx = i
        print(f"\nIterasi {i+1} (i={i}):")
        
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        
        if min_idx != i:
            print(f"  SWAP {data[i]} ↔ {data[min_idx]}")
            data[i], data[min_idx] = data[min_idx], data[i]
        
        print(f"  Array: {data}")
        if i == 1:  # Henti setelah 2 iterasi
            print(f"\nHASIL SETELAH 2 ITERASI: {data}")
            return data
    
    return data

# Test
data = [7, 3, 9, 1, 5]
selection_sort_ascending(data.copy())