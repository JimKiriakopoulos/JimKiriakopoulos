"""Display daylight saving time transitions for European timezones.

The script focuses on the default ``Europe/Athens`` zone but it can report
transitions for any European timezone supported by :mod:`zoneinfo`. It prints
the current local time in the selected zone and lists every daylight saving
change that will occur within the chosen interval (one year by default).
"""

from __future__ import annotations

import argparse
import sys
import datetime as dt
from dataclasses import dataclass
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


@dataclass
class Transition:
    """Container describing a daylight saving time change."""

    moment: dt.datetime
    previous_offset: dt.timedelta
    new_offset: dt.timedelta

    @property
    def action(self) -> str:
        """Return ``"starts"`` if DST begins, otherwise ``"ends"``."""

        return "starts" if self.new_offset > self.previous_offset else "ends"


def _narrow_transition(
    tz: ZoneInfo,
    low: dt.datetime,
    high: dt.datetime,
    old_offset: dt.timedelta,
) -> Transition:
    """Binary search to pinpoint the DST change moment."""

    precision = dt.timedelta(seconds=1)
    while high - low > precision:
        mid = low + (high - low) / 2
        if (mid.utcoffset() or dt.timedelta()) == old_offset:
            low = mid
        else:
            high = mid

    new_offset = high.utcoffset() or dt.timedelta()
    return Transition(moment=high, previous_offset=old_offset, new_offset=new_offset)


def find_dst_transitions(
    tz_name: str, start: dt.datetime, end: dt.datetime
) -> list[Transition]:
    """Return all DST transitions between ``start`` and ``end``."""

    tz = ZoneInfo(tz_name)
    current = start.astimezone(tz)
    step = dt.timedelta(days=1)
    offset = current.utcoffset() or dt.timedelta()
    transitions: list[Transition] = []

    while current < end:
        nxt = min(current + step, end)
        if (nxt.utcoffset() or dt.timedelta()) != offset:
            transition = _narrow_transition(tz, current, nxt, offset)
            transitions.append(transition)
            offset = transition.new_offset
            current = transition.moment
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
            start = dt.datetime.fromisoformat(args.start)
        except ValueError as exc:
            sys.exit(f"Invalid --start value: {exc}")
        start = start.replace(tzinfo=tz) if start.tzinfo is None else start.astimezone(tz)
    else:
        start = dt.datetime.now(tz)

    if args.until:
        try:
            end = dt.datetime.fromisoformat(args.until)
        except ValueError as exc:
            sys.exit(f"Invalid --until value: {exc}")
        end = end.replace(tzinfo=tz) if end.tzinfo is None else end.astimezone(tz)
    else:
        if args.days < 0:
            sys.exit("--days must be non-negative")
        end = start + dt.timedelta(days=args.days)

    if end <= start:
        sys.exit("--until must be after --start")

    print(f"Current time in {tz_name}: {start:%Y-%m-%d %H:%M:%S %Z%z}")

    transitions = find_dst_transitions(tz_name, start, end)
    if transitions:
        print("Upcoming DST changes:")
        for transition in transitions:
            moment = transition.moment
            print(
                f"  {moment:%Y-%m-%d %H:%M:%S %Z%z} - DST {transition.action}"
            )
    else:
        span = (end - start).days
        print(f"No DST change found in the next {span} days.")


if __name__ == "__main__":
    main()
