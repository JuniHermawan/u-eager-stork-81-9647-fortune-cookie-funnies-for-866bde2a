"""Fortune Cookie Funnies for Engineers — make.fun entry. Writes one funny line into /output/entry.txt (OUTPUT_DIR env override for local runs). Stdlib only, deterministic, no network, no randomness, no clock."""
import os
LINE = ("Your code will compile on the first try today. Ask no questions. Touch nothing. Walk away slowly.")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
def main() -> None:
    assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == LINE, "entry.txt does not match the line"
    print(LINE)
if __name__ == "__main__":
    main()
