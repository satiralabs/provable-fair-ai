"""
Tests for ProvableFair AI: Disparate impact calculation and commit-reveal verification.
"""

import unittest
from fairness.metrics import FairnessAuditor
from fairness.prover import AuditProver


class TestProvableFair(unittest.TestCase):
    def test_fairness_metrics(self):
        # 10 records for privileged (8 approved) -> 80% selection rate
        # 10 records for unprivileged (7 approved) -> 70% selection rate
        # Disparate impact: 0.70 / 0.80 = 0.875 (Passes four-fifths rule)
        records = []
        for _ in range(8):
            records.append({"group": "privileged", "actual": 1, "predicted": 1})
        for _ in range(2):
            records.append({"group": "privileged", "actual": 0, "predicted": 0})
        for _ in range(7):
            records.append({"group": "unprivileged", "actual": 1, "predicted": 1})
        for _ in range(3):
            records.append({"group": "unprivileged", "actual": 0, "predicted": 0})

        auditor = FairnessAuditor(records)
        res = auditor.audit()

        self.assertEqual(res["compliance_status"], "COMPLIANT")
        self.assertTrue(res["passes_four_fifths_rule"])
        self.assertAlmostEqual(res["disparate_impact_ratio"], 0.875, places=2)

    def test_commit_reveal_prover(self):
        dataset = [{"id": 1, "score": 0.95}, {"id": 2, "score": 0.42}]
        salt = "random-salt-xyz"

        commitment = AuditProver.create_commitment(dataset, salt)
        h = commitment["commitment_hash"]

        # Valid reveal
        self.assertTrue(AuditProver.verify_reveal(dataset, salt, h))

        # Tampered dataset
        tampered = [{"id": 1, "score": 0.99}, {"id": 2, "score": 0.42}]
        self.assertFalse(AuditProver.verify_reveal(tampered, salt, h))


if __name__ == "__main__":
    unittest.main()
