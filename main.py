def willSigReach(radCoord, sigCoord, sigStrength):
    radX = radCoord[0]
    radY = radCoord[1]
    sigX = sigCoord[0]
    sigY = sigCoord[1]
    distance = ((abs(radX - sigX))**2 + (abs(radY - sigY)**2))**0.5
    if distance <= sigStrength:
        return True
    return False


def yoBro(radios, index, sig):
    # Assumes radio 0 is source
    i = 1
    prevRadio = radios[0]
    myBool = True
    while i < len(radios) and i <= index:
        myBool = willSigReach(radios[i], prevRadio, sig)
        prevRadio = radios[i]
        if not myBool:
            return False
        i += 1

    return myBool


def main():
    # Coord in format of X, Y
    # Takes index as position
    sig = 10  # Signal strength
    radios = {
        "Bob": [0, 0],
        "Garry": [2, 2],
        "Steven": [4, 7],
        "Steveb1": [7, 8],
        "Steven2": [0, -10]
    }

    index = "Steven2"
    print(yoBro(radios, index,  sig))


if __name__ == '__main__':
    main()
