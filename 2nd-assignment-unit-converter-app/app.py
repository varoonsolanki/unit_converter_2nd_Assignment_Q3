import math
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")

# Custom CSS for better UI
st.markdown("""
<style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSelectbox div {
        font-size: 16px;
    }
    .stNumberInput input {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("📏 Unit Converter")
st.write("""
Welcome to the **Unit Converter App**! Convert between different units of length, weight, and temperature easily.
""")

# Main Conversion Logic
def length_converter(value, from_unit, to_unit):
    # Length conversion logic
    conversions = {
        "Meter": {"Kilometer": value / 1000, "Centimeter": value * 100},
        "Kilometer": {"Meter": value * 1000, "Centimeter": value * 100000},
        "Centimeter": {"Meter": value / 100, "Kilometer": value / 100000}
    }
    return conversions[from_unit][to_unit]

def weight_converter(value, from_unit, to_unit):
    # Weight conversion logic
    conversions = {
        "Kilogram": {"Gram": value * 1000, "Pound": value * 2.20462},
        "Gram": {"Kilogram": value / 1000, "Pound": value * 0.00220462},
        "Pound": {"Kilogram": value / 2.20462, "Gram": value * 453.592}
    }
    return conversions[from_unit][to_unit]

def temperature_converter(value, from_unit, to_unit):
    # Temperature conversion logic
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def volume_converter(value, from_unit, to_unit):
    # Volume conversion factors relative to Liter
    conversion_factors = {
        "Liter": 1,
        "Milliliter": 1e3,
        "Cubic Meter": 1e-3,
        "Cubic Centimeter": 1,  # 1 cm³ = 1 mL
        "Cubic Inch": 61.0237,
        "Cubic Foot": 0.0353147,
        "Gallon (US)": 0.264172
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid volume unit '{from_unit}' or '{to_unit}'"

    # Convert to Liters first, then to target unit
    value_in_liters = value / conversion_factors[from_unit]
    converted_value = value_in_liters * conversion_factors[to_unit]

    return converted_value

def speed_converter(value, from_unit, to_unit):
    # Speed conversion factors relative to Meters per Second
    conversion_factors = {
        "Meters per Second (m/s)": 1,
        "Kilometers per Hour (km/h)": 3.6,
        "Miles per Hour (mph)": 2.237,
        "Feet per Second (ft/s)": 3.281,
        "Knots": 1.944
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid speed unit '{from_unit}' or '{to_unit}'"

    # Convert to Meters per Second first, then to target unit
    value_in_mps = value / conversion_factors[from_unit]
    converted_value = value_in_mps * conversion_factors[to_unit]

    return converted_value

def time_converter(value, from_unit, to_unit):
    # Time conversion factors relative to Seconds
    conversion_factors = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid time unit '{from_unit}' or '{to_unit}'"

    # Convert to Seconds first, then to target unit
    value_in_seconds = value * conversion_factors[from_unit]
    converted_value = value_in_seconds / conversion_factors[to_unit]

    return converted_value
 
def area_converter(value, from_unit, to_unit):
    # Area conversion factors (relative to Square Meter)
    conversion_factors = {
        "Square Meter": 1,
        "Square Kilometer": 1e6,
        "Square Centimeter": 1e-4,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
        "Acre": 4046.86,
        "Hectare": 10000
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors:
        return f"Error: '{from_unit}' is not a valid unit."
    if to_unit not in conversion_factors:
        return f"Error: '{to_unit}' is not a valid unit."

    # Convert to Square Meter first, then to the target unit
    value_in_square_meters = value * conversion_factors[from_unit]
    converted_value = value_in_square_meters / conversion_factors[to_unit]

    return converted_value

def pressure_converter(value, from_unit, to_unit):
    # Pressure conversion factors (relative to Pascal)
    conversion_factors = {
        "Pascal": 1,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325,
        "Torr": 133.322
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors:
        return f"Error: '{from_unit}' is not a valid unit."
    if to_unit not in conversion_factors:
        return f"Error: '{to_unit}' is not a valid unit."

    # Convert to Pascal first, then to the target unit
    value_in_pascals = value * conversion_factors[from_unit]
    converted_value = value_in_pascals / conversion_factors[to_unit]

    return converted_value

def energy_converter(value, from_unit, to_unit):
    # Energy conversion factors (relative to Joule)
    conversion_factors = {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,
        "Kilocalorie": 4184,
        "Watt-hour": 3600,
        "Kilowatt-hour": 3.6e6,
        "Electronvolt": 1.60218e-19
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors:
        return f"Error: '{from_unit}' is not a valid unit."
    if to_unit not in conversion_factors:
        return f"Error: '{to_unit}' is not a valid unit."

    # Convert to Joule first, then to the target unit
    value_in_joules = value * conversion_factors[from_unit]
    converted_value = value_in_joules / conversion_factors[to_unit]

    return converted_value

def power_converter(value, from_unit, to_unit):
    # Power conversion factors (relative to Watt)
    conversion_factors = {
        "Watt": 1,
        "Kilowatt": 1000,
        "Horsepower": 745.7,
        "Megawatt": 1e6,
        "Gigawatt": 1e9,
        "BTU/hour": 0.293071,
        "Foot-pound/minute": 0.022597
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors:
        return f"Error: '{from_unit}' is not a valid unit."
    if to_unit not in conversion_factors:
        return f"Error: '{to_unit}' is not a valid unit."

    # Convert to Watt first, then to the target unit
    value_in_watts = value * conversion_factors[from_unit]
    converted_value = value_in_watts / conversion_factors[to_unit]

    return converted_value

 
def storage_converter(value, from_unit, to_unit):
    # Storage conversion factors (relative to Bytes)
    conversion_factors = {
        "Byte": 1,
        "Kilobyte": 1024,
        "Megabyte": 1024**2,
        "Gigabyte": 1024**3,
        "Terabyte": 1024**4,
        "Petabyte": 1024**5
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid storage unit '{from_unit}' or '{to_unit}'"

    # Convert to Bytes first, then to target unit
    value_in_bytes = value * conversion_factors[from_unit]
    converted_value = value_in_bytes / conversion_factors[to_unit]

    return converted_value

def frequency_converter(value, from_unit, to_unit):
    # Frequency conversion factors (relative to Hertz)
    conversion_factors = {
        "Hertz": 1,
        "Kilohertz": 1e3,
        "Megahertz": 1e6,
        "Gigahertz": 1e9
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid frequency unit '{from_unit}' or '{to_unit}'"

    # Convert to Hertz first, then to target unit
    value_in_hertz = value * conversion_factors[from_unit]
    converted_value = value_in_hertz / conversion_factors[to_unit]

    return converted_value

def angle_converter(value, from_unit, to_unit):
    # Angle conversion logic
    conversion_factors = {
        "Degree": 1,
        "Radian": 57.2958,  # 1 radian ≈ 57.2958 degrees
        "Gradian": 0.9       # 1 gradian = 0.9 degrees
    }

    # Error handling for invalid inputs
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return f"Error: Invalid angle unit '{from_unit}' or '{to_unit}'"

    # Convert to Degrees first, then to target unit
    value_in_degrees = value * conversion_factors[from_unit]
    converted_value = value_in_degrees / conversion_factors[to_unit]

    return round(converted_value, 2)  # Ensuring float output

# Main App
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Volume", "Speed", "Time", "Area", "Pressure", "Energy", "Power",   "Frequency", "Angle"])

if unit_type == "Length":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Meter", "Kilometer", "Centimeter"])
    with col2:
        to_unit = st.selectbox("To", ["Meter", "Kilometer", "Centimeter"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Meter" and to_unit == "Kilometer":
            st.write(f"{value} m × (1 / 1000) = {result:.2f} km")
        elif from_unit == "Kilometer" and to_unit == "Meter":
            st.write(f"{value} km × 1000 = {result:.2f} m")
        elif from_unit == "Meter" and to_unit == "Centimeter":
            st.write(f"{value} m × 100 = {result:.2f} cm")
        elif from_unit == "Centimeter" and to_unit == "Meter":
            st.write(f"{value} cm × (1 / 100) = {result:.2f} m")

elif unit_type == "Weight":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Pound"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Pound"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Kilogram" and to_unit == "Gram":
            st.write(f"{value} kg × 1000 = {result:.2f} g")
        elif from_unit == "Gram" and to_unit == "Kilogram":
            st.write(f"{value} g × (1 / 1000) = {result:.2f} kg")
        elif from_unit == "Kilogram" and to_unit == "Pound":
            st.write(f"{value} kg × 2.20462 = {result:.2f} lb")
        elif from_unit == "Pound" and to_unit == "Kilogram":
            st.write(f"{value} lb × (1 / 2.20462) = {result:.2f} kg")

elif unit_type == "Temperature":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            st.write(f"({value} °C × 9/5) + 32 = {result:.2f} °F")
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            st.write(f"({value} °F - 32) × 5/9 = {result:.2f} °C")
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            st.write(f"{value} °C + 273.15 = {result:.2f} K")
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            st.write(f"{value} K - 273.15 = {result:.2f} °C")
            
elif unit_type == "Volume":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Liter", "Milliliter", "Cubic Meter"])
    with col2:
        to_unit = st.selectbox("To", ["Liter", "Milliliter", "Cubic Meter"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = volume_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Liter" and to_unit == "Milliliter":
            st.write(f"{value} L × 1000 = {result:.2f} mL")
        elif from_unit == "Milliliter" and to_unit == "Liter":
            st.write(f"{value} mL × (1 / 1000) = {result:.2f} L")
        elif from_unit == "Liter" and to_unit == "Cubic Meter":
            st.write(f"{value} L × (1 / 1000) = {result:.2f} m³")
        elif from_unit == "Cubic Meter" and to_unit == "Liter":
            st.write(f"{value} m³ × 1000 = {result:.2f} L")

elif unit_type == "Speed":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Meters per Second (m/s)", "Kilometers per Hour (km/h)", "Miles per Hour (mph)"])
    with col2:
        to_unit = st.selectbox("To", ["Meters per Second (m/s)", "Kilometers per Hour (km/h)", "Miles per Hour (mph)"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = speed_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Meters per Second (m/s)" and to_unit == "Kilometers per Hour (km/h)":
            st.write(f"{value} m/s × 3.6 = {result:.2f} km/h")
        elif from_unit == "Kilometers per Hour (km/h)" and to_unit == "Meters per Second (m/s)":
            st.write(f"{value} km/h × (1 / 3.6) = {result:.2f} m/s")
        elif from_unit == "Meters per Second (m/s)" and to_unit == "Miles per Hour (mph)":
            st.write(f"{value} m/s × 2.23694 = {result:.2f} mph")
        elif from_unit == "Miles per Hour (mph)" and to_unit == "Meters per Second (m/s)":
            st.write(f"{value} mph × (1 / 2.23694) = {result:.2f} m/s")

elif unit_type == "Time":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Second", "Minute", "Hour"])
    with col2:
        to_unit = st.selectbox("To", ["Second", "Minute", "Hour"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = time_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Second" and to_unit == "Minute":
            st.write(f"{value} s × (1 / 60) = {result:.2f} min")
        elif from_unit == "Minute" and to_unit == "Second":
            st.write(f"{value} min × 60 = {result:.2f} s")
        elif from_unit == "Second" and to_unit == "Hour":
            st.write(f"{value} s × (1 / 3600) = {result:.2f} h")
        elif from_unit == "Hour" and to_unit == "Second":
            st.write(f"{value} h × 3600 = {result:.2f} s")

elif unit_type == "Area":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Square Meter", "Square Kilometer", "Square Foot"])
    with col2:
        to_unit = st.selectbox("To", ["Square Meter", "Square Kilometer", "Square Foot"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = area_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Square Meter" and to_unit == "Square Kilometer":
            st.write(f"{value} m² × (1 / 1,000,000) = {result:.2f} km²")
        elif from_unit == "Square Kilometer" and to_unit == "Square Meter":
            st.write(f"{value} km² × 1,000,000 = {result:.2f} m²")
        elif from_unit == "Square Meter" and to_unit == "Square Foot":
            st.write(f"{value} m² × 10.7639 = {result:.2f} ft²")
        elif from_unit == "Square Foot" and to_unit == "Square Meter":
            st.write(f"{value} ft² × (1 / 10.7639) = {result:.2f} m²")

elif unit_type == "Pressure":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Pascal", "Bar", "PSI"])
    with col2:
        to_unit = st.selectbox("To", ["Pascal", "Bar", "PSI"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = pressure_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Pascal" and to_unit == "Bar":
            st.write(f"{value} Pa × (1 / 100,000) = {result:.2f} bar")
        elif from_unit == "Bar" and to_unit == "Pascal":
            st.write(f"{value} bar × 100,000 = {result:.2f} Pa")
        elif from_unit == "Pascal" and to_unit == "PSI":
            st.write(f"{value} Pa × (1 / 6894.76) = {result:.2f} psi")
        elif from_unit == "PSI" and to_unit == "Pascal":
            st.write(f"{value} psi × 6894.76 = {result:.2f} Pa")

elif unit_type == "Energy":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Joule", "Kilojoule", "Calorie"])
    with col2:
        to_unit = st.selectbox("To", ["Joule", "Kilojoule", "Calorie"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = energy_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Joule" and to_unit == "Kilojoule":
            st.write(f"{value} J × (1 / 1000) = {result:.2f} kJ")
        elif from_unit == "Kilojoule" and to_unit == "Joule":
            st.write(f"{value} kJ × 1000 = {result:.2f} J")
        elif from_unit == "Joule" and to_unit == "Calorie":
            st.write(f"{value} J × (1 / 4.184) = {result:.2f} cal")
        elif from_unit == "Calorie" and to_unit == "Joule":
            st.write(f"{value} cal × 4.184 = {result:.2f} J")

elif unit_type == "Power":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Watt", "Kilowatt", "Horsepower"])
    with col2:
        to_unit = st.selectbox("To", ["Watt", "Kilowatt", "Horsepower"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = power_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Watt" and to_unit == "Kilowatt":
            st.write(f"{value} W × (1 / 1000) = {result:.2f} kW")
        elif from_unit == "Kilowatt" and to_unit == "Watt":
            st.write(f"{value} kW × 1000 = {result:.2f} W")
        elif from_unit == "Watt" and to_unit == "Horsepower":
            st.write(f"{value} W × (1 / 745.7) = {result:.2f} hp")
        elif from_unit == "Horsepower" and to_unit == "Watt":
            st.write(f"{value} hp × 745.7 = {result:.2f} W")


elif unit_type == "Frequency":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Hertz", "Kilohertz", "Megahertz"])
    with col2:
        to_unit = st.selectbox("To", ["Hertz", "Kilohertz", "Megahertz"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = frequency_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Hertz" and to_unit == "Kilohertz":
            st.write(f"{value} Hz × (1 / 1000) = {result:.2f} kHz")
        elif from_unit == "Kilohertz" and to_unit == "Hertz":
            st.write(f"{value} kHz × 1000 = {result:.2f} Hz")
        elif from_unit == "Hertz" and to_unit == "Megahertz":
            st.write(f"{value} Hz × (1 / 1,000,000) = {result:.2f} MHz")
        elif from_unit == "Megahertz" and to_unit == "Hertz":
            st.write(f"{value} MHz × 1,000,000 = {result:.2f} Hz")

elif unit_type == "Angle":
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Degree", "Radian", "Gradian"])
    with col2:
        to_unit = st.selectbox("To", ["Degree", "Radian", "Gradian"])
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = angle_converter(value, from_unit, to_unit)
        st.success(f"**Converted Value:** {result:.2f} {to_unit}")
        st.write(f"**Formula Used:**")
        if from_unit == "Degree" and to_unit == "Radian":
            st.write(f"{value}° × (π / 180) = {result:.2f} rad")
        elif from_unit == "Radian" and to_unit == "Degree":
            st.write(f"{value} rad × (180 / π) = {result:.2f}°")
        elif from_unit == "Degree" and to_unit == "Gradian":
            st.write(f"{value}° × (200 / 180) = {result:.2f} gon")
        elif from_unit == "Gradian" and to_unit == "Degree":
            st.write(f"{value} gon × (180 / 200) = {result:.2f}°")
            