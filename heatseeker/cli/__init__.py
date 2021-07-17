from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS
from . import (
    index,
    project
)

DESC = """

        <<<---------- Heatseeker Help -------------->>>

List of Commands:
     
     init  --> initializes the heatseeker project
     index --> creates an index file of your project structure 
"""


def parse_args():
    parser = ArgumentParser(description=DESC, formatter_class=RawTextHelpFormatter, usage=SUPPRESS)
    sub_parsers = parser.add_subparsers(dest='command')
    sub_parsers.required = True

    init_parser = sub_parsers.add_parser('init')
    init_parser.set_defaults(func=project.init)
    init_parser.add_argument('--destroy',
                             action='store_true',
                             default=False,
                             help='Flag destroys the current project config and makes fresh one')

    index_parser = sub_parsers.add_parser('index')
    index_parser.set_defaults(func=index.index)

    return parser.parse_args()
