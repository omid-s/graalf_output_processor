# GrAALF Describe Processor

This module is designed to take GrAALF outputs as input and create either a set of paths or a sequence of connected
 components as output.
 
Path outputs are created by starting from leaf nodes defined as nodes for which the in degree is more than zero and
 the out degree is zero. Then any paths that lead to these nodes will become a part of the output   
 
# Install 

 to install `cd` to the directory of the tool then do : 
 
    pip install .
 
# Run

Main file for the project can be accessed by running 

    python main.py
 
in the tool's direcotry. main file accpets the following command arguments: 

    -h, --help            show this help message and exit
    -i INPUT_NAME, --input INPUT_NAME
                        Input file to be processed
    -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory to store files
    -p, --path            to process the input signatures and process output
                        with paths
    -c, --components      to process the input signatures and process output
                        with connected components
                        
                        
This tool will create the output directories if they do not exist and also will overwrite files of the same names. 
