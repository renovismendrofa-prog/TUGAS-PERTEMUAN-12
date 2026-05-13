def selection_sort_generic(arr, ascending=True):
    """
    MODIFIKASI selection_sort_ascending:
    - GENERIK: Bekerja untuk ANGKA dan STRING
    - ascending=True:  A→Z, 1→9
    - ascending=False: Z→A, 9→1
    
    Contoh penggunaan:
    - Angka: [5, 2, 8, 1]
    - String: ["pisang", "apel", "jeruk"]
    """
    n = len(arr)
    
    print(f"Sorting {'ASCENDING' if ascending else 'DESCENDING'}")
    print(f"Data awal: {arr}")
    print(f"Tipe: {type(arr[0]).__name__}")
    print("-" * 40)
    
    for i in range(n-1):
        # Tentukan pivot (min/max index)
        pivot_idx = i
        
        # Cari ekstrem di bagian belum terurut
        for j in range(i+1, n):
            if ascending:
                # ASCENDING: cari YANG LEBIH KECIL
                if arr[j] < arr[pivot_idx]:
                    pivot_idx = j
            else:
                # DESCENDING: cari YANG LEBIH BESAR
                if arr[j] > arr[pivot_idx]:
                    pivot_idx = j
        
        # SWAP jika ditemukan yang lebih ekstrem
        if pivot_idx != i:
            print(f"  Iterasi {i+1}: SWAP {arr[i]} ↔ {arr[pivot_idx]}")
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
        else:
            print(f"  Iterasi {i+1}: Sudah benar")
        
        print(f"  Array: {arr}")
    
    print("-" * 40)
    print(f"Hasil akhir: {arr}")
    return arr

# ================================================
# CONTOH PENGGUNAAN DENGAN LIST STRING
# ================================================

print("CONTOH 1: NAMA BUAH (Alfabetis A→Z)")
buah = ["pisang", "apel", "jeruk", "mangga", "anggur", "durian"]
selection_sort_generic(buah.copy(), ascending=True)

print("\n" + "="*60)

print("CONTOH 2: NAMA BUAH (Reverse Z→A)")
selection_sort_generic(buah.copy(), ascending=False)

print("\n" + "="*60)

print("CONTOH 3: ANGKA (Verifikasi)")
angka = [64, 34, 25, 12, 22, 90, 11]
selection_sort_generic(angka.copy(), ascending=True)

print("\n" + "="*60)

print("CONTOH 4: Mixed Case String")
nama = ["Zebra", "apple", "Banana", "zebra", "Cherry"]
selection_sort_generic(nama.copy(), ascending=True)