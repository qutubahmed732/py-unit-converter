import sys

def convert_length(value, from_unit, to_unit):
    
    conversions = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "ft": 0.3048,
        "in": 0.0254
    }
    if from_unit not in conversions or to_unit not in conversions:
        return None
    meters = value * conversions[from_unit]
    return meters / conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    
    conversions = {
        "g": 1.0,
        "kg": 1000.0,
        "mg": 0.001,
        "lb": 453.592,
        "oz": 28.3495
    }
    if from_unit not in conversions or to_unit not in conversions:
        return None
    grams = value * conversions[from_unit]
    return grams / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == to_unit:
        return value
        
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5/9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        return None
        
    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9/5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        return None

def main():
    print("=" * 45)
    print("           CLI UNIT CONVERTER           ")
    print("=" * 45)
    print("1. Length (m, km, cm, mm, mi, ft, in)")
    print("2. Weight (g, kg, mg, lb, oz)")
    print("3. Temperature (c, f, k)")
    
    choice = input("\nSelect category (1-3): ").strip()
    
    if choice == "1":
        cat = "Length"
        valid_units = ["m", "km", "cm", "mm", "mi", "ft", "in"]
    elif choice == "2":
        cat = "Weight"
        valid_units = ["g", "kg", "mg", "lb", "oz"]
    elif choice == "3":
        cat = "Temperature"
        valid_units = ["c", "f", "k"]
    else:
        print("Error: Invalid category selection.")
        return

    print(f"\nAvailable units for {cat}: {', '.join(valid_units)}")
    
    try:
        value = float(input("Enter value to convert: "))
        from_unit = input("Enter source unit: ").strip().lower()
        to_unit = input("Enter target unit: ").strip().lower()
    except ValueError:
        print("Error: Please enter a valid numeric value.")
        return

    if cat == "Length":
        res = convert_length(value, from_unit, to_unit)
    elif cat == "Weight":
        res = convert_weight(value, from_unit, to_unit)
    elif cat == "Temperature":
        res = convert_temperature(value, from_unit, to_unit)

    if res is None:
        print("Error: Invalid unit(s) provided.")
    else:
        print(f"\nResult: {value} {from_unit} = {res:.4f} {to_unit}")

if __name__ == "__main__":
    main()