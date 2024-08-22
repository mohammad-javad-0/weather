import requests as rq
import tkinter as tk
from tkinter import messagebox


class Error400(Exception):
    pass


class Error404(Exception):
    pass


root = tk.Tk()
root.geometry("600x200")
root.resizable(False, False)
icon_photo = tk.PhotoImage(file="image/icon_photo.png")
root.iconphoto(False, icon_photo)
root.title("Weather App")
root.config(bg="#11D9F9")


def temperature_show():
    q = search_var.get()
    appid = "9d4b0d707df609e51c08d987d3ec0d37"
    request = rq.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={appid}"
    )
    try:
        result = request.json()
        if result["cod"] == "400":
            raise Error400()
        elif result["cod"] == "404":
            raise Error404()

    except Error400:
        messagebox.showerror(title="Weather App", message="Nothing to geocode")
    except Error404:
        messagebox.showerror(title="Weather App", message="city not found")
    else:
        temp_window = tk.Tk()
        temp_window.geometry("800x400")
        temp_window.resizable(False, False)
        temp_window.title("TEMPERATURE")
        temp_window.config(bg="#7CB2AF")

        tk.Label(
            temp_window,
            text=f"{result['sys']['country']}/{result['name']}",
            font="arial 20 bold",
            bg="#000",
            fg="#FF0000",
        ).place(x=250, y=20, width=300)

        lbl_list = [
            {"name": "Temp", "value": f"\t{result['main']['temp'] - 273.15:.2f} °C"},
            {"name": "Description", "value": result["weather"][0]["main"]},
            {"name": "Humidity", "value": f"{result['main']['humidity']} %"},
            {"name": "Wind", "value": f"\t{result['wind']['speed'] * 3.6:.2f} km/h"},
            {"name": "Sea level", "value": f"{result['main']['pressure']} hPa"},
        ]
        for num, lbl_text in enumerate(lbl_list):
            tk.Label(
                temp_window,
                text=f"{lbl_text['name']}:\t\t\t\t\t{lbl_text['value']}",
                font="arial 15 bold",
                bg="#7CB2AF",
            ).place(x=50, y=(num + 2) * 50)


icon_heading = tk.PhotoImage(file="image/icon_heading.png").subsample(2, 2)
lbl_heading = tk.Label(
    root,
    text="WEATHER",
    compound="right",
    image=icon_heading,
    font="arial 20 bold",
    bg="#fff",
    fg="#11D9F9",
)

search_var = tk.StringVar()
ent_search = tk.Entry(
    root,
    textvariable=search_var,
    font="arial 15",
    bd=0,
)

search_image = tk.PhotoImage(file="image/search_image.png").subsample(10, 10)
btn_search = tk.Button(
    root,
    image=search_image,
    bg="#11D9F9",
    activebackground="#11D9F9",
    bd=0,
    command=temperature_show,
)

lbl_heading.place(x=0, y=0, width=600, height=100)
ent_search.place(x=100, y=130, width=350, height=30)
btn_search.place(x=460, y=130)

root.mainloop()
