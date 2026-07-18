# Appliance list corresponding to bits 0 through 7
DEVICES = ["Porch Light", "Living Room Light", "Garage Door", "Smart TV", 
           "Refrigerator", "Air Conditioner", "Water Heater", "Security System"]

def check_switches(reg):
    """Prints the status of each bit/appliance."""
    print(f"\nRegister: 0b{reg:08b} (Decimal: {reg})")
    for i, name in enumerate(DEVICES):
        status = "ON 🟢" if (reg & (1 << i)) else "OFF 🔴"
        print(f"Bit {i} | {name:<20}: {status}")

# 1. Initialize register to 0 (all OFF)
reg = 0b00000000

# 2. Turn ON Porch (Bit 0) and Living Room (Bit 1) using OR (|)
reg |= (1 << 0) | (1 << 1)

# 3. Turn ON Air Conditioner (Bit 5) using OR (|)
reg |= (1 << 5)
check_switches(reg)

# 4. Toggle Living Room Light (Bit 1) OFF using XOR (^)
print("\n[Action] Toggling Living Room Light...")
reg ^= (1 << 1)

# 5. Force Air Conditioner (Bit 5) OFF using AND NOT (& ~)
print("[Action] Forcing Air Conditioner OFF...")
reg &= ~(1 << 5)
check_switches(reg)
