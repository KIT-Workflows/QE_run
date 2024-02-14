import os
import subprocess
import yaml


def run_quantum_espresso(input_file, output_file):
    """
    Executes a Quantum ESPRESSO calculation using the specified input and output files.

    This function runs a Quantum ESPRESSO calculation with a given input file and directs
    the output to the specified output file.

    Parameters:
    input_file (str): The name of the input file for Quantum ESPRESSO (e.g., 'relax.pwi').
    output_file (str): The name of the output file where the results will be saved ('*.pwo').

    Writes to '*.pwo'.
    """

    os.environ['ESPRESSO_PSEUDO'] = os.getcwd()

    command = ["mpirun", "-np", "1", "pw.x", "-in", input_file]
    with open(output_file, 'w') as file:
        subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    with open("rendered_wano.yml", "r") as file:
        params = yaml.safe_load(file)

    input_file = params['input_file']
    output_file = '*.pwo'

    run_quantum_espresso(input_file, output_file)
