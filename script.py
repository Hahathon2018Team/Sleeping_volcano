import time, requests

API_ADDRESS = "http://94.250.253.199:5000/api/set_data"

def main():
    ids = ["88942", "89336", "89520", "89589", "89600", "89604", "89639", "89655", "89667", "89709", "89726", "89730", "89731", "89751", "89758", "89760", "89781", "89783", "89788", "89791", "89792", "89793", "89806", "89808", "89815", "weather"]
    files = [open("extracted_dataset/"+section_id+".csv") for section_id in ids]
    for i in files:
        i.readline()
    for i in range(1000):
        for i in files:
            data = {'section_id':ids[files.index(i)], 'values':i.readline()}
            r = requests.post(url=API_ADDRESS, data=data)
            print(r.text)
            if r.text != "OK":
                print("ERROR")
        time.sleep(5)

if __name__ == '__main__':
    main()