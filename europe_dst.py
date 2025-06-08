from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import sys


def get_next_dst_transition(tz_name: str) -> datetime | None:
    """Return the next DST transition time for the given timezone."""
    tz = ZoneInfo(tz_name)
    now = datetime.now(tz)
    current_offset = now.utcoffset()
    # check up to one year ahead for a transition
    for day_offset in range(1, 366):
        candidate = now + timedelta(days=day_offset)
        if candidate.utcoffset() != current_offset:
            return candidate
    return None


def main() -> None:
    tz_name = sys.argv[1] if len(sys.argv) > 1 else "Europe/Athens"
    try:
        tz = ZoneInfo(tz_name)
    except Exception as exc:
        sys.exit(f"Unknown timezone {tz_name}: {exc}")

    now = datetime.now(tz)
    print(f"Current time in {tz_name}: {now:%Y-%m-%d %H:%M:%S %Z%z}")

    next_transition = get_next_dst_transition(tz_name)
    if next_transition:
        print(
            "Next DST transition occurs on"
            f" {next_transition:%Y-%m-%d %H:%M:%S %Z%z}"
        )
    else:
        print("No DST transition found in the next year.")


if __name__ == "__main__":
    main()
