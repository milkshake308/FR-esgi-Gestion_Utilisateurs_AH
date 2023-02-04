def generate_login(p_nom, p_prenom):
    p_nom = p_nom.replace(" ", "")
    p_prenom = p_prenom.strip()
    return p_prenom[0]+p_nom

