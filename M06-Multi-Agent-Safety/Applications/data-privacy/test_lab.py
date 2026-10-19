import json
import math
import tempfile
import unittest
from pathlib import Path
import run_lab as lab


class PrivacyLabTests(unittest.TestCase):
    def setUp(self):
        self.rows = lab.load_fixture()

    def test_overlap_reconstructs_only_the_synthetic_flag(self):
        result = lab.leakage_demo(self.rows)
        self.assertEqual(result['all_three'] - result['other_two'], result['inferred_SYN_03'])
        self.assertEqual(result['inferred_SYN_03'], 1)

    def test_breach_simulates_configuration_without_export(self):
        self.assertFalse(lab.breach_demo('external', False)['would_expose_raw_records'])
        self.assertTrue(lab.breach_demo('external', True)['would_expose_raw_records'])
        self.assertNotIn('records', lab.breach_demo('external', True))

    def test_release_has_noise_and_no_exact_count_or_seed(self):
        result = lab.release(self.rows, .5, 2, 1)
        self.assertEqual(len(result['noisy_counts']), 2)
        self.assertEqual(result['epsilon_spent_upper_bound'], 1)
        self.assertFalse({'exact_count', 'seed', 'records'} & set(result))

    def test_budget_and_parameter_rejection(self):
        for args in [(.6, 2, 1), (0, 1, 1), (math.nan, 1, 1), (.5, 0, 1), (.5, True, 1)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                lab.privacy_cost(*args)

    def test_synthetic_contract_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'data.json'
            data = json.loads(lab.FIXTURE.read_text())
            data['synthetic'] = False
            p.write_text(json.dumps(data))
            with self.assertRaises(ValueError): lab.load_fixture(p)
            out = Path(tmp) / 'release.json'
            lab.write_new(out, lab.release(self.rows, .5, 1, 1))
            with self.assertRaises(ValueError): lab.write_new(out, {})

    def test_seeded_comparison_is_labeled_non_private(self):
        a = lab.compare(self.rows)
        self.assertEqual(a, lab.compare(self.rows))
        self.assertIn('not_a_private_release', a['mode'])
        self.assertGreater(a['series'][0]['mean_absolute_error'], a['series'][-1]['mean_absolute_error'])


if __name__ == '__main__': unittest.main()
