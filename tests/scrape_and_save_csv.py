import requests
import csv
import json
import requests

cookies = {
    'activemississauga_JSESSIONID': 'node01hou97lihch3f1vxx0rnb9ps8e14221092.node0',
    'activemississauga_FullPageView': 'true',
    'org': 'activemississauga',
    'TS0178a0b2': '01e462b1a27b8751958999e0bb2c4bc1e55ed0c5583cc23f759df556ba7219d08c726889c94728fcb0c53754df8c0c330ed4c522e78756c12226a8e91f34ed3fd012cb49af081862375857f2815a5708fb56100ba9534fdf62bc7e81f79c58f7e38503a077',
    'TS01b919ad': '01e462b1a2447171a5c426f00d97257d7eb23997a63cc23f759df556ba7219d08c726889c9e85c1ed28792796bb831fc8a82a8de4bb0a3dd6bc30e7d9f117d8601cb33add9',
    'JSESSIONID': 'node01xzssi43jeobc108lghojbsezg4543192.node0',
    'BIGipServer~activenet~anc_prodca_activemississauga': '!fT7RwqqtTax731zQxKw49ZK1Uq+JikY9FawuUvXnZDcY7UXU6eQTb96b3pbPxiDCzAlrZEPNC1ejLg==',
    'BIGipServer~activenet~activenet_cui_prod_ats': '!aQNmpoUJOmQxxYcEieGbaAu4betNFbFpvkeWPhZZYpE3GnfT7oxomA2buBprqEevpU8UC7EVqrLkAns=',
    'activemississauga_locale': 'en-US',
    's_fid': '72C0658EC944744C-130C8F1180496613',
    's_cc': 'true',
    's_vi': '[CS]v1|33C1E5C828AB7BCF-40001977602F09B4[CE]',
    '_ga': 'GA1.1.1350510308.1736690578',
    'TS012d8099': '01e462b1a2dd787f0d0a06710ba97607b6a1952a0a98fdd580f3cc70af183435d78fa7a35854fbc3e0310dfeab1dabe75fb8aee3336d6d24ed6d721d5cae7c2812a7c31099a47b5df682f4702c4de7bc7dc35c79f2',
    '_ga_9TVEC3MTMH': 'GS1.1.1736693918.2.1.1736694983.0.0.0',
    '_ga_GFNR8XEQ99': 'GS1.1.1736693918.2.1.1736694983.0.0.0',
    'utag_main': '_sn:3$_se:1%3Bexp-session$_ss:1%3Bexp-session$_st:1736698605109%3Bexp-session$ses_id:1736696805109%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:activecommunities.com',
    's_sq': '%5B%5BB%5D%5D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Cookie': 'activemississauga_JSESSIONID=node01hou97lihch3f1vxx0rnb9ps8e14221092.node0; activemississauga_FullPageView=true; org=activemississauga; TS0178a0b2=01e462b1a27b8751958999e0bb2c4bc1e55ed0c5583cc23f759df556ba7219d08c726889c94728fcb0c53754df8c0c330ed4c522e78756c12226a8e91f34ed3fd012cb49af081862375857f2815a5708fb56100ba9534fdf62bc7e81f79c58f7e38503a077; TS01b919ad=01e462b1a2447171a5c426f00d97257d7eb23997a63cc23f759df556ba7219d08c726889c9e85c1ed28792796bb831fc8a82a8de4bb0a3dd6bc30e7d9f117d8601cb33add9; JSESSIONID=node01xzssi43jeobc108lghojbsezg4543192.node0; BIGipServer~activenet~anc_prodca_activemississauga=!fT7RwqqtTax731zQxKw49ZK1Uq+JikY9FawuUvXnZDcY7UXU6eQTb96b3pbPxiDCzAlrZEPNC1ejLg==; BIGipServer~activenet~activenet_cui_prod_ats=!aQNmpoUJOmQxxYcEieGbaAu4betNFbFpvkeWPhZZYpE3GnfT7oxomA2buBprqEevpU8UC7EVqrLkAns=; activemississauga_locale=en-US; s_fid=72C0658EC944744C-130C8F1180496613; s_cc=true; s_vi=[CS]v1|33C1E5C828AB7BCF-40001977602F09B4[CE]; _ga=GA1.1.1350510308.1736690578; TS012d8099=01e462b1a2dd787f0d0a06710ba97607b6a1952a0a98fdd580f3cc70af183435d78fa7a35854fbc3e0310dfeab1dabe75fb8aee3336d6d24ed6d721d5cae7c2812a7c31099a47b5df682f4702c4de7bc7dc35c79f2; _ga_9TVEC3MTMH=GS1.1.1736693918.2.1.1736694983.0.0.0; _ga_GFNR8XEQ99=GS1.1.1736693918.2.1.1736694983.0.0.0; utag_main=_sn:3$_se:1%3Bexp-session$_ss:1%3Bexp-session$_st:1736698605109%3Bexp-session$ses_id:1736696805109%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:activecommunities.com; s_sq=%5B%5BB%5D%5D',
    'Origin': 'https://anc.ca.apm.activecommunities.com',
    'Referer': 'https://anc.ca.apm.activecommunities.com/activemississauga/calendars?onlineSiteId=0&no_scroll_top=true&defaultCalendarId=1&locationId=290%2C56%2C261%2C240%2C267%2C250%2C243%2C252%2C253%2C125%2C65%2C100%2C119%2C401%2C82%2C396%2C91%2C128%2C106%2C110%2C68&displayType=0&view=2',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'X-CSRF-Token': '61bf472c-610b-4ed7-bdb5-210becd8c897',
    'X-Requested-With': 'XMLHttpRequest',
    'page_info': '{"page_number":1,"total_records_per_page":20}',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'locale': 'en-US',
}

json_data = {
    'calendar_id': 1,
    'center_ids': [
        290,
        56,
        261,
        240,
        267,
        250,
        243,
        252,
        253,
        125,
        65,
        100,
        119,
        401,
        82,
        396,
        91,
        128,
        106,
        110,
        68,
    ],
    'display_all': 0,
    'search_start_time': '',
    'search_end_time': '',
    'facility_ids': [],
    'activity_category_ids': [],
    'activity_sub_category_ids': [],
    'activity_ids': [],
    'activity_min_age': None,
    'activity_max_age': None,
    'event_type_ids': [],
}



def fetch_calendar_data():
    """
    Posts to the Mississauga ActiveNet JSON endpoint, returning the parsed JSON (a Python dict).
    """
    response = requests.post(
        'https://anc.ca.apm.activecommunities.com/activemississauga/rest/onlinecalendar/multicenter/events',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()
    return response.json()

def parse_calendar_data(data):
    """
    data: dict with shape:
      {
        "headers": {...},
        "body": {
          "center_events": [
            {
              "center_id": 290,
              "center_name": "Burnhamthorpe Community Centre",
              "events": [
                {
                  "title": "Adult Leisure Swim",
                  "start_time": "2025-01-11 15:00:00",
                  "end_time": "2025-01-11 16:00:00",
                  "description": "...",
                  "facilities": [...],
                  ...
                },
                ...
              ]
            },
            ...
          ]
        }
      }

    Returns a list of dicts, each dict is one event with keys like title, start_time, etc.
    """
    events_list = []

    # 1) Grab the "center_events" array
    centers = data.get("body", {}).get("center_events", [])

    for center_info in centers:
        center_id = center_info.get("center_id")
        center_name = center_info.get("center_name", "Unknown Center")

        # 2) Loop over the "events" in this center
        for event in center_info.get("events", []):
            title = event.get("title", "")
            start_time = event.get("start_time", "")
            end_time = event.get("end_time", "")
            description = event.get("description", "")

            # If there's at least one facility
            facility_name = ""
            if event.get("facilities"):
                facility_name = event["facilities"][0].get("facility_name", "")

            # Build a flattened record
            record = {
                "center_id": center_id,
                "center_name": center_name,
                "title": title,
                "start_time": start_time,
                "end_time": end_time,
                "description": description,
                "facility_name": facility_name
            }
            events_list.append(record)

    return events_list

def save_events_to_csv(events, csv_file="events.csv"):
    """
    Writes the list of event dicts to a CSV file with columns:
      center_id, center_name, title, start_time, end_time, description, facility_name
    """
    if not events:
        print("No events to save.")
        return

    fieldnames = [
        "center_id",
        "center_name",
        "title",
        "start_time",
        "end_time",
        "description",
        "facility_name"
    ]

    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Saved {len(events)} events to {csv_file}!")

if __name__ == "__main__":
    # 1) Fetch JSON
    data = fetch_calendar_data()
    # 2) Parse
    events = parse_calendar_data(data)
    # 3) Save to CSV
    save_events_to_csv(events, "events.csv")

    # At this point, you have an events.csv file with all your scraped data.