import datetime
from auth_helper import get_service

def test_types():
    service = get_service('fitness', 'v1')
    now_dt = datetime.datetime.now()
    start_of_today = now_dt.replace(hour=0, minute=0, second=0, microsecond=0)
    
    types = [
        "com.google.step_count.delta",
        "com.google.calories.expended",
        "com.google.distance.delta",
        "com.google.heart_minutes",
        "com.google.active_minutes",
        "com.google.heart_rate.bpm",
        "com.google.weight",
        "com.google.height"
    ]
    
    for t in types:
        body = {
            "aggregateBy": [{"dataTypeName": t}],
            "bucketByTime": { "durationMillis": 86400000 },
            "startTimeMillis": int(start_of_today.timestamp() * 1000),
            "endTimeMillis": int(now_dt.timestamp() * 1000)
        }
        try:
            service.users().dataset().aggregate(userId="me", body=body).execute()
            print(f"✅ {t} is accessible")
        except Exception as e:
            print(f"❌ {t} failed: {e}")

if __name__ == "__main__":
    test_types()
