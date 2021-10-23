def main ():

    altura = float (input ("Informe sua altura: "))
    peso   = float (input ("Informe seu peso: "))
    IMC    = peso / (altura **2)

    print ("Seu indice de massa corporica eh: ", IMC)
    
    if IMC< 18.5:
        print ("Você está abaixo do peso com", IMC, " sua massa corporica  deveria ser maior que 18.5")

        if IMC >24.9:
            print ("Você está acima do peso com", IMC, " sua massa corporica deveria ser menor que 24.9")

            if IMC >18.5  IMC <24.9:
            print ("você esta dentro do peso ideal com ", IMC):
main()


