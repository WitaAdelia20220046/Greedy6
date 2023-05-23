def select_outfit(formal, semi_formal, casual, accessories, shoes):
    outfit = []

    # Pilih pakaian formal terlebih dahulu
    if formal:
        outfit.append(formal.pop(0))

    # Pilih pakaian semi formal jika tidak ada pakaian formal
    elif semi_formal:
        outfit.append(semi_formal.pop(0))

    # Pilih pakaian kasual jika tidak ada pakaian formal dan semi formal
    elif casual:
        outfit.append(casual.pop(0))

    # Pilih aksesoris yang sesuai dengan pakaian
    if accessories:
        outfit.append(accessories.pop(0))

    # Pilih sepatu yang sesuai dengan pakaian
    if shoes:
        outfit.append(shoes.pop(0))

    return outfit
