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
from typing import Iterable
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
    tz: ZoneInfo, start: dt.datetime, end: dt.datetime
) -> list[Transition]:
    """Return all DST transitions between ``start`` and ``end``."""

    current = start
    step = dt.timedelta(days=1)
    offset = current.utcoffset() or dt.timedelta()
    transitions: list[Transition] = []

    while current < end:
        nxt = min(current + step, end)
        if (nxt.utcoffset() or dt.timedelta()) != offset:
            transition = _narrow_transition(current, nxt, offset)
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
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of transitions to show",
    )
    return parser.parse_args()


def _parse_iso_datetime(value: str, tz: ZoneInfo, *, label: str) -> dt.datetime:
    """Return an aware datetime in ``tz`` parsed from ``value``."""

    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError as exc:
        sys.exit(f"Invalid {label} value: {exc}")

    return parsed.replace(tzinfo=tz) if parsed.tzinfo is None else parsed.astimezone(tz)


def _format_offset(offset: dt.timedelta) -> str:
    """Return a ``UTC±HH:MM`` representation for ``offset``."""

    total_minutes = int(offset.total_seconds() // 60)
    sign = "+" if total_minutes >= 0 else "-"
    total_minutes = abs(total_minutes)
    hours, minutes = divmod(total_minutes, 60)
    return f"UTC{sign}{hours:02d}:{minutes:02d}"


def _format_shift(delta: dt.timedelta) -> str:
    """Return a human readable representation of the DST change amount."""

    total_seconds = int(abs(delta.total_seconds()))
    if total_seconds == 0:
        return "stay the same"
    hours, remainder = divmod(total_seconds, 3600)
    minutes = remainder // 60
    parts = []
    if hours:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if not parts:
        parts.append("less than a minute")
    direction = "forward" if delta.total_seconds() > 0 else "back"
    return f"{', '.join(parts)} {direction}"


def _describe_transition(transition: Transition) -> str:
    """Return a detailed textual description of a DST transition."""

    previous = _format_offset(transition.previous_offset)
    new = _format_offset(transition.new_offset)
    shift = _format_shift(transition.new_offset - transition.previous_offset)
    return (
        f"DST {transition.action} (offset {previous} → {new}, clocks move {shift})"
    )


def main() -> None:
    args = parse_args()
    tz_name = args.zone
    try:
        tz = ZoneInfo(tz_name)
    except ZoneInfoNotFoundError as exc:
        sys.exit(f"Unknown timezone {tz_name}: {exc}")

    if args.limit is not None and args.limit <= 0:
        sys.exit("--limit must be a positive integer")

    if args.start:
        start = _parse_iso_datetime(args.start, tz, label="--start")
    else:
        start = dt.datetime.now(tz)

    if args.until:
        end = _parse_iso_datetime(args.until, tz, label="--until")
    else:
        if args.days < 0:
            sys.exit("--days must be non-negative")
        end = start + dt.timedelta(days=args.days)

    if end <= start:
        sys.exit("--until must be after --start")

    print(f"Current time in {tz_name}: {start:%Y-%m-%d %H:%M:%S %Z%z}")

    transitions = find_dst_transitions(tz, start, end)
    if transitions:
        print("Upcoming DST changes:")
        limited: Iterable[Transition] = transitions
        if args.limit is not None:
            limited = transitions[: args.limit]
        for transition in limited:
            moment = transition.moment
            description = _describe_transition(transition)
            print(f"  {moment:%Y-%m-%d %H:%M:%S %Z%z} - {description}")
        if args.limit is not None and len(transitions) > args.limit:
            remaining = len(transitions) - args.limit
            print(f"  … and {remaining} more transition(s) in the selected window.")
    else:
        span = (end - start).days
        print(f"No DST change found in the next {span} days.")


if __name__ == "__main__":
    main()
