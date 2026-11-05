def battery_bars(percent):
    full = percent // 20
    empty = 5 - full
    return "[" + "#" * full + "." * empty + "]"