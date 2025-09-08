import random

# 3 divisions with 60 students each (random SPI between 0 and 10)
div1 = [random.uniform(0, 10) for _ in range(60)]
div2 = [random.uniform(0, 10) for _ in range(60)]
div3 = [random.uniform(0, 10) for _ in range(60)]

# Sort each division and take top 20
top1 = sorted(div1, reverse=True)[:20]
top2 = sorted(div2, reverse=True)[:20]
top3 = sorted(div3, reverse=True)[:20]

# Merge all top students (60 total)
merged = top1 + top2 + top3

# Sort merged list
merged_sorted = sorted(merged, reverse=True)

# Show results
print("Top 20 from Division 1:", top1)
print("Top 20 from Division 2:", top2)
print("Top 20 from Division 3:", top3)
print("\nFinal Merged Top 60 Sorted:", merged_sorted)
