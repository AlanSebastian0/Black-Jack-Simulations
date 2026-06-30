def copycat_AI(score: int, dealer_visible: str) -> str:
    if score >= 17:
        return "S"
    else:
        return "H"
