from left_tree import LeftistTree
from timeit import default_timer as timer
import random

# TIME TEST PARAMS
ITER = 25
AUTO_RANGE_START = 0
AUTO_RANGE_STOP = 50000
AUTO_SAMPLES_CNT = 10000

# FUNCTIONALITY TEST PARAMS
SAMPLES = [17, 73, 48, 2, 91, 33, 59, 84, 12]
VAL_ONE = 25
VAL_TWO = 47
NEW_VAL = 2


class TestLeftistTree:
    def __init__(self):
        self.test_left_tree = LeftistTree()
        self.node_to_delete = None

        self.start_time = None
        self.stop_time = None

    def print_tree(self):
        print(self.test_left_tree)

    def reset_times(self):
        self.start_time = None
        self.stop_time = None

    def calc_time(self):
        return (self.stop_time - self.start_time) * 1000

    def test_make_heap(self):
        self.reset_times()
        self.start_time = timer()
        self.test_left_tree.make_heap()
        self.stop_time = timer()

        return self.calc_time()

    def test_minimum(self):
        self.reset_times()
        self.start_time = timer()
        self.test_left_tree.minimum()
        self.stop_time = timer()

        return self.calc_time()

    def test_full_insert(self, seed=42):
        random.seed(seed)
        samples = random.sample(range(AUTO_RANGE_START, AUTO_RANGE_STOP), AUTO_SAMPLES_CNT)

        # perform inserts and calculate time
        self.reset_times()
        self.start_time = timer()
        for sample in samples:
            self.test_left_tree.insert(sample)
        self.stop_time = timer()
        del samples
        return self.calc_time()

    def test_extract_min(self):
        self.reset_times()
        self.start_time = timer()
        self.test_left_tree.extract_min()
        self.stop_time = timer()

        return self.calc_time()

    def test_single_insert(self):
        random.seed(42)
        sample = random.randint(AUTO_RANGE_START, AUTO_RANGE_STOP)

        # perform inserts and calculate time
        self.reset_times()
        self.start_time = timer()
        self.node_to_delete = self.test_left_tree.insert(sample)
        self.stop_time = timer()
        return self.calc_time()

    def test_delete(self):
        # take node from insert to delete
        if self.node_to_delete is not None:
            self.reset_times()
            self.start_time = timer()
            self.test_left_tree.delete(self.node_to_delete)
            self.stop_time = timer()
            self.node_to_delete = None

            return self.calc_time()
        else:
            print("DELETE ... unable to delete. No node given.")
            return

    def test_decrease_key(self):
        random.seed(42)
        # make sure to get a random number that is smaller (or equal) than the current value
        cur_val = self.node_to_delete.value
        new_val = random.randint(AUTO_RANGE_START, cur_val+1)

        # take node from insert to decrease
        if self.node_to_delete is not None:
            self.reset_times()
            self.start_time = timer()
            self.test_left_tree.decrease_key(self.node_to_delete, new_val)
            self.stop_time = timer()
            self.node_to_delete = None

            return self.calc_time()
        else:
            print("DECREASE_KEY ... unable to decrease the key. No node given.")
            return

    def automate_test(self):
        make_heap_time = 0.0
        full_insert_time = 0.0
        minimum_time = 0.0
        extract_min_time = 0.0
        single_insert_one_time = 0.0
        delete_time = 0.0
        single_insert_two_time = 0.0
        decrease_key_time = 0.0

        for i in range(ITER):
            make_heap_time += self.test_make_heap()
            full_insert_time += self.test_full_insert(i)

            minimum_time += self.test_minimum()
            extract_min_time += self.test_extract_min()

            # INSERT followed by a DELETE, because a pointer is needed to delete
            single_insert_one_time += self.test_single_insert()
            delete_time += self.test_delete()

            # INSERT followed by a DECREASE_KEY, because a pointer is needed to decrease a key
            single_insert_two_time += self.test_single_insert()
            decrease_key_time += self.test_decrease_key()

        print(f"The automated test with random numbers is going to run {ITER} times.")
        print("################### LEFTIST TREE TIMES ###################\n")

        print(f"MAKE HEAP: {make_heap_time/ITER} ms\n")
        print(f"FULL INSERT: {full_insert_time / ITER} ms\n")

        print(f"MINIMUM: {minimum_time / ITER} ms\n")
        print(f"EXTRACT MIN: {extract_min_time / ITER} ms\n")

        print(f"SINGLE INSERT 1: {single_insert_one_time / ITER} ms\n")
        print(f"DELETE: {delete_time / ITER} ms\n")

        print(f"SINGLE INSERT 2: {single_insert_two_time / ITER} ms\n")
        print(f"DECREASE KEY: {decrease_key_time / ITER} ms\n")

        print("##########################################################\n")
        del self.test_left_tree
        self.test_left_tree = LeftistTree()

    def functional_test(self):
        # MAKE HEAP
        print("MAKE HEAP\n")
        self.test_left_tree.make_heap()

        # INSERT
        print("\nINSERT\n")
        for sample in SAMPLES:
            self.test_left_tree.insert(sample)
            # self.print_tree()
        self.print_tree()

        # MINIMUM
        print("\nMINIMUM\n")
        mini = self.test_left_tree.minimum()
        print(f"minimum: {mini}")

        # EXTRACT MIN
        print("\nEXTRACT_MIN\n")
        self.test_left_tree.extract_min()
        self.print_tree()

        # DELETE (insert needed)
        print("\nDELETE\n")
        print(f"first insert {VAL_ONE}\n")
        node = self.test_left_tree.insert(VAL_ONE)
        self.print_tree()
        print(f"\nthen delete insert {VAL_ONE}\n")
        self.test_left_tree.delete(node)
        self.print_tree()

        # DECREASE_KEY (insert needed)
        print("\nDECREASE_KEY\n")
        print(f"first insert {VAL_TWO}\n")
        node = self.test_left_tree.insert(VAL_TWO)
        self.print_tree()
        print(f"\nthen decrease the key of {VAL_TWO} to the new value {NEW_VAL}\n")
        self.test_left_tree.decrease_key(node, NEW_VAL)
        self.print_tree()
