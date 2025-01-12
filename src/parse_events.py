"""
src/parse_events.py

Parses the JSON structure returned by fetch_calendar_data
into a flat list of events with consistent keys.
"""

def parse_calendar_data(data):
    """
    data: dict with structure like:
      {
        "headers": {...},
        "body": {
          "center_events": [
            {
              "center_id": 290,
              "center_name": "...",
              "events": [
                {
                  "title": "Adult Leisure Swim",
                  "start_time": "2025-01-11 15:00:00",
                  "end_time": "2025-01-11 16:00:00",
                  "description": "...",
                  "facilities": [ { "facility_name": "..."} ],
                  ...
                },
                ...
              ]
            },
            ...
          ]
        }
      }

    Returns: list of dicts, each representing a single event.
    """
    events_list = []

    # Step 1: Grab the list of center_events
    centers = data.get("body", {}).get("center_events", [])

    for center_info in centers:
        center_id = center_info.get("center_id")
        center_name = center_info.get("center_name", "Unknown")

        # Step 2: Each center has an array of "events"
        for event in center_info.get("events", []):
            title = event.get("title", "")
            start_time = event.get("start_time", "")
            end_time = event.get("end_time", "")
            description = event.get("description", "")

            # If there's at least one facility, let's get the first name
            facilities = event.get("facilities", [])
            facility_name = ""
            if facilities:
                facility_name = facilities[0].get("facility_name", "")

            # Build a flat event record
            events_list.append({
                "center_id": center_id,
                "center_name": center_name,
                "title": title,
                "start_time": start_time,
                "end_time": end_time,
                "description": description,
                "facility_name": facility_name
            })

    return events_list
