"""
src/scrape_calendar.py

Fetch JSON data from the Mississauga ActiveNet endpoint.
No BeautifulSoup required for this approach.
"""

import requests
from src.config import EVENTS_URL

def fetch_calendar_data(url=EVENTS_URL):
    """
    Fetches the JSON directly from the known events endpoint.
    Returns a Python dict (parsed from JSON).
    """
    headers = {
        "User-Agent": "Mozilla/5.0",  # Sometimes needed to avoid blocks
        # Add more headers/cookies if needed, exactly like your browser request
    }

    response = requests.get(url, headers=headers)
    
    # --- Debug prints to see what you're actually getting back ---
    print("Status code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("First 500 chars of text:\n", response.text[:500])
    # ------------------------------------------------------------

    response.raise_for_status()

    # If the response is valid JSON, this will succeed;
    # if it's actually HTML or an error message, it will raise JSONDecodeError
    return response.json()

def fetch_calendar_data():
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
        's_sq': 'anactivenet%3D%2526pid%253Danc.ca.apm.activecommunities.com%25252Factivemississauga%25252Fcalendars%2526pidt%253D1%2526oid%253Dfunctioncn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSPAN',
        'TS012d8099': '01e462b1a2dd787f0d0a06710ba97607b6a1952a0a98fdd580f3cc70af183435d78fa7a35854fbc3e0310dfeab1dabe75fb8aee3336d6d24ed6d721d5cae7c2812a7c31099a47b5df682f4702c4de7bc7dc35c79f2',
        '_ga_9TVEC3MTMH': 'GS1.1.1736693918.2.1.1736694981.0.0.0',
        '_ga_GFNR8XEQ99': 'GS1.1.1736693918.2.1.1736694981.0.0.0',
        'utag_main': '_sn:2$_se:5%3Bexp-session$_ss:0%3Bexp-session$_st:1736696783103%3Bexp-session$ses_id:1736693928402%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:activecommunities.com',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=utf-8',
        # 'Cookie': 'activemississauga_JSESSIONID=node01hou97lihch3f1vxx0rnb9ps8e14221092.node0; activemississauga_FullPageView=true; org=activemississauga; TS0178a0b2=01e462b1a27b8751958999e0bb2c4bc1e55ed0c5583cc23f759df556ba7219d08c726889c94728fcb0c53754df8c0c330ed4c522e78756c12226a8e91f34ed3fd012cb49af081862375857f2815a5708fb56100ba9534fdf62bc7e81f79c58f7e38503a077; TS01b919ad=01e462b1a2447171a5c426f00d97257d7eb23997a63cc23f759df556ba7219d08c726889c9e85c1ed28792796bb831fc8a82a8de4bb0a3dd6bc30e7d9f117d8601cb33add9; JSESSIONID=node01xzssi43jeobc108lghojbsezg4543192.node0; BIGipServer~activenet~anc_prodca_activemississauga=!fT7RwqqtTax731zQxKw49ZK1Uq+JikY9FawuUvXnZDcY7UXU6eQTb96b3pbPxiDCzAlrZEPNC1ejLg==; BIGipServer~activenet~activenet_cui_prod_ats=!aQNmpoUJOmQxxYcEieGbaAu4betNFbFpvkeWPhZZYpE3GnfT7oxomA2buBprqEevpU8UC7EVqrLkAns=; activemississauga_locale=en-US; s_fid=72C0658EC944744C-130C8F1180496613; s_cc=true; s_vi=[CS]v1|33C1E5C828AB7BCF-40001977602F09B4[CE]; _ga=GA1.1.1350510308.1736690578; s_sq=anactivenet%3D%2526pid%253Danc.ca.apm.activecommunities.com%25252Factivemississauga%25252Fcalendars%2526pidt%253D1%2526oid%253Dfunctioncn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSPAN; TS012d8099=01e462b1a2dd787f0d0a06710ba97607b6a1952a0a98fdd580f3cc70af183435d78fa7a35854fbc3e0310dfeab1dabe75fb8aee3336d6d24ed6d721d5cae7c2812a7c31099a47b5df682f4702c4de7bc7dc35c79f2; _ga_9TVEC3MTMH=GS1.1.1736693918.2.1.1736694981.0.0.0; _ga_GFNR8XEQ99=GS1.1.1736693918.2.1.1736694981.0.0.0; utag_main=_sn:2$_se:5%3Bexp-session$_ss:0%3Bexp-session$_st:1736696783103%3Bexp-session$ses_id:1736693928402%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:activecommunities.com',
        'Origin': 'https://anc.ca.apm.activecommunities.com',
        'Referer': 'https://anc.ca.apm.activecommunities.com/activemississauga/calendars?onlineSiteId=0&no_scroll_top=true&defaultCalendarId=1&locationId=290&displayType=0&view=2',
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

    response = requests.post(
        'https://anc.ca.apm.activecommunities.com/activemississauga/rest/onlinecalendar/multicenter/events',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()
    return response.json()
