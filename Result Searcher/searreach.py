

names  = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
quiz_scores = [90,      75,      88,    62,       95]
n = len(quiz_scores)
print("=== Score Tracker (n =", n, "players) ===")
for i in range(n):
    print(i + 1, ". ", names[i], " : ", quiz_scores[i], sep="")
print()


steps = 1
print("Score at index 0 :", quiz_scores[0], "| steps =", steps, "| Theta(1) - tight bound")
print()


target = "Aarav"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| Omega(1) - best case lower bound")

target = "Kabir"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Search for", target, "| steps =", steps, "| O(n) =", n, "- worst case upper bound")
print()


steps = 0
target_sum = 150
print("Pairs with total score =", target_sum, ":")
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if quiz_scores[i] + quiz_scores[j] == target_sum:
            print(" ", names[i], "+", names[j], "=", quiz_scores[i] + quiz_scores[j])
print("Total comparisons :", steps, "| O(n^2) - drop constants, keep n^2")
print()


# ── PART 5: Asymptotic Summary ────────────────────────────────────────────────
# Asymptotic analysis: only the dominant (fastest-growing) term matters.
# Example: 3n^2 + 5n + 9 -> O(n^2). Smaller terms become irrelevant at large n.

print("=== Asymptotic Summary ===")
print("Theta(1) : index access - always 1 step, tight bound")
print("Omega(1) : best case    - found in 1 step, lower bound")
print("O(n)     : worst case   - found after n =", n, "steps, upper bound")
print("O(n^2)   : pair check   - n*(n-1)/2 =", n * (n - 1) // 2, "comparisons")
print()
print("Drop constants. Keep the dominant term. That is asymptotic analysis!")
