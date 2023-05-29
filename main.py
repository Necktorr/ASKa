from threading import Thread
import multiprocessing

import Voice
import UI_Window


if __name__ == '__main__':
    p1 = multiprocessing.Process(target = Voice.start_voice)
    p2 = multiprocessing.Process(target = UI_Window.start_ui)
    
    p1.start()
    p2.start()
    # starting Processes here parallel by using start function.
    p1.join()
    # this join() will wait until the calc_square() function is finished.
    p2.join()