from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS
from . import index

DESC = """

        <<<---------- Heatseeker Help -------------->>>

List of Commands:

     index --> creates an index file of your project structure 
"""


def parse_args():
    parser = ArgumentParser(description=DESC, formatter_class=RawTextHelpFormatter, usage=SUPPRESS)
    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    index_parser = sub_parsers.add_parser('index')
    index_parser.set_defaults(func=index.index)

    return parser.parse_args()
