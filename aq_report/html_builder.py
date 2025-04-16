from aq_report.color_rules import get_color
from aq_report.reader import FIELDS

def create_html_table(results):
    html = """
    <html><body>
    <h2>Air Quality Report</h2>
    <table border="1" cellpadding="6" cellspacing="0">
        <tr style="background-color:#e0e0e0;">
            <th>Location</th>
            <th>Timestamp</th>
            <th>PM1.0 (µg/m³)</th>
            <th>PM2.5 (µg/m³)</th>
            <th>PM10 (µg/m³)</th>
            <th>VOC (ppb)</th>
            <th>CO₂ (ppm)</th>
            <th>Humidity (%)</th>
            <th>Temperature (°C)</th>
        </tr>
    """

    for location, values in results.items():
        html += f"<tr><td>{location}</td>"
        for i, val in enumerate(values):
            field = FIELDS[i]
            color = get_color(field, val) if i > 0 else "#FFFFFF"
            html += f'<td style="background-color:{color}; text-align:center;">{val}</td>'
        html += "</tr>"

    html += "</table></body></html>"
    return html
