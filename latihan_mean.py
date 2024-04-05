import os

def mean(*args):
    """
    Fungsi untuk menghitung rata-rata (mean) dari sekumpulan angka.

    Args:
    *args: Sejumlah angka yang ingin dihitung rata-ratanya.

    Returns:
    float: Nilai rata-rata dari sekumpulan angka.
    """
    if not args:
        return None  # Mengembalikan None jika tidak ada argumen yang diberikan
    total = sum(args)
    count = len(args)
    return total / count

def main():
    numbers = []
    while True:
        try:
            os.system('cls')  # Membersihkan layar pada setiap iterasi
            num_input = float(input("Masukkan angka: "))
            numbers.append(num_input)
            continue_input = input("Lanjut (y/n): ").lower()
            if continue_input != 'y':
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue

    if numbers:
        avg = mean(*numbers)
        print(f"Nilai mean:\nHasil mean dari data: {numbers} = {avg}")
    else:
        print("Tidak ada data untuk dihitung.")

if __name__ == "__main__":
    main()
