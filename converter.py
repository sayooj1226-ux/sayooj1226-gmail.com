# converter.py - Extended conversion logic

def convert_length(value, from_unit, to_unit):
    to_meter = {
        "km": 1000, "m": 1, "cm": 0.01,
        "mm": 0.001, "mile": 1609.34,
        "inch": 0.0254, "foot": 0.3048,
        "yard": 0.9144, "nautical mile": 1852
    }
    return (value * to_meter[from_unit]) / to_meter[to_unit]


def convert_weight(value, from_unit, to_unit):
    to_kg = {
        "kg": 1, "g": 0.001, "mg": 0.000001,
        "lb": 0.453592, "oz": 0.0283495,
        "ton": 1000, "carat": 0.0002,
        "stone": 6.35029
    }
    return (value * to_kg[from_unit]) / to_kg[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C" and to_unit == "F": return (value * 9/5) + 32
    if from_unit == "F" and to_unit == "C": return (value - 32) * 5/9
    if from_unit == "C" and to_unit == "K": return value + 273.15
    if from_unit == "K" and to_unit == "C": return value - 273.15
    if from_unit == "F" and to_unit == "K": return (value - 32) * 5/9 + 273.15
    if from_unit == "K" and to_unit == "F": return (value - 273.15) * 9/5 + 32


def convert_speed(value, from_unit, to_unit):
    to_mps = {
        "m/s": 1, "km/h": 0.277778,
        "mph": 0.44704, "knot": 0.514444,
        "ft/s": 0.3048
    }
    return (value * to_mps[from_unit]) / to_mps[to_unit]


def convert_area(value, from_unit, to_unit):
    to_sqm = {
        "m²": 1, "km²": 1e6, "cm²": 0.0001,
        "mm²": 1e-6, "acre": 4046.86,
        "hectare": 10000, "ft²": 0.092903,
        "inch²": 0.00064516
    }
    return (value * to_sqm[from_unit]) / to_sqm[to_unit]


def convert_volume(value, from_unit, to_unit):
    to_liter = {
        "liter": 1, "ml": 0.001,
        "gallon": 3.78541, "cup": 0.236588,
        "pint": 0.473176, "quart": 0.946353,
        "fl oz": 0.0295735, "m³": 1000,
        "cm³": 0.001
    }
    return (value * to_liter[from_unit]) / to_liter[to_unit]


def convert_data(value, from_unit, to_unit):
    to_bit = {
        "bit": 1, "byte": 8,
        "KB": 8192, "MB": 8388608,
        "GB": 8589934592, "TB": 8796093022208
    }
    return (value * to_bit[from_unit]) / to_bit[to_unit]


def convert_time(value, from_unit, to_unit):
    to_sec = {
        "second": 1, "minute": 60,
        "hour": 3600, "day": 86400,
        "week": 604800, "month": 2628000,
        "year": 31536000
    }
    return (value * to_sec[from_unit]) / to_sec[to_unit]