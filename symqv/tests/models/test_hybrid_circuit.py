import numpy as np

from symqv.lib.constants import zero
from symqv.lib.operations.state_decomposition import from_angles
from symqv.lib.parsing.open_qasm import read_from_qasm
from symqv.lib.utils.arithmetic import kron


def test___get_final_states():
    qc_path = '../../../benchmarks/symqv/teleportv3.qasm'
    qc = read_from_qasm(qc_path)

    psi = from_angles(0.3, 0.4)
    print(psi)

    final_state = qc._get_final_states(kron([psi, zero, zero]))
    print(final_state)

    psi = from_angles(3.67837934, 3.14159265)
    print(psi)

    final_state = qc._get_final_states(kron([psi, zero, zero]))
    print(final_state)

    psi = from_angles(0, np.pi)
    print(psi)

    final_state = qc._get_final_states(kron([psi, zero, zero]))
    print(final_state)

    psi = from_angles(2 * np.pi, np.pi)
    print(psi)

    final_state = qc._get_final_states(kron([psi, zero, zero]))
    print(final_state)


if __name__ == '__main__':
    test___get_final_states()