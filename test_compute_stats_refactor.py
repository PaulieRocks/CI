import unittest
import compute_stats_refactor

class test_compute_stats_refactor(unittest.TestCase):

    def test_accuracy_of_harmonic_mean_three_positive_numbers(self):
        list_ints=[1,2,3]
        self.assertAlmostEqual(compute_stats_refactor.compute_harmonic_mean(list_ints),1.636363637,8)



