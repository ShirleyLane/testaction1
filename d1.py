import requests
import sys
import os

def get_last_friday():
  from datetime import datetime, timedelta
                                                              
  #today = datetime.today() - timedelta(days=2)
  today = datetime.today()
  #print(today)
                                                              
  weekday = today.weekday()
                                                              
  if weekday == 4:
    last_friday = today - timedelta(days=7)
  else:
    days_to_last_friday = (weekday - 4 + 7) % 7
    last_friday = today - timedelta(days=days_to_last_friday)
                                                              
  last_friday_formatted = last_friday.strftime("%Y%m%d")
  return(last_friday_formatted)


if __name__ == "__main__":
  date = get_last_friday()
  filename = "tdcc_data_%s.csv" % date
  folder = "data"
  if not os.path.exists(folder):
    os.makedirs(folder)
  filename_path = os.path.join(folder, filename)

  if not os.path.exists(filename_path):
    url = "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      with open(filename_path, "wb") as f:
        f.write(response.content)
        print("finished", file=sys.stderr)
    else:
      print("failed", file=sys.stderr)
  else:
    print("file already exist", file=sys.stderr)