from PIL.ImageOps import cover


def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8 :
        print("breakfast time")
    elif 12 <= convert(time) <= 13 :
        print("lunch time")
    elif 18 <= convert(time) <= 19 :
        print("dinner time")



def convert(time):
    if "a.m." in time :
        time = time.strip("a.m.").strip()
        if time == "12:00" :
            time = "00:00"
    elif "p.m." in time :
        time = time.strip("p.m.").strip()
        time = time.split(":")
        hour = int(time[0])
        minute = int(time[1])
        time = f"{hour+12}:{minute}"
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[1])
    time = hour + (minute/60)
    return time


if __name__ == "__main__":
    main()