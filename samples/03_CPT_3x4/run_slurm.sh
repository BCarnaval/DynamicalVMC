#!/usr/bin/env bash
#SBATCH --job-name=3x4_CPT_dVMC
#SBATCH --account=def-charleb1
#SBATCH --mem-per-cpu=1G
#SBATCH --ntasks=64
#SBATCH --cpus-per-task=1
#SBATCH --time=00-00:45           # time (DD-HH:MM)


main () {
    # Setting env variables
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
    export DVMC_MPI_PROC=${SLURM_NTASKS}

    # Setting working directory
    RUNDIR="/home/${USER}/scratch/${SLURM_JOB_NAME}_${SLURM_JOB_ID}"

    if [[ -d ${RUNDIR} ]]; then
        rm -rf ${RUNDIR}
        mkdir ${RUNDIR}
    else
        mkdir ${RUNDIR}
    fi

    cd ${RUNDIR}

    # Copy files to working directory
    cp ${SLURM_SUBMIT_DIR}/params .
    cp ${SLURM_SUBMIT_DIR}/model_3x4.py .
    cp ${SLURM_SUBMIT_DIR}/fermi_surface.py .

    # Execute the calculations
    python3 fermi_surface.py
}

main
