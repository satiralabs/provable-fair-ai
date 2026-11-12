"""
ProvableFair Metrics: Evaluates bias and disparity metrics on decision models.
Zero external scientific libraries required.
"""

from typing import Any, Dict, List


class FairnessAuditor:
    """Computes standard regulatory fairness metrics for binary decision systems."""

    def __init__(self, records: List[Dict[str, Any]]):
        """
        records: List of dicts, each containing:
          - 'group': string (e.g. 'unprivileged' or 'privileged')
          - 'actual': int (1 or 0 ground truth)
          - 'predicted': int (1 or 0 decision)
        """
        self.records = records

    def audit(self, unprivileged_group: str = "unprivileged", privileged_group: str = "privileged") -> Dict[str, Any]:
        unpriv = [r for r in self.records if r.get("group") == unprivileged_group]
        priv = [r for r in self.records if r.get("group") == privileged_group]

        if not unpriv or not priv:
            return {"error": "Both groups must have representative records"}

        # Selection rates (Positive prediction rate)
        sr_unpriv = sum(1 for r in unpriv if r.get("predicted") == 1) / len(unpriv)
        sr_priv = sum(1 for r in priv if r.get("predicted") == 1) / len(priv)

        # Statistical Parity Difference (Goal: 0.0)
        stat_parity_diff = round(sr_unpriv - sr_priv, 4)

        # Disparate Impact Ratio (EEOC 80% Rule: should be between 0.80 and 1.25)
        disparate_impact = round(sr_unpriv / sr_priv, 4) if sr_priv > 0 else 0.0
        passes_four_fifths_rule = 0.80 <= disparate_impact <= 1.25

        # True Positive Rates (Equal Opportunity)
        unpriv_pos = [r for r in unpriv if r.get("actual") == 1]
        priv_pos = [r for r in priv if r.get("actual") == 1]

        tpr_unpriv = sum(1 for r in unpriv_pos if r.get("predicted") == 1) / len(unpriv_pos) if unpriv_pos else 0.0
        tpr_priv = sum(1 for r in priv_pos if r.get("predicted") == 1) / len(priv_pos) if priv_pos else 0.0
        equal_opportunity_diff = round(tpr_unpriv - tpr_priv, 4)

        return {
            "unprivileged_group": unprivileged_group,
            "privileged_group": privileged_group,
            "unprivileged_count": len(unpriv),
            "privileged_count": len(priv),
            "selection_rate_unprivileged": round(sr_unpriv, 4),
            "selection_rate_privileged": round(sr_priv, 4),
            "statistical_parity_diff": stat_parity_diff,
            "disparate_impact_ratio": disparate_impact,
            "passes_four_fifths_rule": passes_four_fifths_rule,
            "equal_opportunity_diff": equal_opportunity_diff,
            "compliance_status": "COMPLIANT" if passes_four_fifths_rule else "NON_COMPLIANT",
        }
