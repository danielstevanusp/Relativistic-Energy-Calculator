def calculate_energy(mass, speed_of_light):
    energy = mass * (speed_of_light ** 2)
    return energy

# Input values for mass (kg) and the speed of light (m/s)
mass = float(input("Enter mass (kg): "))
speed_of_light = 3.0 * 10**8  # Speed of light in m/s

# Calculate energy using the formula E=mc^2
energy = calculate_energy(mass, speed_of_light)

# Display the result
print(f"The energy produced is {energy:.2e} joules.")
