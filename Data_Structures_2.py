# Recipe Explorer (complete activity, DSCM2L2). Python 3 standard library only.
# Run: python recipe_explorer.py  (or paste into one Google Colab cell and press Run)
# Time: O(n log n) overall, only because sorted() orders each set for printing; building the sets
# and every set operation is O(n) on average. Space: O(n) (n = number of ingredients).

# A. Step 1: two recipe cards as tuples: (name, cuisine, minutes, level). They never change.
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
burrito = ("Veg Burrito", "Mexican", 45, "Hard")
all_recipes = (pasta, burrito)                     # B: a tuple of tuples (nested)
print("Recipe 1:", pasta)

# Step 2: read the tuples without changing them.
print("Name:", pasta[0], "| Level:", pasta[-1])
print("Burrito time:", all_recipes[1][2])
print("Cuisine and minutes:", pasta[1:3])

# Step 3: loop over a tuple.
print("Pasta card:")
for detail in pasta:
    print(" -", detail)

# C. Step 4: ingredient lists as typed by a cook (garlic is typed twice).
pasta_list = ["tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"]
burrito_items = {"rice", "oregano", "garlic", "onion", "tomato", "spices"}
pasta_items = set(pasta_list)
print("Pasta items:", len(pasta_items), sorted(pasta_items))

# Step 5: change the set.
extra = input("Add one ingredient to the pasta: ")
pasta_items.add(extra)
pasta_items.discard("chilli")
pasta_items.discard("basil")
print("Updated pasta items:", sorted(pasta_items))

# Step 6: compare the two sets.
every_item = pasta_items.union(burrito_items)
shared = pasta_items.intersection(burrito_items)
only_pasta = pasta_items.difference(burrito_items)
not_shared = pasta_items.symmetric_difference(burrito_items)
print("Every item:", sorted(every_item))
print("Shared:", sorted(shared))
print("Only pasta:", sorted(only_pasta))
print("Not shared:", sorted(not_shared))

# D: edge cases.
print("Is garlic in pasta?", "garlic" in pasta_items)      # O(1) on average
print("Empty braces make a:", type({}).__name__, "| set() makes a:", type(set()).__name__)
print("Shared with an empty set:", pasta_items.intersection(set()))
