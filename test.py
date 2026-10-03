import time
import random

print("--- Starting Real-Time Data Simulation ---")

for i in range(1, 6):
    simulated_temp = round(random.uniform(20.0, 40.0), 2)
    print(f"Time Step {i}: Received live sensor temperature -> {simulated_temp}°C")
    time.sleep(1)

print("--- Simulation Complete! ---")