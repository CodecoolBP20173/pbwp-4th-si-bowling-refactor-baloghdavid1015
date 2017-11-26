def score(game):
    result = 0
    frame = 1
    global spare, strike
    spare = '/'
    strike = 'x'
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10  and get_value(game[i]) == 10:
            if game[i] == spare:
                result += get_value(game[i+1])
            elif game[i].lower() == strike:
                result += get_value(game[i+1])
                frame += 1
                if game[i+2] == spare:
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(game[i])
        if in_first_half == True:
            in_first_half = False
        elif not in_first_half:
            in_first_half = True
            frame += 1
        if game[i].lower() == strike:
            in_first_half = True
    return result

def get_value(char):
    try:
        return int(char)
    except ValueError:
        if char.lower() == strike or char == spare:
            return 10
        elif char == '-':
            return 0
        raise ValueError()
