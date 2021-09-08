from datetime import datetime, timedelta
import re

def main():
    f = open("/home/sam/Coding/discord_role_stripper/role_subs.txt", "r")
    txt = f.read()
    f.close()

    data = re.findall("(\d{2}/\d{2}/\d{4}).*\n.*approved.*to (\D*farme[r I]+)", txt)

    role_reach_times = {}

    for pair in data:
        role = pair[1].replace('III', '3').replace('II', '2')
        if len(role.split()) == 1:
            role = role + " 1"
        [day, month, year] = list(map(int, pair[0].split("/")))
        dt = datetime(year, month, day)
        timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)
        role_reach_times[role] = timestamp

    add_list =  '!!addmyroles ' + str(role_reach_times)
    return add_list

if __name__ == "__main__":
    print(main())