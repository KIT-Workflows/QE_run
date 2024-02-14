# Quantum ESPRESSO Runner

**Version:** 0.0.1

**Author:** J. Schaarschmidt

## Description

This script automates the process of running Quantum ESPRESSO calculations. It reads parameters from a YAML file, sets up the environment, and executes the Quantum ESPRESSO calculation using MPI for parallel execution. The output is saved to a specified file.

## Inputs

- `rendered_wano.yml`: A YAML file containing the input parameters for the Quantum ESPRESSO calculation, including the input file name.

## Outputs

- A file with a `*.pwo` extension where the results of the Quantum ESPRESSO calculation will be saved.
