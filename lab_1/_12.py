#12. Дано значення кута α в градусах (0 ≤ α < 360). Обчислити значення цього ж кута в радіанах, враховуючи, що 180 ° = π радіанів.
#У якості значення π використовувати 3.14.
deg = float(input("Angle in degree (0-360): "))
if 0<=deg<=360:
    rad = deg *3.14 / 180
    print(rad)

else: print("the angle must be between 0 and 360")

