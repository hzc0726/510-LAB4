import streamlit as st
import pytz
import datetime
import time

st.title('World Clock')

# Time zones list
time_zones = list(pytz.all_timezones)

# Multi-select dropdown for time zone selection
selected_zones = st.multiselect("Select Time Zones", time_zones, default=["UTC"])

# Function to show time
def show_time():
    while True:
        # Clear old time values
        with st.empty():
            # Display current time for selected zones
            for tz in selected_zones:
                now = datetime.datetime.now(pytz.timezone(tz))
                st.write(f"Time in {tz}: {now.strftime('%Y-%m-%d %H:%M:%S')}")

            # Sleep for 1 second before updating time
            time.sleep(1)

# Call the function to display time
show_time()
