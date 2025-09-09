import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    """
    Télécharge une image depuis une URL et l'enregistre dans Fetched_Images
    Retourne True si succès, False sinon
    """
    try:
        # Récupérer l'image
        response = requests.get(url.strip(), timeout=10)
        response.raise_for_status()

        # Vérifier que le contenu est bien une image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Ignoré (pas une image) : {url}")
            return False

        # Extraire le nom du fichier de l'URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # si l'URL ne contient pas de nom de fichier
            ext = content_type.split("/")[-1]  # exemple : "jpeg"
            filename = f"downloaded_image.{ext}"

        # Éviter les doublons
        filepath = os.path.join("Fetched_Images", filename)
        counter = 1
        while os.path.exists(filepath):
            name, ext = os.path.splitext(filename)
            filepath = os.path.join("Fetched_Images", f"{name}_{counter}{ext}")
            counter += 1

        # Sauvegarde
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Récupération réussie : {os.path.basename(filepath)}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Erreur de connexion pour {url} : {e}")
        return False
    except Exception as e:
        print(f"✗ Une erreur est survenue pour {url} : {e}")
        return False


def main():
    print("🌍 Bienvenue dans Ubuntu Image Fetcher (version multi-URL)")
    print("Un outil pour collecter consciencieusement des images sur le Web\n")

    # Créer le répertoire si nécessaire
    os.makedirs("Fetched_Images", exist_ok=True)

    # Saisie utilisateur
    urls = input("Veuillez entrer une ou plusieurs URLs (séparées par des virgules) : ")
    urls_list = urls.split(",")

    print("\n--- Téléchargement en cours ---\n")
    success_count = 0

    for url in urls_list:
        if fetch_image(url):
            success_count += 1

    print(f"\nRésumé : {success_count}/{len(urls_list)} images téléchargées avec succès.")
    print("Connexion renforcée. Communauté enrichie. Ubuntu 🙌")


if __name__ == "__main__":
    main()
