def treat(wl):
    affis = wl.count("aff")
    calcis = wl.count("calc")
    varis = wl.count("var")


    if affis > 0:
        aff(wl)

    elif calcis > 0:
        print("iscalc")

    elif varis > 0:
        print("isvar")
    
    
