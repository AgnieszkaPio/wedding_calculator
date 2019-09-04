def convert_second (time):
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    if hour == 1:
        hh = "godzina"
    elif hour ==2 or hour ==3 or hour ==4 or hour == 22 or hour == 23:
        hh = "godziny"
    else:
        hh = "godzin"

    print(f'{hour} {hh}, {minutes} minut, {seconds} sekund')

convert_second(11783)