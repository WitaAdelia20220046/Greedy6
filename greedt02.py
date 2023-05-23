def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Urutkan koin dari yang terbesar ke terkecil
    coin_count = 0  # Jumlah koin yang digunakan
    i = 0  # Indeks koin saat ini

    while amount > 0 and i < len(coins):
        if coins[i] <= amount:
            # Jika koin saat ini dapat digunakan, gunakan koin tersebut
            coin_count += 1
            amount -= coins[i]
        else:
            i += 1  # Pindah ke koin yang lebih kecil

    if amount > 0:
        return "Tidak ada solusi kembalian yang tepat."
    else:
        return coin_count

# Contoh penggunaan
coins = [1, 5, 10, 25]  # Nilai koin yang tersedia
amount = 47  # Jumlah uang yang akan dikembalikan

min_coins = coin_change_greedy(coins, amount)
print("Jumlah koin yang paling sedikit:", min_coins)
