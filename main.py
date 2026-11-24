import os

LINE = ("You describe the app you want in plain words, an AI agent "
        "builds it while you watch, and you can change anything by "
        "just saying so — no code, no waiting months, no hiring anyone.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
