"""
main python file for the GrAALF output processor.

This main can be called using the following keywords :

* -i --input : the input file
* -o --output dir : the output files directory : this is a directory as an input can result in multiple outputs
* -p --paths : does the path based model
* -c --components : does the connected components model

"""

import argparse
from src.__main__ import main

parser = argparse.ArgumentParser(description="Processes GrAALF's output into the path or connected components model",
                                 add_help='How to use', prog='python main.py <options>')

parser.add_argument("-i", "--input", dest="input_name", required=True, default=None,
                    help="Input file to be processed")

parser.add_argument("-o", "--output-dir", dest="output_dir", required=True, default=None,
                    help="output directory to store files")

parser.add_argument("-p", "--path", dest="path_based", default=False, action="store_true",
                    help="to process the input signatures and process output with paths")

parser.add_argument("-c", "--components", dest="component_based", default=False, action="store_true",
                    help="to process the input signatures and process output with connected components")

args = parser.parse_args()

main(args)
