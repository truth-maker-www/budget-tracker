import requests

# כתובת ה-API של מפתח התקציב - מחפש העברות תקציביות אחרונות
API_URL = "https://next.obudget.org/api/query?query=SELECT%20*%20FROM%20budget%20ORDER%20BY%20year%20DESC%20LIMIT%201"

def check_for_updates():
    print("מתחיל בדיקת נתונים ממפתח התקציב...")
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        if data and 'rows' in data and len(data['rows']) > 0:
            latest = data['rows'][0]
            # חילוץ נתונים לדוגמה
            title = latest.get('title', 'לא צוין שם')
            net_allocated = latest.get('net_allocated', 0)
            
            print(f"--- נמצא נתון חדש! ---")
            print(f"נושא: {title}")
            print(f"סכום: {net_allocated:,} ש''ח")
        else:
            print("לא נמצאו נתונים בשאילתה הנוכחית.")
            
    except Exception as e:
        print(f"שגיאה בתהליך: {e}")

if __name__ == "__main__":
    check_for_updates()
89
