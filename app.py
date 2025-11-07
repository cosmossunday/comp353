"""
Simple CLI for calculator operations.
Usage:
  python app.py add 2 3
  python app.py sub 5 2
  python app.py mul 4 2
  python app.py div 8 4
"""
import argparse, sys, calculator as calc

def main(argv=None):
    parser = argparse.ArgumentParser(description="Calculator CLI (Git practice)")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for op in ("add", "sub", "mul", "div"):
        p = sub.add_parser(op)
        p.add_argument("a", type=float)
        p.add_argument("b", type=float)
    args = parser.parse_args(argv)
    a, b = args.a, args.b
    try:
        print(getattr(calc, args.cmd)(a, b))
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
