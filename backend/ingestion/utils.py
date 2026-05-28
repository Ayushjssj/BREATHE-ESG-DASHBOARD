from datetime import datetime


def parse_date(value):
    value = str(value).strip()

    formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass

    raise ValueError(f"Invalid date format: {value}")


def normalize_unit(quantity, unit):
    unit = str(unit).lower().strip()
    quantity = float(quantity)

    if unit in ["l", "liter", "litre", "liters", "litres"]:
        return quantity, "litre"

    if unit in ["kl", "kiloliter", "kilolitre"]:
        return quantity * 1000, "litre"

    if unit in ["kwh"]:
        return quantity, "kWh"

    if unit in ["mwh"]:
        return quantity * 1000, "kWh"

    if unit in ["km", "kilometer", "kilometre"]:
        return quantity, "km"

    if unit in ["mile", "miles"]:
        return quantity * 1.60934, "km"

    if unit in ["night", "nights"]:
        return quantity, "night"

    return quantity, unit


def detect_suspicious(quantity, unit):
    quantity = float(quantity)

    if quantity <= 0:
        return "Quantity is zero or negative."

    if unit.lower() in ["kwh", "mwh"] and quantity > 1000000:
        return "Electricity usage is unusually high."

    if unit.lower() in ["l", "liter", "litre", "liters", "litres", "kl"] and quantity > 100000:
        return "Fuel quantity is unusually high."

    if unit.lower() in ["km", "mile", "miles"] and quantity > 20000:
        return "Travel distance is unusually high."

    return None