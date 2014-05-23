#!/usr/bin/env python
'''contains method for creating a parser set up for splatfilch'''


import argparse

def splatfilch_argparser():
    '''return an argparser parser, configured for splatfilch'''
    # create the top-level parser
    parser = argparse.ArgumentParser(prog='splatfilch',
        description="For help with a specific command, run 'Splatfilch.py \
            {argument} --help', using one of the arguments below:")

    # create subparser object to manage subparsers
    subp = parser.add_subparsers(dest="mode")

    # "update" subparser
    sp_update = subp.add_parser('update',
        description="Filch any content uploaded since the last run, from all \
            tracked sources.",
        help="Download new content from all sources since last run.")

    sp_update.add_argument('-s', '--stderr', action='store_true',
        help="print to screen instead of creating a log file")
    sp_update.add_argument('-v', '--verbosity', action='count', default=0,
        help="increase output verbosity [-v, -vv, -vvv]")

    # "source" subparser
    sp_source = subp.add_parser('source',
        help="Actions for managing tracked sources",
        description="Actions for managing tracked sources.")

    # subparsers for each "source" action (list, search, remove)
    sp_source_modes = sp_source.add_subparsers(dest="source_mode")

    # pylint: disable=unused-variable
    sp_source_list = sp_source_modes.add_parser('list',
        help="Print a list of all tracked sources")
    sp_source_search = sp_source_modes.add_parser('search',
        help="Search for a channel by name")
    sp_source_search.add_argument('search_term',
        help="Name of channel to search for")
    sp_source_remove = sp_source_modes.add_parser('remove',
        help="Remove a source (by name, or by place in list)")
    sp_source_remove.add_argument('channel',
        help="Name (or number in list) of channel to remove")
    sp_source.add_argument('-v', '--verbosity', action='count', default=0,
        help="increase output verbosity [-v, -vv, -vvv]")

    return parser

if __name__ == "__main__":
    args = splatfilch_argparser().parse_args()
    print args

