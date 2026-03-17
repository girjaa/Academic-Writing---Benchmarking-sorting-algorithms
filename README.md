Here is a **clean, professional `README.md`** you can place in your repository
(ready to paste directly into GitHub).

---

# Benchmarking Sorting Algorithms

This repository contains the implementation and experimental evaluation of several sorting algorithms as part of an **Academic Writing project on algorithm benchmarking**.

The goal of the project is to compare the performance of different sorting algorithms under various conditions, such as different dataset sizes, structures, and data types.

Sorting algorithms are fundamental in computer science and play an important role in efficiently organizing and processing data in many systems. ([irjiet.com][1])

---

# Project Objectives

The project aims to:

* Implement multiple sorting algorithms
* Generate datasets with different characteristics
* Measure execution time for each algorithm
* Compare algorithm performance across different scenarios
* Analyze whether observed behavior matches theoretical time complexity

---

# Implemented Sorting Algorithms

The repository includes implementations of the following algorithms:

* Bubble Sort
* Selection Sort
* Insertion Sort
* Shell Sort
* Merge Sort
* Quick Sort
* Heap Sort
* Counting Sort
* Radix Sort

These algorithms represent different complexity classes such as:

| Algorithm Type                     | Example Algorithms           |
| ---------------------------------- | ---------------------------- |
| Quadratic (O(n²))                  | Bubble, Selection, Insertion |
| Log-linear (O(n log n))            | Merge, Quick, Heap           |
| Linear (O(n)) (for specific cases) | Counting, Radix              |

Studies comparing sorting algorithms often show that algorithms like **QuickSort and MergeSort perform best for large datasets**, while simpler algorithms such as **Bubble Sort are significantly slower**. ([PhilPapers][2])

---

# Dataset Types Tested

To obtain meaningful results, the algorithms are tested on multiple dataset structures:

* Random lists
* Already sorted lists
* Reverse sorted lists
* Almost sorted lists
* Half sorted / half random lists
* Flat lists (few distinct values)

This helps evaluate how algorithms behave in **best-case, average-case, and worst-case scenarios**.

---

# Dataset Sizes

The experiment includes datasets of increasing sizes:

```
20
30
50
100
1,000
10,000
100,000
1,000,000
10,000,000
100,000,000
```

Small datasets are used for algorithms with quadratic complexity, while large datasets are used for more efficient algorithms.

---

# Data Structures Tested

The experiments test sorting performance using:

* **Arrays (Python lists)**
* **Linked lists**

This allows comparison of algorithm behavior depending on the underlying data structure.

---

# Benchmark Methodology

The benchmark framework performs the following steps:

1. Generate input datasets
2. Run sorting algorithms on each dataset
3. Measure execution time using high-precision timers
4. Repeat experiments to reduce measurement noise
5. Store results in a CSV file

Execution time is measured using Python's high-resolution timer:

```
time.perf_counter()
```

---

# Running the Experiment

### 1. Clone the repository

```bash
git clone https://github.com/girjaa/Academic-Writing---Benchmarking-sorting-algorithms.git
cd Academic-Writing---Benchmarking-sorting-algorithms
```

### 2. Prepare dataset sizes

Edit the file:

```
sizes.txt
```

Example:

```
20
30
50
100
1000
10000
100000
1000000
```

### 3. Run the benchmark

```bash
python benchmark.py
```

---

# Output

Results are written to:

```
results.csv
```

Example output:

```
algorithm,structure,dataset,size,time
quick,array,random,10000,0.0042
merge,array,sorted,10000,0.0038
heap,array,reverse,10000,0.0051
```

This data can later be used to generate charts and performance analysis.

---

# Project Structure

```
PythonProject        # main benchmarking folder ran in pycharm/vsc
AW_Sorting_Alg_Girjaliu_Gabriel_.zip  # a zip containing a latex version of a documentation
```

---

# Possible Future Improvements

* Visualization of results using graphs
* Parallel sorting experiments
* GPU-based sorting comparisons
* Additional algorithms (Timsort, Bucket Sort, Tree Sort)
* Statistical analysis of benchmark results

---

# Author

Academic Writing Project
Benchmarking Sorting Algorithms

GitHub:
[https://github.com/girjaa](https://github.com/girjaa)

---
