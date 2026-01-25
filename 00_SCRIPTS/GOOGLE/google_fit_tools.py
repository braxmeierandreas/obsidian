import datetime
import time
from auth_helper import get_service

def get_fit_data():
    try:
        service = get_service('fitness', 'v1')
    except Exception as e:
        print(f"Error authenticating: {e}")
        print("Please run 'python login_fix.py' to update your permissions.")
        return

    # Time range: Start of the current month until now
    now_dt = datetime.datetime.now()
    start_of_month = now_dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    start_time_ms = int(start_of_month.timestamp() * 1000)
    end_time_ms = int(now_dt.timestamp() * 1000)
    
    # Aggregate request body
    body = {
        "aggregateBy": [{
            "dataTypeName": "com.google.step_count.delta",
            "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
        }],
        "bucketByTime": { "durationMillis": 86400000 }, # 1 day in ms
        "startTimeMillis": start_time_ms,
        "endTimeMillis": end_time_ms
    }

    try:
        response = service.users().dataset().aggregate(userId="me", body=body).execute()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    month_name = now_dt.strftime('%B %Y')
    print(f"Google Fit Data (Schritte im {month_name}):")
    total_steps = 0
    days_count = 0
    
    for bucket in response.get('bucket', []):
        start_ts = int(bucket['startTimeMillis']) / 1000
        date_str = datetime.datetime.fromtimestamp(start_ts).strftime('%Y-%m-%d')
        
        steps = 0
        for dataset in bucket.get('dataset', []):
            for point in dataset.get('point', []):
                for value in point.get('value', []):
                    steps += value.get('intVal', 0)
        
        print(f"{date_str}: {steps:>6} Schritte")
        total_steps += steps
        if steps > 0: days_count += 1
    
    if days_count > 0:
        avg = total_steps / days_count
        print("-" * 30)
        print(f"Gesamt: {total_steps} Schritte")
        print(f"Schnitt: {int(avg)} Schritte/Tag (an Tagen mit Aktivität)")

if __name__ == '__main__':
    get_fit_data()
