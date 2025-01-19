#!/usr/bin/env python3
import argparse
import sys

# Check for arguments
if len(sys.argv) == 1:
    # no arguments supplied, load the console.
    from interfaces.console import Console
    Console().cmdloop()
    sys.exit()

parser = argparse.ArgumentParser()

parser.add_argument_group()

parser.add_argument(
    "--console",
    action="store_true",
    help="start the console, all other args will be ignored"
)

parser.add_argument(
    "--json",
    required=True,
    help="path to the json to parse"
)

parser.add_argument(
    "--out-path",
    required=True,
    help="path to the json to parse"
)

parser.add_argument(
    "--store-db",
    action="store_true",
    help="add the generated ca/certs to the db"
)

args = parser.parse_args()

# First, check for console and if set, drop to it
# or go to noninteractive mode and parse the args
if args.console:
    from interfaces.console import Console
    Console().cmdloop()
else:
    from interfaces.noninteractive import Noninteractive
    Noninteractive(args)
