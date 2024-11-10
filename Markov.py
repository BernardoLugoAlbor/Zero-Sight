import pandas as pd
import numpy as np

# Leer DataFrame de ventas desde el archivo CSV
df_compras = pd.read_csv('datos.csv')

# Matriz de transición específica 10x10
transition_matrix = np.array([
    [0.0433668, 0.17057338, 0.01874732, 0.07245254, 0.05150475, 0.36838537,
     0.04001976, 0.01655979, 0.06061248, 0.1577778],
    [0.01497903, 0.02018832, 0.14024094, 0.03303987, 0.05276571, 0.48898913,
     0.05693067, 0.12639707, 0.06377337, 0.00269588],
    [0.0086045, 0.08975175, 0.15995447, 0.07187111, 0.11629609, 0.09777201,
     0.03553352, 0.28758747, 0.10908569, 0.0235434],
    [0.08017673, 0.16439886, 0.01750733, 0.11396609, 0.04980869, 0.03919612,
     0.04315719, 0.17754636, 0.03007668, 0.28416594],
    [0.10081405, 0.0802452, 0.03475821, 0.06556538, 0.09016294, 0.03475102,
     0.069806, 0.30538653, 0.17318369, 0.04532697],
    [0.17367426, 0.18593365, 0.16001254, 0.04329064, 0.06772013, 0.014372,
     0.11548546, 0.03924196, 0.11603566, 0.0842337],
    [0.09928767, 0.05447662, 0.03607935, 0.00738818, 0.10450756, 0.31341301,
     0.06999618, 0.01366023, 0.23815022, 0.06304098],
    [0.24033549, 0.20718738, 0.04705007, 0.0184255, 0.05778282, 0.04325449,
     0.0994252, 0.17500343, 0.00067125, 0.11086437],
    [0.17152305, 0.034871, 0.0731916, 0.08925588, 0.02104316, 0.22755627,
     0.03788549, 0.2238321, 0.01230541, 0.10853605],
    [0.25966157, 0.11179898, 0.00234142, 0.0383153, 0.00756219, 0.1088065,
     0.05260833, 0.34014742, 0.04326883, 0.03548946]
])

# Vector de estado inicial
initial_state = np.full(len(transition_matrix), 1/len(transition_matrix))

# Función para seleccionar el siguiente estado estocásticamente
def stochastic_transition(current_probabilities):
    return np.random.choice(range(len(current_probabilities)), p=current_probabilities)

# Inicializar el estado inicial y simular una secuencia de estados
state_index = np.random.choice(range(len(initial_state)), p=initial_state)
print("Initial state:", state_index)

n_steps = 12
total = 0

# Simulación de la cadena de Markov y lectura del DataFrame
for step in range(1, n_steps + 1):
    # Actualizar el vector de probabilidad actual usando la matriz de transición
    current_probabilities = transition_matrix[state_index]
    # Elegir el siguiente estado de manera estocástica
    state_index = stochastic_transition(current_probabilities)
    print(f"Step {step}: Current state -> {state_index}")
    
    # Acceder al valor de ventas correspondiente
    valor_venta = df_compras.iloc[state_index, (step - 1) % 30]
    total += valor_venta

print('Total:', total)

# Simulación de la cadena de Markov y lectura del DataFrame
for step in range(1, n_steps + 1):
    # Actualizar el vector de probabilidad actual usando la matriz de transición
    current_probabilities = transition_matrix[state_index]
    # Elegir el siguiente estado de manera estocástica
    state_index = stochastic_transition(current_probabilities)
    print(f"Step {step}: Current state -> {state_index}")
    
    # Fondo de ahorro en base a sobrantes
    if state_index == 0:
        total = total + 0.5*70
    elif state_index == 1:
        total = total + 1*70
    elif state_index == 2:
        total = total + 1.5*70
    elif state_index == 3:
        total = total + 2*70
    elif state_index == 4:
        total = total + 2.5*70
    elif state_index == 5:
        total = total + 3*70
    elif state_index == 6:
        total = total + 3.5*70
    elif state_index == 7:
        total = total + 4*70
    elif state_index == 8:
        total = total + 4.5*70
    elif state_index == 9:
        total = total + 5*70
print('Total:', total)
