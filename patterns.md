# 🧩 Core Algorithmic Patterns Library

Quick reference templates for standard Python DSA patterns.

---

## 1. Two Pointers (Opposite Direction)
```python
def two_pointer_template(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    result = 0
    while left < right:
        # Check condition
        if arr[left] + arr[right] == target:
            return (left, right)
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return -1
```

---

## 2. Sliding Window (Variable Size)
```python
def sliding_window_variable(arr: list[int], target: int) -> int:
    left = 0
    current_val = 0
    best_res = float('inf')
    
    for right in range(len(arr)):
        current_val += arr[right]
        
        while current_val >= target:
            best_res = min(best_res, right - left + 1)
            current_val -= arr[left]
            left += 1
            
    return best_res if best_res != float('inf') else 0
```

---

## 3. Binary Search (Standard)
```python
def binary_search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
