"""Plots the Fermi surface of the model defined in 'model_3x4'
Python module using PyQCM library to invoke dVMC solver instead
of exact diagonalization.
"""
import pyqcm
import numpy as np
from model_3x4 import model
from dvmc import dvmc_solver
import matplotlib.pyplot as plt


def plot_results() -> None:
    """Plots the cluster spectral functions for both ED and
    dVMC impurity solver.
    """
    # Reading parameters as dictionnary
    pyqcm.solver = None
    params = dict(np.genfromtxt('./params', encoding='utf8', dtype=None))

    # Setting model parameters
    sector = f"R0:N{params['nelec']}:S0"
    model.set_target_sectors([sector])
    model.set_parameters(
        f"""
        U={params['U']}
        t={params['t']}
        tp={params['tp']}
        tpp={params['tpp']}
        mu={params['mu']}
        """
    )

    # dVMC part
    model_dvmc = pyqcm.model_instance(model)
    with open('./output/qmatrix.def') as qmatrix:
        dvmc_sol = qmatrix.read()
        qmatrix.close()

    model_dvmc.read(dvmc_sol, 0)
    w_dvmc, A_dvmc = model_dvmc.cluster_spectral_function(wmax=15, eta=0.1)

    # ED part
    model_ed = pyqcm.model_instance(model)
    w_ed, A_ed = model_ed.cluster_spectral_function(wmax=15)

    # Plotting both dVMC & ED solutions for cluster spectral functions
    dim = int(params['nelec']) // 3
    for i in range(dim):
        plt.plot(np.real(w_dvmc), A_dvmc[:, i] + 2 *
                 i, color='C5', lw=2, alpha=0.95)
        plt.plot(np.real(w_ed), A_ed[:, i] + 2 * i, color='C0')

    plt.yticks(2 * np.arange(0, dim), [str(i) for i in range(1, dim + 1)])
    plt.xlabel(r'$\omega$')
    plt.axvline(0, ls='solid', lw=0.5)
    plt.savefig("./spectrums.pdf", dpi=800)
    plt.close()

    return


def main() -> None:
    # Reading parameters as dictionnary
    params = dict(np.genfromtxt('./params', encoding='utf8', dtype=None))

    # Setting hamiltonian sector & lattice parameters
    sector = f"R0:N{params['nelec']}:S0"
    model.set_target_sectors([sector])
    model.set_parameters(
        f"""
        U={params['U']}
        t={params['t']}
        tp={params['tp']}
        tpp={params['tpp']}
        mu={params['mu']}
        """
    )

    f = open('sec', 'w')
    f.write(sector)
    f.close()

    # Setup dVMC solver through PyQCM
    pyqcm.solver = dvmc_solver
    model_instance = pyqcm.model_instance(model)

    # CPT DoS
    model_instance.mdc(eta=0.12,
                       quadrant=False,
                       freq=1.5970819385867554,
                       file='fermi_surface.pdf',
                       sym='RXY'
                       )

    return


if __name__ == "__main__":
    # main()
    plot_results()
