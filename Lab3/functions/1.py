def grams_to_ounces(grams):
    ounces=28.3495231*grams
    return ounces
grams=int(input("Gram engiz"))
x=grams_to_ounces(grams)
print(f"{grams}={x}")