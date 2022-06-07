from playsound import playsound


def play_celebratory_song():
    return playsound("sounds/Celebratory.wav")


def play_wrong_answer():
    return playsound("sounds/Wrong_choice.wav")


def play_correct_answer():
    return playsound("sounds/correct_answer.wav")


def play_game_over():
    return playsound("sounds/gameover.wav")


def play_game_over_wrongchoice():
    return playsound("sounds/gameover_wrong_choice.wav")


def play_quiz_incorrect():
    return playsound("sounds/quiz_incorrect.wav")


def play_win_points():
    return playsound("sounds/acheivement.wav")


def level_complete():
    return playsound("sounds/level_complete.wav")
