<div align="center">

# dVMC + CDMFT calculation sample

</div>

This directory contains a direct application of the dVMC software to
compute the ground state of a 1D cluster of 2 sites with 4 bath sites then using
the Q-matrix representation in cluster dynamical mean field theory (CDMFT)
from PyQCM library.

## Content

- `general_bath_1D.py`: Defines 1D lattice models using PyQCM library instances.

- `params`: Global dVMC solver input parameter file.

- `expected/`: Directory containing expected results from the dVMC + CDMFT calculations.

## Usage

Since this example uses dVMC through PyQCM, the only thing to do is to execute
the `general_bath_1D.py` script using Python 3 (with proper PyQCM installation)

#### Run script to generate A(k,w) from dVMC + CDMFT

```shell
python3 general_bath_1D.py
```

## Post processing

To clean the directory from generated files that would be overwritten by the program,
use the `dvmc` command line interface

```shell
dvmc clean --help
```