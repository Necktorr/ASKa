
import config
import stt
import tts
from fuzzywuzzy import fuzz
import datetime
from num2t4ru import num2text
import webbrowser
import random
from yaweather import UnitedKingdom, YaWeather
from modules.weather import get_weather

class Voice_Module():
    def __init__(self) -> None:
        self.stt_module = stt.VA_Listen_Module()
        print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")
            
    def va_com(self, voice: str, login: bool):
        cmd = self.recognize_cmd(self.filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.va_speak("Что?")
        else:
            self.execute_cmd(cmd['cmd'], login)
                    
    def va_respond(self, voice: str):
        print(voice)
        if voice.startswith(config.VA_IDEN):
            self.va_com(voice, login = True)
            
            
        elif voice.startswith(config.VA_ALIAS):
            self.va_com(voice, login = False)
                
                


    def filter_cmd(self, raw_voice: str):
        cmd = raw_voice

        for x in config.VA_ALIAS:
            cmd = cmd.replace(x, "").strip()

        for x in config.VA_TBR:
            cmd = cmd.replace(x, "").strip()

        return cmd


    def recognize_cmd(self, cmd: str):
        rc = {'cmd': '', 'percent': 0}
        for c, v in config.VA_CMD_LIST.items():

            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > rc['percent']:
                    rc['cmd'] = c
                    rc['percent'] = vrt

        return rc


    def execute_cmd(self, cmd: str, login):
        if cmd == 'help':
            # help
            text = "Я умею: ..."
            text += "произносить время ..."
            text += "рассказывать анекдоты ..."
            text += "и открывать браузер"
            text += "показывать погоду"
            tts.va_speak(text)
            pass
        elif cmd == 'ctime':
            # current time
            now = datetime.datetime.now()
            text = "Сейчас " + num2text(now.hour) + "часов " + num2text(now.minute)+"минут"
            tts.va_speak(text)
            
        elif cmd == 'browser' and login:
            url = "https://google.com/search?q="
            webbrowser.get().open(url)
            
        elif cmd == 'weather':
            print(get_weather())
        elif cmd == 'joke':
            jokes = ['Как смеются программисты? ... ехе ехе ехе',
                    'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                    'Программист это машина для преобразования кофе в код']

            tts.va_speak(random.choice(jokes))

        #elif cmd == 'open_browser':
            #webbrowser.open('https://vk.com/', new=2)
            #chrome_path = 'C:\Program Files\Google\Chrome\Application %s'
            #webbrowser.get(chrome_path).open("http://python.org")


    def start(self):
        self.stt_module.start_listen(self.va_respond)

    def stop(self):
        self.stt_module.stop_listen()

def start_voice():
    vm = Voice_Module()
    vm.start()
    
if __name__ == "__main__":
    start_voice()
