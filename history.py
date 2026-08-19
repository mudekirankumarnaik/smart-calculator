def save_history(text):
    file = open("history.txt", "a")
    file.write(text + "\n")
    file.close()


def show_history():
    file = open("history.txt", "r")
    history = file.read()
    file.close()

    return history
