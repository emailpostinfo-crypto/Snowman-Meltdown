import game_logic


def main():
    while True:
        game_logic.play_game()
        if game_logic.play_again() == False:
            break


if __name__ == "__main__":
    main()