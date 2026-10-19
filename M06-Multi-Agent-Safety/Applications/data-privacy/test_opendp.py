import importlib.util
import math
import unittest
import run_opendp


@unittest.skipUnless(importlib.util.find_spec('opendp'), 'optional OpenDP not installed')
class OpenDPTests(unittest.TestCase):
    def test_synthetic_release_and_budget_split(self):
        result = run_opendp.run(1.0, 2)
        self.assertEqual(result['epsilon_per_query'], 0.5)
        self.assertEqual(len(result['noisy_sums']), 2)
        self.assertFalse({'exact_count', 'records', 'seed'} & set(result))

    def test_invalid_arguments_stop_before_query(self):
        for epsilon, queries in [(0, 1), (math.nan, 1), (1, 0), (1, 11)]:
            with self.subTest(epsilon=epsilon, queries=queries), self.assertRaises(ValueError):
                run_opendp.run(epsilon, queries)
