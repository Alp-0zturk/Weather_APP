import tkinter as tk
from tkinter import *
import Weather_App.weather_analysis as wa
import os
from PIL import Image, ImageTk

# get images for weather UI
path = "/Users/w/Desktop/Python/Weather_APP/img/"

def loadImages(path):
    imagesList = os.listdir(path)
    loadedImages = []
    for image in imagesList:
        img_path = os.path.join(path, image)
        try:
            img = Image.open(img_path)
            img = img.resize((20, 20))  # Resize the image to fit better
            tk_img = ImageTk.PhotoImage(img)
            loadedImages.append(tk_img)
            print(f"Loaded image: {img_path}")
        except Exception as e:
            print(f"Failed to load image: {img_path}, error: {e}")
    return loadedImages

def on_search(entry, result_labels):
    city = entry.get()
    weather_data = wa.get_weather_data(city)
    
    # Assuming weather_data is a dictionary with keys like 'temperature', 'humidity', etc.
    result_labels[0].config(text=f"Weather in {city}")
    result_labels[1].config(text=f"Temperature: {weather_data.get('temperature', 'N/A')}")
    result_labels[2].config(text=f"Humidity: {weather_data.get('humidity', 'N/A')}")
    result_labels[3].config(text=f"Wind Speed: {weather_data.get('wind_speed', 'N/A')}")
    result_labels[4].config(text=f"Description: {weather_data.get('description', 'N/A')}")

def main():
    window = tk.Tk()
    window.title('Fast Weather')
    window.geometry("300x400")

    loadedImages = loadImages(path)

    if not loadedImages:
        print("No images loaded")
        return

    # Keep a reference to the images to prevent garbage collection
    window.loadedImages = loadedImages

    # Create a frame
    Frm = Frame(window)
    Frm.pack(side=TOP, pady=10)

    # Add an entry widget
    modify = Entry(Frm, width=20)
    modify.pack(side=LEFT, fill=BOTH, expand=1)
    modify.focus_set()

    # Add a search button with an image
    search_button = Button(Frm, image=loadedImages[0], command=lambda: on_search(modify, result_labels), bd=0, highlightthickness=0)
    search_button.pack(side=LEFT, padx=(5, 0))

    # Add labels to display results
    result_labels = []
    for i in range(5):
        label = Label(window, text="")
        label.pack(pady=5)
        result_labels.append(label)

    result_labels[0].config(text="Enter a city name and click the search icon")

    window.mainloop()

if __name__ == "__main__":
    main()