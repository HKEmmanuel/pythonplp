def modify_content(content):
    """
    Fonction qui transforme le contenu du fichier.
    Ici, juste pour l'exemple, on met tout en MAJUSCULES.
    """
    return content.upper()


# --- Programme principal ---
filename = input("Entrez le nom du fichier à lire : ")

try:
    # Lecture du fichier original
    with open(filename, "r", encoding="utf-8") as infile:
        content = infile.read()

    # Modification du contenu
    modified_content = modify_content(content)

    # Nouveau nom pour le fichier de sortie
    new_filename = "modified_" + filename

    # Écriture du nouveau fichier
    with open(new_filename, "w", encoding="utf-8") as outfile:
        outfile.write(modified_content)

    print(f"✅ Fichier modifié créé avec succès : {new_filename}")

except FileNotFoundError:
    print("❌ Erreur : Le fichier n'existe pas.")
except PermissionError:
    print("❌ Erreur : Impossible de lire ou d'écrire ce fichier (problème de permissions).")
except Exception as e:
    print(f"⚠️ Une erreur inattendue est survenue : {e}")
