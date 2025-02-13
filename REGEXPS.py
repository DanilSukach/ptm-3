import json


REGEXPS_PATH = "REGEXPS.json"
REGEXPS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
    "height": "^[1-3]\\.\\d{2}$",
    "snils": "^\\d{11}$",
    "passport": "^\\d{2}\\s\\d{2}\\s\\d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\\s-]+$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",
    "issn": "^\\d{4}-\\d{4}$",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "time": "^([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d)\\.(\\d{1,6})$"
}

if __name__ == "__main__":
    with open(REGEXPS_PATH, 'w') as fp:
        json.dump(REGEXPS, fp)
