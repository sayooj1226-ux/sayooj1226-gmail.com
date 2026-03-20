# main.py - Enhanced UI with more units & color palette

import tkinter as tk
from tkinter import ttk, messagebox
from converter import (
    convert_length, convert_weight, convert_temperature,
    convert_speed, convert_area, convert_volume,
    convert_data, convert_time
)

# ─────────────────────────────────────────
#  🎨 Color Palette — Purple & Teal Theme
# ─────────────────────────────────────────
BG_MAIN    = "#0d0d1a"   # deep dark background
BG_CARD    = "#1a1a35"   # card background
BG_INPUT   = "#252550"   # input field background
HEADER_BG  = "#6c3483"   # purple header
ACCENT1    = "#9b59b6"   # purple accent
ACCENT2    = "#1abc9c"   # teal accent
BTN_CONV   = "#1abc9c"   # teal convert button
BTN_CLEAR  = "#e74c3c"   # red clear button
TEXT_WHITE = "#f0f0f0"
TEXT_GRAY  = "#95a5a6"
TEXT_GREEN = "#2ecc71"
TEXT_LABEL = "#bb8fce"   # light purple labels

FONT_TITLE  = ("Helvetica", 20, "bold")
FONT_SUB    = ("Helvetica", 9)
FONT_LABEL  = ("Helvetica", 11, "bold")
FONT_ENTRY  = ("Helvetica", 11)
FONT_RESULT = ("Helvetica", 14, "bold")
FONT_BTN    = ("Helvetica", 11, "bold")
FONT_FOOTER = ("Helvetica", 8)

# ─────────────────────────────────────────
#  📐 Unit Categories
# ─────────────────────────────────────────
UNITS = {
    "📏  Length": [
        "km", "m", "cm", "mm",
        "mile", "inch", "foot",
        "yard", "nautical mile"
    ],
    "⚖️  Weight": [
        "kg", "g", "mg", "lb",
        "oz", "ton", "carat", "stone"
    ],
    "🌡️  Temperature": ["C", "F", "K"],
    "🚀  Speed": [
        "m/s", "km/h", "mph",
        "knot", "ft/s"
    ],
    "🗺️  Area": [
        "m²", "km²", "cm²", "mm²",
        "acre", "hectare", "ft²", "inch²"
    ],
    "🧪  Volume": [
        "liter", "ml", "gallon", "cup",
        "pint", "quart", "fl oz",
        "m³", "cm³"
    ],
    "💾  Data": [
        "bit", "byte", "KB",
        "MB", "GB", "TB"
    ],
    "⏱️  Time": [
        "second", "minute", "hour",
        "day", "week", "month", "year"
    ],
}

CONVERT_FUNC = {
    "📏  Length":      convert_length,
    "⚖️  Weight":      convert_weight,
    "🌡️  Temperature": convert_temperature,
    "🚀  Speed":       convert_speed,
    "🗺️  Area":        convert_area,
    "🧪  Volume":      convert_volume,
    "💾  Data":        convert_data,
    "⏱️  Time":        convert_time,
}

# ─────────────────────────────────────────
#  Category accent colors
# ─────────────────────────────────────────
CATEGORY_COLORS = {
    "📏  Length":      "#3498db",
    "⚖️  Weight":      "#e67e22",
    "🌡️  Temperature": "#e74c3c",
    "🚀  Speed":       "#1abc9c",
    "🗺️  Area":        "#2ecc71",
    "🧪  Volume":      "#9b59b6",
    "💾  Data":        "#f39c12",
    "⏱️  Time":        "#1abc9c",
}


# ─────────────────────────────────────────
#  App Class
# ─────────────────────────────────────────
class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter Pro")
        self.root.geometry("500x580")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_MAIN)
        self.build_ui()

    def build_ui(self):

        # ── Gradient Header ──
        header = tk.Frame(self.root,
                          bg=HEADER_BG, height=75)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="⚙️  Unit Converter Pro",
            font=FONT_TITLE,
            bg=HEADER_BG, fg=TEXT_WHITE
        ).pack(pady=10)

        # ── Tagline ──
        tk.Label(
            self.root,
            text="8 categories  •  40+ units  •  Instant results",
            font=FONT_SUB,
            bg=BG_MAIN, fg=ACCENT2
        ).pack(pady=6)

        # ── Colored category indicator bar ──
        self.indicator = tk.Frame(
            self.root, bg=ACCENT1, height=4)
        self.indicator.pack(fill="x",
                            padx=35, pady=2)

        # ── Card ──
        card = tk.Frame(self.root, bg=BG_CARD,
                        bd=0, relief="flat")
        card.pack(padx=35, pady=8,
                  fill="both", ipady=8)

        # ── Category ──
        self._row_label(card, "Category", 0)
        self.category_var = tk.StringVar(
            value=list(UNITS.keys())[0])
        cat_box = ttk.Combobox(
            card, textvariable=self.category_var,
            values=list(UNITS.keys()),
            state="readonly", width=24,
            font=FONT_ENTRY
        )
        cat_box.grid(row=0, column=1,
                     padx=15, pady=10)
        cat_box.bind("<<ComboboxSelected>>",
                     self.update_units)

        # ── From ──
        self._row_label(card, "From", 1)
        self.from_var = tk.StringVar()
        self.from_menu = ttk.Combobox(
            card, textvariable=self.from_var,
            state="readonly", width=24,
            font=FONT_ENTRY
        )
        self.from_menu.grid(row=1, column=1,
                            padx=15, pady=10)

        # ── To ──
        self._row_label(card, "To", 2)
        self.to_var = tk.StringVar()
        self.to_menu = ttk.Combobox(
            card, textvariable=self.to_var,
            state="readonly", width=24,
            font=FONT_ENTRY
        )
        self.to_menu.grid(row=2, column=1,
                          padx=15, pady=10)

        # ── Value ──
        self._row_label(card, "Value", 3)
        self.value_entry = tk.Entry(
            card, font=FONT_ENTRY, width=26,
            bg=BG_INPUT, fg=TEXT_WHITE,
            insertbackground=ACCENT2,
            relief="flat", bd=6
        )
        self.value_entry.grid(row=3, column=1,
                              padx=15, pady=10)
        # Bind Enter key
        self.value_entry.bind("<Return>",
                              lambda e: self.convert())

        # ── Buttons ──
        btn_frame = tk.Frame(self.root, bg=BG_MAIN)
        btn_frame.pack(pady=12)

        tk.Button(
            btn_frame, text="⚡  Convert",
            font=FONT_BTN,
            bg=BTN_CONV, fg=BG_MAIN,
            activebackground="#17a589",
            activeforeground=BG_MAIN,
            width=14, relief="flat",
            cursor="hand2",
            command=self.convert
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame, text="🗑  Clear",
            font=FONT_BTN,
            bg=BTN_CLEAR, fg=TEXT_WHITE,
            activebackground="#c0392b",
            activeforeground=TEXT_WHITE,
            width=10, relief="flat",
            cursor="hand2",
            command=self.clear
        ).grid(row=0, column=1, padx=10)

        # ── Result Box ──
        self.result_frame = tk.Frame(
            self.root, bg=BG_CARD,
            bd=0, relief="flat"
        )
        self.result_frame.pack(
            padx=35, fill="x", pady=5)

        self.result_label = tk.Label(
            self.result_frame,
            text="⬆️  Enter a value and click Convert",
            font=FONT_RESULT,
            bg=BG_CARD, fg=TEXT_GRAY,
            wraplength=400, pady=15
        )
        self.result_label.pack()

        # ── Footer ──
        tk.Label(
            self.root,
            text="Unit Converter Pro v3.0  •  Python & Tkinter",
            font=FONT_FOOTER,
            bg=BG_MAIN, fg=TEXT_GRAY
        ).pack(side="bottom", pady=8)

        # Load defaults
        self.update_units()
        self._apply_style()

    def _row_label(self, parent, text, row):
        tk.Label(
            parent, text=text,
            font=FONT_LABEL,
            bg=BG_CARD, fg=TEXT_LABEL,
            width=10, anchor="w"
        ).grid(row=row, column=0,
               padx=15, pady=10, sticky="w")

    def _apply_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
            fieldbackground=BG_INPUT,
            background=BG_INPUT,
            foreground=TEXT_WHITE,
            selectbackground=BG_INPUT,
            selectforeground=TEXT_WHITE,
            arrowcolor=ACCENT2
        )
        style.map("TCombobox",
            fieldbackground=[("readonly", BG_INPUT)],
            foreground=[("readonly", TEXT_WHITE)]
        )

    def update_units(self, event=None):
        category = self.category_var.get()
        units = UNITS[category]
        self.from_menu["values"] = units
        self.to_menu["values"] = units
        self.from_var.set(units[0])
        self.to_var.set(units[1])

        # Update indicator bar color
        color = CATEGORY_COLORS.get(category, ACCENT1)
        self.indicator.configure(bg=color)

        self.result_label.config(
            text="⬆️  Enter a value and click Convert",
            fg=TEXT_GRAY
        )

    def convert(self):
        category  = self.category_var.get()
        from_unit = self.from_var.get()
        to_unit   = self.to_var.get()
        raw       = self.value_entry.get().strip()

        if not raw:
            messagebox.showwarning(
                "Missing Value",
                "Please enter a value!")
            return
        try:
            value = float(raw)
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number!")
            return

        result = CONVERT_FUNC[category](
            value, from_unit, to_unit)

        color = CATEGORY_COLORS.get(category, TEXT_GREEN)
        self.result_label.config(
            text=f"✅  {value} {from_unit}  =  "
                 f"{result:.6g} {to_unit}",
            fg=color,
            font=FONT_RESULT
        )

    def clear(self):
        self.value_entry.delete(0, tk.END)
        self.result_label.config(
            text="⬆️  Enter a value and click Convert",
            fg=TEXT_GRAY
        )


# ─────────────────────────────────────────
#  Run
# ─────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()