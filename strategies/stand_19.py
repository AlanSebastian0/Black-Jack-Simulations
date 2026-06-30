def stand_19(score: int, dealer_visible: str) -> str:
    if score >= 19:
        return "S"
    else:
        return "H"

