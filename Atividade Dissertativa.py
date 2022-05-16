#Imports
import speech_recognition as sr

def obter_audio(microfone):
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa ou diga [FIM] para sair do programa: ")
        audio = microfone.listen(source)
    return audio

def transformar_audio_em_texto(microfone, audio):
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase
    except sr.UnkownValueError:
        print("Não entendi")


def escutar_microfone():
    microfone = sr.Recognizer()
    audio = obter_audio(microfone)
    texto =  transformar_audio_em_texto(microfone, audio)
    return texto

def calculaExpressao(parExpressao):
    try:

        if parExpressao[1]  == "+":
            return int(parExpressao[0]) + int(parExpressao[2])
        elif parExpressao[1]  == "-":
            return int(parExpressao[0]) - int(parExpressao[2])
        else:
            if parExpressao[0].isnumeric() == False or  parExpressao[3].isnumeric() == False:
                print("A entrada dos dados não é númerica: " + texto)
            else:
                print("O algoritmo trata apenas as operações de Adição e Subtração")
    except:
        print("A entrada dos dados não é númerica: " + texto)

if __name__ == '__main__':
    while True:
        texto = escutar_microfone()    
        if texto.upper() == "FIM":
            print("Fim de execução")
            break
        expressao = texto.split()
        resposta = ""
        if len(expressao) != 3:
            print("A entrada dos dados não é válida para o algoritmo: " + texto)
        else :
            resposta = calculaExpressao(expressao) 
            if resposta != None:
                print("Resposta para " + texto + ' é ' + str(resposta))
