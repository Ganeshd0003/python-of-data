# this not makes any sense but consider 1 and 0 are equal  just for same cases using pipe |

i = 0

match i:
    case 0 | 1: print("pipe condtion")
    case 2: print("2")
    case 3: print("3")
    case 4: print("4")
    case _: print("No match")
