from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def next_dst_change(tz_name: str = "Europe/Athens") -> datetime | None:
    """Return the exact datetime of the next DST change for Greece."""
    tz = ZoneInfo(tz_name)
    now = datetime.now(tz).replace(minute=0, second=0, microsecond=0)
    initial_offset = now.utcoffset()
    # search for a change within the next year using hourly increments
    limit = now + timedelta(days=366)
    while now < limit:
        now += timedelta(hours=1)
        if now.utcoffset() != initial_offset:
            return now
    return None


if __name__ == "__main__":
    timezone = "Europe/Athens"
    now = datetime.now(ZoneInfo(timezone))
    print(f"Τρέχουσα ώρα στην Ελλάδα: {now:%Y-%m-%d %H:%M:%S %Z%z}")
    change = next_dst_change(timezone)
    if change:
        print(
            "Η επόμενη αλλαγή ώρας είναι στις",
            f"{change:%Y-%m-%d %H:%M:%S %Z%z}",
        )
    else:
        print("Δε βρέθηκε αλλαγή ώρας μέσα στον επόμενο χρόνο.")
