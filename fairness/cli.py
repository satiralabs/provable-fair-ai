"""
ProvableFair AI CLI: Command-line interface for mathematical fairness audits.
"""

import argparse
import json
import os
import sys
from .metrics import FairnessAuditor
from .prover import AuditProver


def cmd_audit(args):
    if not os.path.exists(args.file):
        print(f"Error: Dataset file not found at {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        data = json.load(f)

    auditor = FairnessAuditor(data)
    results = auditor.audit(
        unprivileged_group=args.unprivileged,
        privileged_group=args.privileged,
    )
    print(json.dumps(results, indent=2))


def cmd_commit(args):
    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        data = json.load(f)

    proof = AuditProver.create_commitment(data, args.salt)
    print(json.dumps(proof, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="provable-fair-ai",
        description="ProvableFair AI: Algorithmic Fairness Audit & Cryptographic Verification",
    )
    subparsers = parser.add_subparsers(dest="command")

    p_aud = subparsers.add_parser("audit", help="Audit dataset against algorithmic fairness metrics")
    p_aud.add_argument("--file", "-f", required=True, help="Path to JSON dataset of decision records")
    p_aud.add_argument("--unprivileged", default="unprivileged")
    p_aud.add_argument("--privileged", default="privileged")
    p_aud.set_defaults(func=cmd_audit)

    p_com = subparsers.add_parser("commit", help="Generate a cryptographic commitment hash")
    p_com.add_argument("--file", "-f", required=True)
    p_com.add_argument("--salt", "-s", required=True)
    p_com.set_defaults(func=cmd_commit)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
