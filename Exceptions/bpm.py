def get_age():
    age = int(input('Please enter your age:\n'))
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age

def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70
    return heart_rate

try:
    age = get_age()
    rate = fat_burning_heart_rate(age)
    print(f'Fat burning heart rate for a {age} year-old: {rate:.1f} bpm')
except ValueError as excpt:
    print(excpt)
    print('Could not calculate heart rate info.')