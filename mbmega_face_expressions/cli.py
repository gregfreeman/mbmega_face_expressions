"""Console script for mbmega_face_expressions."""
import argparse
import sys
from mbmega_face_expressions.controller import Controller
import asyncio as aio


def main():
    """Console script for mbmega_face_expressions."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "mbmega_face_expressions.cli.main")
    controller = Controller()
    loop = aio.get_event_loop()
    loop.run_forever()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
