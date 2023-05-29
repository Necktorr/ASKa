from threading import Thread

import Voice
import UI_Window


if __name__ == '__main__':
    Thread(target = Voice.start_voice).start()
    Thread(target = UI_Window.start_ui).start()
    