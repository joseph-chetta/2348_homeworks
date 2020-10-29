# Joseph Chetta 1640405

def get_age():
    age = int(input())
    if not 18 < age < 75:
        raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * .7
    return heart_rate


if __name__ == '__main__':
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, heart_rate))
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")
