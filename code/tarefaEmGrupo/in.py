from InquirerPy import inquirer
nome= inquirer.text("Qual o seu nome?  ") .execute()
cor= inquirer.select("qual a sua cor favorita? ",choices=["azul" ,"verde" , "vermelho"] ).execute()