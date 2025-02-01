#!/bin/bash

while true; do
  # Get battery information using upower
  battery_info=$(upower -i $(upower -e | grep -E '^battery_' | 
head -n 1))

  # Extract status and percentage
  battery_status=$(echo "$battery_info" | grep -Eo 'state:\s+(.*)'
| awk '{print $2}')
  battery_percentage=$(echo "$battery_info" | grep -Eo 
'percentage:\s+(.*)' | awk '{print $2}' | sed 's/%//g')

  # Display status and percentage
  echo "Battery Status: $battery_status"
  echo "Battery Percentage: $battery_percentage%"

  # Check if battery is charging
  if [[ $battery_status == "Discharging" ]]; then
    echo "Battery is discharging."
  elif [[ $battery_status == "Charging" ]]; then
    echo "Battery is charging."
  elif [[ $battery_status == "Full" ]]; then
    echo "Battery is fully charged."
  else
    echo "Unknown battery status."
  fi

  # Sleep for 5 seconds
  sleep 5
done

