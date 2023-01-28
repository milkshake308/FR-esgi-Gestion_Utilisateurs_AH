app = True
def prompt_yes_no(prompt: str):
    while True:
        response = input((prompt+' [o/N]: '))
        if response.lower() in ["y", "yes", "o", "oui"]:
            return True
        elif response.lower() in ["n", "no", "non"]:
            return False
        else:
            print("Merci de saisir 'oui' ou 'non'.")
            return prompt_yes_no(prompt)