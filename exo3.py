def calculate_discount(price, discount_percent):
    """
    Calcule le prix final après application d'une réduction.
    Si la réduction est >= 20%, on l'applique, sinon on retourne le prix original.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Programme principal ---
# Demander les infos à l'utilisateur
price = float(input("Entrez le prix original de l'article : "))
discount_percent = float(input("Entrez le pourcentage de réduction : "))

# Calculer le prix final
final_price = calculate_discount(price, discount_percent)

# Afficher le résultat
if discount_percent >= 20:
    print(f"Prix final après réduction : {final_price:.2f}")
else:
    print(f"Aucune réduction appliquée. Prix original : {final_price:.2f}")
