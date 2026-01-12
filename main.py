from js import document, prompt

fahrenheit = float(prompt("Enter temperature in Fahrenheit:"))

celsius = (fahrenheit - 32) * 5 / 9

if celsius >= 37.8:
    result = f"{float(celsius)} °C - Fever"
else:
    result = f"{float(celsius)} °C - No Fever"

document.getElementById("output").innerText = result
