import urllib, json, argparse
from datetime import datetime, timedelta
kota = "Surabaya"
negara = "Indonesia"
bulan = datetime.now().strftime("%m")
tahun = datetime.now().strftime("%Y")
d = datetime.today() - timedelta(days=1)
tgl = d.strftime("%d")

url = "http://api.aladhan.com/v1/calendarByCity?city="+kota+"&country="+negara+"&method=2&month="+bulan+"&year="+tahun
response = urllib.urlopen(url)
data = json.loads(response.read())
subuh = json.dumps(data['data'][int(tgl)]['timings']['Fajr'])
duhur = json.dumps(data['data'][int(tgl)]['timings']['Dhuhr'])
asr = json.dumps(data['data'][int(tgl)]['timings']['Asr'])
maghrib = json.dumps(data['data'][int(tgl)]['timings']['Maghrib'])
isha = json.dumps(data['data'][int(tgl)]['timings']['Isha'])
parser = argparse.ArgumentParser()

parser.add_argument('-s', '--subuh', action='store_true', help="Waktu subuh")
parser.add_argument('-d', '--duhur', action='store_true', help="Waktu duhur")
parser.add_argument('-a', '--asr', action='store_true', help="Waktu Asr")
parser.add_argument('-m', '--maghrib', action='store_true', help="Waktu Maghrib")
parser.add_argument('-i', '--isha', action='store_true', help="Waktu Isha")

args = parser.parse_args()

if args.subuh:
    print(subuh.strip('\"'))
elif args.duhur:
    print(duhur.strip('\"'))
elif args.asr:
    print(asr.strip('\"'))
elif args.maghrib:
    print(maghrib.strip('\"'))
elif args.isha:
    print(isha.strip('\"'))
else:
    parser.print_help()
