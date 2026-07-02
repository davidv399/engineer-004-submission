#!/usr/bin/env python3
"""Simple event simulator for the Engineer 004 submission artifact.

This script generates a small batch of synthetic analytics events to illustrate
how the proposed pipeline would ingest and normalize incoming traffic.
"""
import json
import random
from datetime import datetime, timezone
from pathlib import Path

random.seed(42)

TENANTS = ["tenant-a", "tenant-b", "tenant-c"]
EVENT_TYPES = ["page_view", "click", "form_submit", "custom_event"]


def build_event(tenant: str, index: int) -> dict:
    return {
        "tenant_id": tenant,
        "event_id": f"evt-{index:06d}",
        "event_type": random.choice(EVENT_TYPES),
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "anonymous_id": f"anon-{random.randint(1000, 9999)}",
        "user_id": None,
        "session_id": f"sess-{random.randint(10000, 99999)}",
        "device_id": f"device-{random.randint(1, 10)}",
        "properties_json": json.dumps({"path": "/pricing", "value": random.randint(1, 5)}),
        "source_sdk_version": "1.2.0",
        "schema_version": 1,
    }


def main() -> None:
    events = [build_event(tenant, i) for i, tenant in enumerate(TENANTS * 3)]
    output_path = Path(__file__).with_name("sample_events.json")
    output_path.write_text(json.dumps(events, indent=2), encoding="utf-8")
    print(f"Wrote {len(events)} synthetic events to {output_path}")


if __name__ == "__main__":
    main()
