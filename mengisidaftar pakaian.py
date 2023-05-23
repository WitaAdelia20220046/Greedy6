formal = ["Pakaian Formal 1", "Pakaian Formal 2"]
semi_formal = []
casual = ["Pakaian Kasual 1", "Pakaian Kasual 2"]
accessories = ["Aksesoris 1", "Aksesoris 2"]
shoes = ["Sepatu 1", "Sepatu 2"]

selected_outfit = select_outfit(formal, semi_formal, casual, accessories, shoes)
print("Pakaian yang dipilih:")
for item in selected_outfit:
    print("- " + item)
