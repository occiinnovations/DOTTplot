import numpy as np
import pytesseract as pt
import cv2 as cv2
import matplotlib.pyplot as plt

metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # type: ignore[attr-defined]
print("Feed active. Press 'q' to kill the window.")

LaTex = 1
Matplotlib = 2
Excel = 3

Algebra = 4
Calculus = 5
Statistics = 6

software_presets = np.array([LaTex, Matplotlib, Excel])
function_presets = np.array([Algebra, Calculus, Statistics])

software_choice = int(
    input("What is the software preset? software_presets:(1, 2, 3): "))
function_choice = int(
    input("What is the function preset? function_presets:(4, 5, 6): "))

if software_choice == 1:
    print("LaTex selected.")
elif software_choice == 2:
    print("Matplotlib selected.")
elif software_choice == 3:
    print("Excel selected.")


if function_choice == 4:
    print("Algebra selected.")
elif function_choice == 5:
    print("Calculus selected.")
elif function_choice == 6:
    print("Statistics selected.")

if software_choice < 1 or software_choice > 3:
    print("Invalid software preset choice. Please choose a number between 1 and 3.")
    exit()

if function_choice < 4 or function_choice > 6:
    print("Invalid function preset choice. Please choose a number between 4 and 6.")
    exit()


def Matplotlib_Algebra():
    x = np.linspace(f, g, h)
    y = "tesseract"  # Placeholder for OCR result
    plt.plot(x, y)


while True:
    ret, frame = metime.read()

    if not ret:
        print("Dropped frame.")
        break

    cv2.imshow('Camera View', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

metime.release()
cv2.destroyAllWindows()
