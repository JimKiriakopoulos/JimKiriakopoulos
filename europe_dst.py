"""Display daylight saving time transitions for European timezones.

The script focuses on the default ``Europe/Athens`` zone but it can report
transitions for any European timezone supported by :mod:`zoneinfo`. It prints
the current local time in the selected zone and lists every daylight saving
change that will occur within the chosen interval (one year by default).

Extra helper options make it easy to explore all European timezones and limit
how many transitions are shown.  Output now includes the change in UTC offset
so it is immediately clear how the clocks will move.
"""

from __future__ import annotations

import argparse
import sys
import datetime as dt
from dataclasses import dataclass
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError, available_timezones


@dataclass
class Transition:
    """Container describing a daylight saving time change."""

    moment: dt.datetime
    previous_offset: dt.timedelta
    new_offset: dt.timedelta

    @property
    def offset_change(self) -> dt.timedelta:
        """Return the difference between the new and previous offsets."""

        return self.new_offset - self.previous_offset

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
    tz_name: str,
    start: dt.datetime,
    end: dt.datetime,
    limit: int | None = None,
) -> list[Transition]:
    """Return all DST transitions between ``start`` and ``end``.

    Parameters
    ----------
    tz_name:
        Name of the timezone to inspect.
    start, end:
        Inclusive range for the search.
    limit:
        Maximum number of transitions to return. ``None`` keeps searching until
        the ``end`` instant.
    """

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
            if limit is not None and len(transitions) >= limit:
                break
            continue
        current = nxt

    return transitions


def _format_offset(offset: dt.timedelta) -> str:
    """Return ``offset`` in ``UTC±HH:MM`` form."""

    total_minutes = int(offset.total_seconds() // 60)
    sign = "-" if total_minutes < 0 else "+"
    total_minutes = abs(total_minutes)
    hours, minutes = divmod(total_minutes, 60)
    return f"UTC{sign}{hours:02d}:{minutes:02d}"


def _iter_european_timezones() -> list[str]:
    """Return the available timezones within the ``Europe/`` namespace."""

    return sorted(zone for zone in available_timezones() if zone.startswith("Europe/"))


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
        "--limit",
        type=int,
        default=None,
        help="Maximum number of transitions to display",
    )
    parser.add_argument(
        "--until",
        help="ISO timestamp to stop searching (overrides --days)",
    )
    parser.add_argument(
        "--start",
        help="ISO timestamp to begin searching from",
    )
    parser.add_argument(
        "--list-zones",
        action="store_true",
        help="List all Europe/* timezones and exit",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.list_zones:
        print("Available European timezones:")
        for name in _iter_european_timezones():
            print(f"  {name}")
        return

    tz_name = args.zone
    if not tz_name.startswith("Europe/"):
        sys.exit("This script only supports Europe/* timezones.")

    if args.limit is not None and args.limit <= 0:
        sys.exit("--limit must be a positive integer")
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

    transitions = find_dst_transitions(tz_name, start, end, limit=args.limit)
    if transitions:
        print("Upcoming DST changes:")
        for transition in transitions:
            moment = transition.moment
            old_offset = _format_offset(transition.previous_offset)
            new_offset = _format_offset(transition.new_offset)
            change = transition.offset_change
            change_hours = change.total_seconds() / 3600
            if change_hours.is_integer():
                change_str = f"{int(change_hours):+d}h"
            else:
                change_str = f"{change_hours:+.2f}h"
            print(
                "  "
                f"{moment:%Y-%m-%d %H:%M:%S %Z%z} - DST {transition.action}"
                f" ({old_offset} → {new_offset}, {change_str})"
            )
    else:
        span = (end - start).days
        print(f"No DST change found in the next {span} days.")


if __name__ == "__main__":
    main()
