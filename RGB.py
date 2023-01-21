def rgb(r, g, b):
    r = min(255, max(0, r))
    g = min(255, max(0, g))
    b = min(255, max(0, b))
    return "{:02X}{:02X}{:02X}".format(r, g, b)
