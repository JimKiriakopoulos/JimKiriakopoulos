"""Display daylight saving time transitions for a European timezone.

This script prints the current time in the chosen zone (``Europe/Athens`` by
default) and lists all DST changes that will occur within a configurable
time range (one year by default). The search can also be bounded by a specific
end timestamp via ``--until``. Each change is reported with the exact
timestamp and whether daylight saving time starts or ends.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import argparse
import sys


def find_dst_transitions(tz_name: str, start: datetime, end: datetime) -> list[datetime]:
    """Return all DST transition datetimes between ``start`` and ``end``."""

    tz = ZoneInfo(tz_name)
    current = start.astimezone(tz)
    step = timedelta(days=1)
    offset = current.utcoffset() or timedelta()
    transitions: list[datetime] = []

    while current < end:
        nxt = min(current + step, end)
        if (nxt.utcoffset() or timedelta()) != offset:
            # Narrow down the exact change moment to one second precision
            low, high = current, nxt
            while high - low > timedelta(seconds=1):
                mid = low + (high - low) / 2
                if mid.utcoffset() == offset:
                    low = mid
                else:
                    high = mid
            transitions.append(high)
            offset = high.utcoffset() or timedelta()
            current = high
            continue
        current = nxt

    return transitions


def parse_args() -> argparse.Namespace:
    """Return parsed command line arguments."""
    parser = argparse.ArgumentParser(
        description="List upcoming daylight saving time changes for a timezone"
    )
    parser.add_argument(
        "zone",
        nargs="?",
        default="Europe/Athens",
        help="Timezone name, e.g. Europe/London",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=365,
        help="How many days ahead to search",
    )
    parser.add_argument(
        "--until",
        help="ISO timestamp to stop searching (overrides --days)",
    )
    parser.add_argument(
        "--start",
        help="ISO timestamp to begin searching from",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tz_name = args.zone
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError as exc:
        sys.exit(f"Unknown timezone {tz_name}: {exc}")

    if args.start:
        try:
            start = datetime.fromisoformat(args.start)
        except ValueError as exc:
            sys.exit(f"Invalid --start value: {exc}")
        start = start.replace(tzinfo=tz) if start.tzinfo is None else start.astimezone(tz)
    else:
        start = datetime.now(tz)

    if args.until:
        try:
            end = datetime.fromisoformat(args.until)
        except ValueError as exc:
            sys.exit(f"Invalid --until value: {exc}")
        end = end.replace(tzinfo=tz) if end.tzinfo is None else end.astimezone(tz)
    else:
        if args.days < 0:
            sys.exit("--days must be non-negative")
        end = start + timedelta(days=args.days)

    if end <= start:
        sys.exit("--until must be after --start")

    print(f"Current time in {tz_name}: {start:%Y-%m-%d %H:%M:%S %Z%z}")

    transitions = find_dst_transitions(tz_name, start, end)
    if transitions:
        print("Upcoming DST changes:")
        for trans in transitions:
            prev_offset = (trans - timedelta(minutes=1)).astimezone(tz).utcoffset() or timedelta()
            new_offset = trans.utcoffset() or timedelta()
            action = "starts" if new_offset > prev_offset else "ends"
            print(f"  {trans:%Y-%m-%d %H:%M:%S %Z%z} - DST {action}")
    else:
        span = (end - start).days
        print(f"No DST change found in the next {span} days.")


if __name__ == "__main__":
    main()
