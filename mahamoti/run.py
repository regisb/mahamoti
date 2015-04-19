#!/usr/bin/env python
import argparse

from .views import app

def main():
    parser = argparse.ArgumentParser(description="Mahamoti server runner")
    parser.add_argument("--debug", action="store_true", default=False, help="Activate debug mode")
    args = parser.parse_args()

    app.debug = args.debug
    app.run()

if __name__ == "__main__":
    main()
