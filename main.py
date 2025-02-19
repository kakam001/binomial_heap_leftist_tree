from test_left_tree import TestLeftistTree
from test_binomial_heap import TestBinomialHeap


def mainloop():
    ####################  LEFTIST TREE  #######################

    # leftist_test = TestLeftistTree()
    # leftist_test.automate_test()

    leftist_func_test = TestLeftistTree()
    leftist_func_test.functional_test()

    ###########################################################

    ####################  BINOMIAL HEAP  ######################

    # binomial_test = TestBinomialHeap()
    # binomial_test.automate_test()

    binomial_func_test = TestBinomialHeap()
    binomial_func_test.functional_test()

    ###########################################################


if __name__ == '__main__':
    mainloop()
