# MSC_porject

## Repository structure:

* Qiskit, Puquil, Cirq folders:
    *  Folder 1~99: result of the system's last version
    *  xml file: statical information about results
    *  mutation_and_create.ipynb: Generate mutative seed programs and make equivalent circuits.
    *  execute_quantum_circuits.ipynb: Execute circuits in each folder and save the results(csv files) in each folder.
    *  collect_and_evaluation.ipynb: Collect results and evaluate them.

## Running the system:
* Selece any QSS.
* Execute the ipynb files in the order of: mutation_and_create -> execute_quantum_circuits -> collect_and_evaluation.
* To restrat the system, please move the folders which end with number to a new place.
* Running Tips: all the ipynb should keep the same root with generated folders.
* If need to execute Qiskit circuits on IBM quantum computer, an IBM ID is required. It can be applied from [IBM](https://quantum-computing.ibm.com/).

## Package version:
* Qiskit 0.21.0
* Cirq 0.15.0
* Pyqiuil 2.27.0 
* Forest-sdk-2.23.0(For Pyquil) can be downloaded from [Pyquil](https://downloads.rigetti.com/qcs-sdk/forest-sdk-2.23.0.msi).
    * QVM 1.7.1
    * Quilc 1.23.0


## Acknowledgement
* [QDiff](https://github.com/wjy99-c/QDiff)



