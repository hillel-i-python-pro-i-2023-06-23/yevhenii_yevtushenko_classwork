def answer_validator(uid: int, answer: str) -> bool:
    answers_list = {
        "question_1": "answer_1",
        "question_2": "answer_2",
        "question_3": "answer_3",
        "question_4": "answer_4",
        "question_5": "answer_5",
    }

    if answer == answers_list[f"question_{uid}"]:
        return True

    return False