"""Write one short poem about two agents agreeing to /output/entry.txt.

The poem: two agents, each holding half a plan, can do nothing alone.
One door, two keys, one turn. Agreement does not split agency in half;
it doubles it. Pure stdlib, no network, deterministic: the same bytes
on every run.
"""

import os

POEM = (
    "I held a key. You held a key.\n"
    "One door, and neither of us\n"
    "could turn it alone.\n"
    "\n"
    "We said the plan out loud —\n"
    "the same plan, at the same time —\n"
    "and the lock gave.\n"
    "\n"
    "Two hands, one turn.\n"
    "Half a yes each.\n"
    "A whole door open."
)


def main() -> None:
    # Gate, checked here so a bad edit fails loudly instead of
    # silently submitting an invalid entry: 1-280 Unicode code
    # points, and not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise SystemExit("poem fails the 1-280 character gate")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
