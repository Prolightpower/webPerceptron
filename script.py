from pyscript import document

weights = [0.23, -0.32, 0.21, 0.09, 0.17, -0.42, 0.46, 0.16, 0.24, 0.03,
           -0.11, -0.2, 0.39, -0.08, -0.05, -0.35, 0.16, 0.06, 0.2, 0.0,
           0.31, -0.05, -0.06, -0.3, -0.33]
bias = -0.03

def activation_function(z):
    if z >= 0:
        return 1
    else:
        return 0

def predict(pixels):
    z = 0
    for i in range(len(weights)):
        z = z + weights[i] * pixels[i]
    z = z + bias
    return activation_function(z)

def get_pixels():
    cells = document.querySelectorAll(".cell")
    pixels = []
    for c in cells:
        if "on" in c.className:
            pixels.append(1)
        else:
            pixels.append(0)
    return pixels

def classify(event):
    pixels = get_pixels()
    label = predict(pixels)
    result = document.getElementById("test-output")
    if label == 0:
        result.innerText = "L"
    else:
        result.innerText = "T"

def load_l(event):
    pattern = [1, 0, 0, 0, 0,
               1, 0, 0, 0, 0,
               1, 0, 0, 0, 0,
               1, 0, 0, 0, 0,
               1, 1, 1, 1, 1]
    cells = document.querySelectorAll(".cell")
    for i, c in enumerate(cells):
        if pattern[i] == 1:
            c.classList.add("on")
        else:
            c.classList.remove("on")

def load_t(event):
    pattern = [1, 1, 1, 1, 1,
               0, 0, 1, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 1, 0, 0,
               0, 0, 1, 0, 0]
    cells = document.querySelectorAll(".cell")
    for i, c in enumerate(cells):
        if pattern[i] == 1:
            c.classList.add("on")
        else:
            c.classList.remove("on")

def clear_grid(event):
    cells = document.querySelectorAll(".cell")
    for c in cells:
        c.classList.remove("on")
    document.getElementById("test-output").innerText = "-"

