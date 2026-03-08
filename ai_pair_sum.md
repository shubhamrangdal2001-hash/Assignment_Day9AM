# Part D — AI-Augmented Task: Pair Sum Analysis

## Step 1: Prompt Used

**Exact prompt sent to AI tool:**

> "Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions."

---

## Step 2: AI-Generated Code

```python
def find_pairs(lst, target):
    return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i+1, len(lst)) if lst[i] + lst[j] == target]
```

---

## Step 3: Testing the AI Code

**Test 1:**
```python
print(find_pairs([1, 2, 3, 4, 5], target=6))
# Output: [(1, 5), (2, 4)]
```

**Test 2:**
```python
print(find_pairs([1, 1, 1], target=2))
# Output: [(1, 1), (1, 1), (1, 1)]
```

### Issues Found

| Issue | Details |
|-------|---------|
| Duplicate pairs | For `[1, 1, 1]` with target `2`, it returns `(1, 1)` three times because it counts every index combination separately |
| No deduplication | It doesn't check if the same pair values have already been added |
| O(n²) complexity | Nested loop over all index combinations — fine for small lists but slow for large ones |

---

## Improved Version

```python
def find_pairs_improved(lst, target):
    seen = set()
    result = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            if pair not in result:
                result.append(pair)
        seen.add(num)
    return result
```

### Testing Improved Version

```python
print(find_pairs_improved([1, 2, 3, 4, 5], target=6))
# Output: [(1, 5), (2, 4)]

print(find_pairs_improved([1, 1, 1], target=2))
# Output: [(1, 1)]   <-- correctly returns only one pair
```

---

## Explanation of Each Improvement

### 1. Avoiding Duplicate Pairs
The AI version uses index-based iteration `(i, j)` so `(lst[1], lst[2])` and `(lst[0], lst[2])` can both be `(1, 1)`. The improved version normalizes each pair using `(min, max)` and checks if it already exists in the result before appending.

### 2. Handling Duplicate Values Correctly
For `[1, 1, 1]` the AI returns three copies of `(1, 1)`. My version uses a `seen` set to track processed elements and a result deduplication check so `(1, 1)` only appears once.

### 3. O(n) Solution Using Sets
The improved version runs in O(n) time. Instead of checking all pairs, for each element we check if its complement (`target - num`) is already in the `seen` set — a O(1) lookup. This avoids the nested loop entirely.

| Version | Time Complexity | Handles Duplicates? |
|---------|----------------|----------------------|
| AI version | O(n²) | No |
| Improved version | O(n) | Yes |

---

## Full Runnable Code

```python
# ai_pair_sum_demo.py

# --- AI Version (original) ---
def find_pairs_ai(lst, target):
    return [(lst[i], lst[j])
            for i in range(len(lst))
            for j in range(i+1, len(lst))
            if lst[i] + lst[j] == target]

# --- Improved Version ---
def find_pairs_improved(lst, target):
    seen = set()
    result = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            if pair not in result:
                result.append(pair)
        seen.add(num)
    return result


# Testing
print("AI Version:")
print(find_pairs_ai([1, 2, 3, 4, 5], 6))   # [(1, 5), (2, 4)]
print(find_pairs_ai([1, 1, 1], 2))          # [(1,1),(1,1),(1,1)] - duplicates!

print("\nImproved Version:")
print(find_pairs_improved([1, 2, 3, 4, 5], 6))  # [(1, 5), (2, 4)]
print(find_pairs_improved([1, 1, 1], 2))         # [(1, 1)] - correct
```
