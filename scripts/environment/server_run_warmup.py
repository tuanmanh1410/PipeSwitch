import os
import sys

from scripts.common.util import RunDocker

def main():
    with RunDocker('pipeswitch:ready_model', 'warm_up') as rd:
        # Start the server: ready_model
        rd.run('python PipeSwitch/scripts/environment/container_run_warmup.py')
        
        # Get and return the data point

if __name__ == '__main__':
    main()