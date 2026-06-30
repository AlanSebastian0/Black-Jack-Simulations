def stand_18(score: int, dealer_visible: str) -> str:
    if score >= 18:
        return "S"
    else:
        return "H"

