import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parameters ---
# Growth Rates (Cheaters grow faster)
mu_good = 0.5  
mu_cheat = 0.5

# Logic Parameters
kill_efficiency = 2.0  # How fast the latch kills (Vmax)
antidote_strength = 100.0 # How well the antidote protects
false_positive_rate = 0.001 # Risk 

# Time
T = np.linspace(0, 20, 200)

def simulate_bioreactor(system_active=False):
    N_good = [100] # Start with mostly good cells
    N_cheat = [1]  # Start with 1 mutant
    
    dt = T[1] - T[0]
    
    for i in range(1, len(T)):
        # Determine Kill Rates
        if system_active:
            # Cheaters: High Stress, No Antidote -> HIGH KILL
            k_c = kill_efficiency 
            # Good: Low Stress, High Antidote -> LOW KILL
            k_g = false_positive_rate 
        else:
            k_c = 0
            k_g = 0
            
        # Update Populations (Euler method)
        # Good cells grow, minus accidents
        change_good = (mu_good * N_good[-1] - k_g * N_good[-1]) * dt
        
        # Cheaters grow fast, minus SYSTEM KILL
        change_cheat = (mu_cheat * N_cheat[-1] - k_c * N_cheat[-1]) * dt
        
        N_good.append(N_good[-1] + change_good)
        N_cheat.append(N_cheat[-1] + change_cheat)
        
    return N_good, N_cheat

# --- 2. Run Simulation ---
g_no_sys, c_no_sys = simulate_bioreactor(system_active=False)
g_sys, c_sys = simulate_bioreactor(system_active=True)

# --- 3. Plotting ---
plt.figure(figsize=(10, 6))

# Without System
plt.plot(T, g_no_sys, 'b--', alpha=0.5, label='Good Cells (No System)')
plt.plot(T, c_no_sys, 'r--', alpha=0.5, label='Cheaters (No System)')

# With Catcheater
plt.plot(T, g_sys, 'b-', linewidth=3, label='Good Cells (With Catcheater)')
plt.plot(T, c_sys, 'r-', linewidth=3, label='Cheaters (With Catcheater)')

plt.title("Yield Prediction: Prevention of Population Drift")
plt.xlabel("Fermentation Time")
plt.ylabel("Cell Population")
plt.legend()
plt.grid(True)
plt.show()