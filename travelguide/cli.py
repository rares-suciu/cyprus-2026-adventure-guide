import argparse

def main():
    parser = argparse.ArgumentParser(prog="travelguide")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("build")
    subparsers.add_parser("serve")
    subparsers.add_parser("new")

    args = parser.parse_args()

    if args.command == "build":
        print("Build command")
    elif args.command == "serve":
        print("Serve command")
    elif args.command == "new":
        print("New command")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()