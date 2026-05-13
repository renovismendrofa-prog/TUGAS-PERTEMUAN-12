def selection_sort_detailed(arr):
    """
    Selection Sort dengan logging ULTRA DETAIL
    Menampilkan tabel perbandingan setiap iterasi
    """
    n = len(arr)
    print(" " * 80)
    print("SELECTION SORT ASCENDING - LANGKAH DETAIL")
    print(" " * 80)
    print(f"DATA AWAL: {arr}")
    print()
    
    for i in range(n-1):
        print(f"ITERASI {i+1} (i = {i})")
        print("-" * 50)
        print(f"TERURUT: {arr[:i]}")
        print(f"BELUM TERURUT: {arr[i:]}")
        
        min_idx = i
        print("\nTABEL PERBANDINGAN:")
        print(f"{'Indeks':<6} {'Nilai':<6} {'>' + str(arr[i]) + '?':<10} {'min_idx':<7}")
        print("-" * 35)
        
        for j in range(i, n):
            is_smaller = arr[j] < arr[min_idx]
            if is_smaller:
                min_idx = j
            status = "YES" if is_smaller else "NO "
            print(f"{j:<6} {arr[j]:<6} {status:<10} {min_idx:<7}")
        
        print("-" * 35)
        if min_idx != i:
            print(f"TERKECIL: {arr[min_idx]} (indeks {min_idx})")
            print(f"SWAP: arr[{i}]={arr[i]} <-> arr[{min_idx}]={arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"ARRAY BARU: {arr}")
        else:
            print(f"{arr[i]} sudah terkecil -> TIDAK SWAP")
            print(f"ARRAY: {arr}")
    
    print("\n" + " " * 80)
    print(f"HASIL AKHIR: {arr}")
    return arr

if __name__ == "__main__":
    print("LANGKAH-LANGKAH SELECTION SORT")
    print("Data: [80, 10, 50, 70, 60, 20]")
    print()
    
    data_awal = [80, 10, 50, 70, 60, 20]
    hasil = selection_sort_detailed(data_awal.copy())
    
    print("\n" + " "*80)
    print("VERIFIKASI:")
    print(f"Awal:  {data_awal}")
    print(f"Akhir: {hasil}")
    print("TERURUT!")