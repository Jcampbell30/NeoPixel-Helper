import tkinter as tk
from tkinter import ttk

APP_BG = "#020617"
CARD_BG = "#020617"
TEXT_MAIN = "#e5e7eb"
TEXT_SUB = "#9ca3af"
ACCENT = "#22c55e"


class NeoPixelTutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MicroPython NeoPixel Helper")
        self.root.geometry("920x540")
        self.root.minsize(820, 480)
        self.root.configure(bg=APP_BG)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("App.TFrame", background=APP_BG)
        style.configure("Card.TFrame", background=CARD_BG)
        style.configure(
            "Title.TLabel",
            background=APP_BG,
            foreground=TEXT_MAIN,
            font=("Segoe UI", 18, "bold"),
        )
        style.configure(
            "Body.TLabel",
            background=CARD_BG,
            foreground=TEXT_MAIN,
            font=("Segoe UI", 11),
            wraplength=540,
            justify="left",
        )
        style.configure(
            "Small.TLabel",
            background=CARD_BG,
            foreground=TEXT_SUB,
            font=("Segoe UI", 10),
            wraplength=540,
            justify="left",
        )
        style.configure(
            "Status.TLabel",
            background=APP_BG,
            foreground=TEXT_SUB,
            font=("Segoe UI", 10),
        )
        style.configure("TNotebook.Tab", padding=(10, 4))

        # Top bar
        top = ttk.Frame(root, style="App.TFrame", padding=(16, 10))
        top.pack(fill="x")

        ttk.Label(top, text="MicroPython NeoPixel Helper", style="Title.TLabel").pack(
            side="left"
        )

        self.status_var = tk.StringVar(
            value="Step through the tabs. Use the Code tab to generate a NeoPixel script."
        )
        status = ttk.Label(top, textvariable=self.status_var, style="Status.TLabel")
        status.pack(side="right")

        # Main area
        main = ttk.Frame(root, style="App.TFrame", padding=(16, 0, 16, 16))
        main.pack(fill="both", expand=True)

        self.notebook = ttk.Notebook(main)
        self.notebook.pack(fill="both", expand=True)

        self.build_overview_tab()
        self.build_wiring_tab()
        self.build_thonny_tab()
        self.build_code_tab()

    def make_card(self, title_text: str):
        frame = ttk.Frame(self.notebook, style="App.TFrame")
        card = ttk.Frame(frame, style="Card.TFrame", padding=20)
        card.pack(fill="both", expand=True, padx=12, pady=12)

        title = ttk.Label(
            card,
            text=title_text,
            background=CARD_BG,
            foreground=TEXT_MAIN,
            font=("Segoe UI", 14, "bold"),
        )
        title.pack(anchor="w", pady=(0, 10))

        return frame, card

    # --------- Tabs ----------

    def build_overview_tab(self):
        frame, card = self.make_card("Big Picture: NeoPixels + MicroPython")

        text = (
            "This app is focused on controlling a NeoPixel strip or ring with a Raspberry Pi Pico / Pico W.\n\n"
            "High-level steps:\n"
            "  1. Wire your NeoPixel DIN (data) pin to a GPIO on the Pico.\n"
            "  2. Provide 5V and GND to the strip (often from USB or external supply).\n"
            "  3. Flash MicroPython on the board (one-time) and connect in Thonny.\n"
            "  4. Use the Code tab here to generate a MicroPython script using the neopixel module.\n"
            "  5. Paste it into Thonny, save as main.py on the Pico, and run.\n\n"
            "You still create a Pin in MicroPython, but only to tell neopixel which GPIO you're using. "
            "You won't be toggling the pin manually — neopixel handles the LED timings for you."
        )

        ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
        self.notebook.add(frame, text="Overview")

    def build_wiring_tab(self):
        frame, card = self.make_card("Step 1: Wiring NeoPixels")

        text = (
            "Typical NeoPixel strip connections:\n"
            "  • DIN (data in) -> one of the Pico's GPIO pins (e.g. GP15).\n"
            "  • 5V (or VIN)   -> 5V supply (often USB 5V or separate 5V supply).\n"
            "  • GND           -> GND on the Pico AND the 5V supply (shared ground).\n\n"
            "Minimum wiring using the Pico's USB 5V (for small strips):\n"
            "  1. Connect NeoPixel GND to Pico GND.\n"
            "  2. Connect NeoPixel 5V/VIN to the Pico's VSYS/5V pin (check your board docs).\n"
            "  3. Connect NeoPixel DIN to a GPIO pin such as GP15.\n\n"
            "In code you'll pass that GPIO number into neopixel.NeoPixel, like this:\n"
            "  - Wiring to GP15    -> use Pin(15, Pin.OUT).\n"
            "  - If you wire to GP2 -> use Pin(2, Pin.OUT).\n\n"
            "For longer strips or lots of LEDs, it's better to power them from a separate 5V "
            "supply with a shared GND, and leave the Pico just handling data + logic."
        )

        ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
        self.notebook.add(frame, text="Wiring")

    def build_thonny_tab(self):
        frame, card = self.make_card("Step 2: MicroPython + Thonny")

        text = (
            "Once your Pico / Pico W has MicroPython installed (one-time):\n\n"
            "  1. Open Thonny and set the interpreter to 'MicroPython (Raspberry Pi Pico)'.\n"
            "  2. Plug in your Pico normally (not in BOOTSEL mode).\n"
            "  3. In Thonny, the REPL at the bottom should show a MicroPython prompt (>>>).\n\n"
            "To run NeoPixel code:\n"
            "  1. Go to the Code tab in this app.\n"
            "  2. Enter your GPIO pin, number of pixels, color and pattern.\n"
            "  3. Click 'Generate MicroPython Script'.\n"
            "  4. Copy the generated code into Thonny.\n"
            "  5. File → Save → 'This device' → name it main.py.\n"
            "  6. Click Run ▶. Your NeoPixels should light up.\n\n"
            "If nothing happens:\n"
            "  • Double-check your GPIO pin number matches your wiring.\n"
            "  • Check that 5V and GND are really connected.\n"
            "  • Try a very simple solid color script first to prove wiring."
        )

        ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
        self.notebook.add(frame, text="Thonny")

    def build_code_tab(self):
        frame, card = self.make_card("Step 3: Generate NeoPixel Code")

        opts = ttk.Frame(card, style="Card.TFrame")
        opts.pack(fill="x", pady=(0, 10))

        # Left: general NeoPixel settings
        left = ttk.Frame(opts, style="Card.TFrame")
        left.pack(side="left", padx=(0, 40))

        ttk.Label(left, text="GPIO pin (e.g. 15):", style="Small.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        self.pin_entry = ttk.Entry(left, width=8)
        self.pin_entry.insert(0, "15")
        self.pin_entry.grid(row=0, column=1, padx=(6, 0), pady=(0, 6))

        ttk.Label(left, text="Number of pixels:", style="Small.TLabel").grid(
            row=1, column=0, sticky="w"
        )
        self.count_entry = ttk.Entry(left, width=8)
        self.count_entry.insert(0, "8")
        self.count_entry.grid(row=1, column=1, padx=(6, 0), pady=(0, 6))

        # Right: color + pattern
        right = ttk.Frame(opts, style="Card.TFrame")
        right.pack(side="left")

        ttk.Label(right, text="Base color (0–255):", style="Small.TLabel").grid(
            row=0, column=0, columnspan=6, sticky="w"
        )

        ttk.Label(right, text="R:", style="Small.TLabel").grid(
            row=1, column=0, sticky="e", padx=(0, 2)
        )
        self.r_entry = ttk.Entry(right, width=5)
        self.r_entry.insert(0, "255")
        self.r_entry.grid(row=1, column=1, padx=(0, 10))

        ttk.Label(right, text="G:", style="Small.TLabel").grid(
            row=1, column=2, sticky="e", padx=(0, 2)
        )
        self.g_entry = ttk.Entry(right, width=5)
        self.g_entry.insert(0, "0")
        self.g_entry.grid(row=1, column=3, padx=(0, 10))

        ttk.Label(right, text="B:", style="Small.TLabel").grid(
            row=1, column=4, sticky="e", padx=(0, 2)
        )
        self.b_entry = ttk.Entry(right, width=5)
        self.b_entry.insert(0, "0")
        self.b_entry.grid(row=1, column=5, padx=(0, 0))

        ttk.Label(right, text="Pattern:", style="Small.TLabel").grid(
            row=2, column=0, sticky="w", pady=(8, 0)
        )

        self.pattern_var = tk.StringVar(value="solid")
        ttk.Radiobutton(
            right,
            text="Solid",
            value="solid",
            variable=self.pattern_var,
        ).grid(row=3, column=0, columnspan=3, sticky="w")
        ttk.Radiobutton(
            right,
            text="Blink",
            value="blink",
            variable=self.pattern_var,
        ).grid(row=3, column=3, columnspan=3, sticky="w")

        ttk.Radiobutton(
            right,
            text="Chase",
            value="chase",
            variable=self.pattern_var,
        ).grid(row=4, column=0, columnspan=3, sticky="w", pady=(0, 0))

        ttk.Label(right, text="Delay (ms):", style="Small.TLabel").grid(
            row=5, column=0, sticky="w", pady=(8, 0)
        )
        self.delay_entry = ttk.Entry(right, width=8)
        self.delay_entry.insert(0, "100")
        self.delay_entry.grid(row=5, column=1, padx=(0, 0), pady=(8, 0))

        # Generate button
        gen_btn = ttk.Button(
            card, text="Generate NeoPixel MicroPython Script", command=self.generate_code
        )
        gen_btn.pack(anchor="w", pady=(4, 6))

        info_text = (
            "Copy the generated code below into Thonny.\n"
            "Make sure the GPIO pin and number of pixels match your wiring.\n"
            "Start with a simple Solid pattern to confirm everything is working."
        )
        ttk.Label(card, text=info_text, style="Small.TLabel").pack(
            anchor="w", pady=(0, 6)
        )

        # Code display
        self.code_widget = tk.Text(
            card,
            height=16,
            width=90,
            bg="#020617",
            fg=TEXT_MAIN,
            insertbackground=TEXT_MAIN,
            bd=0,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#1f2937",
            font=("Consolas", 10),
        )
        self.code_widget.pack(fill="both", expand=True)
        self.code_widget.configure(state="disabled")

        self.generate_code()
        self.notebook.add(frame, text="Code")

    # --------- Code generator ----------

    def generate_code(self):
        # Pin, count, color, pattern, delay
        pin_num = self._safe_int(self.pin_entry, default=15)
        num_pixels = self._safe_int(self.count_entry, default=8)
        r = self._clamp_0_255(self.r_entry, default=255)
        g = self._clamp_0_255(self.g_entry, default=0)
        b = self._clamp_0_255(self.b_entry, default=0)
        delay_ms = self._safe_int(self.delay_entry, default=100)
        pattern = self.pattern_var.get()

        if pattern == "solid":
            code = self._generate_solid_code(pin_num, num_pixels, r, g, b)
        elif pattern == "blink":
            code = self._generate_blink_code(pin_num, num_pixels, r, g, b, delay_ms)
        else:  # chase
            code = self._generate_chase_code(pin_num, num_pixels, r, g, b, delay_ms)

        self.code_widget.configure(state="normal")
        self.code_widget.delete("1.0", tk.END)
        self.code_widget.insert("1.0", code)
        self.code_widget.configure(state="disabled")

        self.status_var.set(
            f"Generated {pattern} NeoPixel script for GP{pin_num} with {num_pixels} pixels."
        )

    # --------- Individual patterns ----------

    def _generate_solid_code(self, pin, count, r, g, b):
        return f"""import time
from machine import Pin
import neopixel

PIN_NUM = {pin}
NUM_PIXELS = {count}

np = neopixel.NeoPixel(Pin(PIN_NUM, Pin.OUT), NUM_PIXELS)

COLOR = ({r}, {g}, {b})

def fill(color):
    for i in range(NUM_PIXELS):
        np[i] = color
    np.write()

print("Setting all pixels to", COLOR)
fill(COLOR)

# Script exits here but the LEDs stay lit with the last color.
# If you want them to turn off after some time, uncomment below:

# time.sleep(5)
# fill((0, 0, 0))
"""

    def _generate_blink_code(self, pin, count, r, g, b, delay_ms):
        return f"""import time
from machine import Pin
import neopixel

PIN_NUM = {pin}
NUM_PIXELS = {count}
DELAY_MS = {delay_ms}

np = neopixel.NeoPixel(Pin(PIN_NUM, Pin.OUT), NUM_PIXELS)

ON_COLOR = ({r}, {g}, {b})
OFF_COLOR = (0, 0, 0)

def fill(color):
    for i in range(NUM_PIXELS):
        np[i] = color
    np.write()

print("Blinking all pixels", "ON_COLOR =", ON_COLOR, "with", DELAY_MS, "ms delay")

while True:
    fill(ON_COLOR)
    time.sleep_ms(DELAY_MS)
    fill(OFF_COLOR)
    time.sleep_ms(DELAY_MS)
"""

    def _generate_chase_code(self, pin, count, r, g, b, delay_ms):
        return f"""import time
from machine import Pin
import neopixel

PIN_NUM = {pin}
NUM_PIXELS = {count}
DELAY_MS = {delay_ms}

np = neopixel.NeoPixel(Pin(PIN_NUM, Pin.OUT), NUM_PIXELS)

ON_COLOR = ({r}, {g}, {b})
OFF_COLOR = (0, 0, 0)

def clear():
    for i in range(NUM_PIXELS):
        np[i] = OFF_COLOR
    np.write()

def chase():
    print("Starting chase pattern on", NUM_PIXELS, "pixels")
    pos = 0
    while True:
        clear()
        np[pos] = ON_COLOR
        np[(pos - 1) % NUM_PIXELS] = ON_COLOR
        np[(pos - 2) % NUM_PIXELS] = ON_COLOR
        np.write()
        pos = (pos + 1) % NUM_PIXELS
        time.sleep_ms(DELAY_MS)

clear()
chase()
"""

    # --------- Helpers ----------

    def _safe_int(self, entry, default):
        text = entry.get().strip()
        try:
            value = int(text)
            return value
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(0, str(default))
            return default

    def _clamp_0_255(self, entry, default):
        value = self._safe_int(entry, default)
        if value < 0:
            value = 0
        if value > 255:
            value = 255
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
        return value


def main():
    root = tk.Tk()
    app = NeoPixelTutorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

