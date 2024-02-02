import streamlit as st
from datetime import datetime
import pytz

# Define locations and their respective time zones
LOCATIONS = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Beijing": "Asia/Shanghai",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
}

# Streamlit app layout
st.title('World Clock')

# Dropdown for selecting locations
selected_locations = st.multiselect('Select up to 4 locations:', options=list(LOCATIONS.keys()), default=["New York"])

# Display time for selected locations
for location in selected_locations:
    timezone = pytz.timezone(LOCATIONS[location])
    time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    st.write(f"{location}: {time}")

# Bonus: UNIX Timestamp and Converter
if st.checkbox("Show UNIX Timestamp"):
    st.write(f"Current UNIX Timestamp: {datetime.now().timestamp()}")

if st.checkbox("Convert UNIX Timestamp to Human-Readable Time"):
    unix_timestamp = st.number_input("Enter UNIX Timestamp:", step=1.0, format="%f")
    if unix_timestamp:
        human_time = datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        st.write(f"Human-Readable Time: {human_time}")
