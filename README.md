# Heap Data Structures Implementation

This repository contains Python implementations of two priority queue data structures: Binomial Heap and Leftist Tree. Both implementations provide standard priority queue operations with different performance characteristics.

## Overview

### Binomial Heap
A binomial heap is a collection of binomial trees that satisfies the min-heap property. It provides efficient operations for merging heaps and is well-suited for applications requiring frequent heap merges.

### Leftist Tree
A leftist tree (or leftist heap) is a priority queue implementation that maintains the "leftist" property, meaning the right path from root to an external node is always the shortest path. This property ensures efficient merging operations.

## Files

- `binomial_heap.py`: Implementation of the Binomial Heap data structure
- `left_tree.py`: Implementation of the Leftist Tree data structure
- `test_binomial_heap.py`: Test suite for the Binomial Heap implementation
- `test_left_tree.py`: Test suite for the Leftist Tree implementation
- `main.py`: Driver program to run functional tests for both implementations

## Features

Both implementations provide the following operations:

- `make_heap()`: Initialize an empty heap
- `minimum()`: Find the minimum element
- `extract_min()`: Remove and return the minimum element
- `insert(value)`: Add a new element to the heap
- `decrease_key(node, new_value)`: Decrease the value of a node
- `delete(node)`: Remove a specific node from the heap
- `union()`: Merge two heaps (internal operation)

## Usage

### Running the Tests

To run the functional tests for both implementations:

```bash
python main.py
```

This will execute the `functional_test()` method for both data structures, demonstrating their operations with predefined sample data.

### Automated Performance Testing

The code also includes automated performance testing. To enable this, uncomment the following lines in `main.py`:

```python
# leftist_test = TestLeftistTree()
# leftist_test.automate_test()

# binomial_test = TestBinomialHeap()
# binomial_test.automate_test()
```

Performance tests measure execution time (in milliseconds) for various operations using random data sets.

### Using the Data Structures in Your Code

#### Binomial Heap Example:

```python
from binomial_heap import BinomialHeap

# Create a new heap
heap = BinomialHeap()

# Insert elements
node1 = heap.insert(10)
node2 = heap.insert(5)
node3 = heap.insert(15)

# Get minimum
min_value = heap.minimum()  # Returns 5

# Extract minimum
heap.extract_min()  # Removes 5

# Decrease key
heap.decrease_key(node3, 3)  # Changes value of node3 from 15 to 3

# Delete a node
heap.delete(node1)  # Removes node with value 10
```

#### Leftist Tree Example:

```python
from left_tree import LeftistTree

# Create a new leftist tree
tree = LeftistTree()

# Insert elements
node1 = tree.insert(10)
node2 = tree.insert(5)
node3 = tree.insert(15)

# Get minimum
min_value = tree.minimum()  # Returns 5

# Extract minimum
tree.extract_min()  # Removes 5

# Decrease key
tree.decrease_key(node3, 3)  # Changes value of node3 from 15 to 3

# Delete a node
tree.delete(node1)  # Removes node with value 10
```

## Implementation Details

### Binomial Heap

- A binomial heap consists of a list of binomial trees
- Each binomial tree is represented by the `BinomialNode` class
- The heap maintains the min-heap property where the value of each node is less than or equal to the values of its children
- The union operation merges trees of the same order to maintain the binomial heap structure

### Leftist Tree

- A leftist tree is represented by the `LeftNode` class
- The "leftist property" is maintained: for every node, the distance to an external node along the right path is no greater than the distance along the left path
- The `distance` attribute keeps track of the right path length
- The union operation merges trees while preserving the leftist property

## Performance Characteristics

- **Binomial Heap**: O(log n) for insert, extract-min, delete, and decrease-key; O(1) for find-min
- **Leftist Tree**: O(log n) for insert, extract-min, and delete; O(1) for find-min

## Testing Parameters

The test files include parameters that can be adjusted:

```python
# TIME TEST PARAMS
ITER = 25
AUTO_RANGE_START = 0
AUTO_RANGE_STOP = 50000
AUTO_SAMPLES_CNT = 10000

# FUNCTIONALITY TEST PARAMS
SAMPLES = [17, 73, 48, 2, 91, 33, 59, 84, 12, 67, 5, 27]  # Sample values
```

You can modify these parameters to test with different data sets or iteration counts.
