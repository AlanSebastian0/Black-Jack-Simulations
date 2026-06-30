def stand_16(score: int, dealer_visible: str) -> str: #strat stand when score is 16 or more
    if score >= 16:
        return "S"
    else:
        return "H"
