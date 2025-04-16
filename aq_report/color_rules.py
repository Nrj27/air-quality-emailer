def get_color(field, value):
    try:
        val = float(value)
    except:
        return "#CCCCCC"  # gray for missing or invalid

    if field in ["pm01_ugm3", "pm25_ugm3"]:
        if val <= 12: return "#90EE90"
        elif val <= 35: return "#FFD700"
        else: return "#FF6347"

    elif field == "pm10_ugm3":
        if val <= 50: return "#90EE90"
        elif val <= 150: return "#FFD700"
        else: return "#FF6347"

    elif field == "voc_ppb":
        if val <= 220: return "#90EE90"
        elif val <= 660: return "#FFD700"
        else: return "#FF6347"

    elif field == "co2_ppm":
        if val <= 800: return "#90EE90"
        elif val <= 1200: return "#FFD700"
        else: return "#FF6347"

    elif field == "humidity_RH":
        if 30 <= val <= 60: return "#90EE90"
        elif 20 <= val < 30 or 61 <= val <= 70: return "#FFD700"
        else: return "#FF6347"

    elif field == "temperature_C":
        if 18 <= val <= 25: return "#90EE90"
        elif 10 <= val < 18 or 26 <= val <= 30: return "#FFD700"
        else: return "#FF6347"

    return "#CCCCCC"
