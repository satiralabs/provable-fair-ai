"""
ProvableFair Prover: Cryptographic commit-reveal scheme for verifiable model auditing.
Enables proving that audit results correspond to an un-tampered test split.
"""

import hashlib
import hmac
import json
import time
from typing import Any, Dict, List


def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


class AuditProver:
    """Creates tamper-proof cryptographic commitments for model evaluation runs."""

    @staticmethod
    def create_commitment(dataset: List[Dict[str, Any]], salt: str) -> Dict[str, str]:
        dataset_json = json.dumps(dataset, sort_keys=True, separators=(",", ":"))
        dataset_hash = sha256_hash(dataset_json)
        commitment = hmac.new(salt.encode("utf-8"), dataset_hash.encode("utf-8"), hashlib.sha256).hexdigest()
        return {
            "commitment_hash": commitment,
            "dataset_rows": str(len(dataset)),
            "created_at": str(time.time()),
        }

    @staticmethod
    def verify_reveal(dataset: List[Dict[str, Any]], salt: str, commitment_hash: str) -> bool:
        dataset_json = json.dumps(dataset, sort_keys=True, separators=(",", ":"))
        dataset_hash = sha256_hash(dataset_json)
        computed = hmac.new(salt.encode("utf-8"), dataset_hash.encode("utf-8"), hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed, commitment_hash)
