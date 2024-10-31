
# Galerie de Photos Django

Ce projet est une galerie de photos simple construite avec Django. Il permet d'uploader, de visualiser, de trier, de modifier et de supprimer des photos. L'interface inclut une table où sont listées les photos avec des options de tri dynamique par date d'upload.

## Fonctionnalités

- **Uploader** une photo avec un titre et une image.
- **Lister** les photos dans un tableau avec les colonnes : Nom, Image, Date d'upload, Éditer, et Supprimer.
- **Trier** les photos par date d'upload, de la plus récente à la plus ancienne et inversement, avec un bouton de tri dynamique.
- **Modifier** une photo (titre et image).
- **Supprimer** une photo avec confirmation.

## Configuration

### Prérequis

- Python 3.12+
- Django 5.1.2
- Pillow (bibliothèque nécessaire pour gérer les images)

### Installation

1. **Clonez le projet :**

   ```bash
   git clone <URL_DU_DEPOT quand je l'aurais mis sur git>
   cd galery
   ```

2. **Créez un environnement virtuel :**

   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installez les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez la base de données :**

   Exécutez les commandes suivantes pour créer les tables dans la base de données.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créez un super utilisateur pour accéder à l'interface d'administration :**

   ```bash
   python manage.py createsuperuser
   ```

6. **Lancez les serveurs :**

   #### Serveur web sur un autre port

   ```bash
   python3 manage.py runserver 0.0.0.0:4242
   ```

   #### Serveur api (port 8080 par défaut)

   ```bash
   python3 manage.py runserver
   ```

7. **Accédez au site :**
   Ouvrez votre navigateur et allez sur `http://127.0.0.1:8000/photos/` pour voir la galerie.

## Fonctionnement du Tri Dynamique

La galerie permet de trier les photos par date d'upload, avec un bouton dynamique qui change de label et de comportement selon l'ordre actuel :

- **Trier par ordre croissant** : Affiche les photos de la plus ancienne à la plus récente.
- **Trier par ordre décroissant** : Affiche les photos de la plus récente à la plus ancienne.

### Mise en Place du Tri Dynamique

1. Dans `views.py`, la vue `PhotoListView` gère l'ordre de tri en fonction du paramètre `sort` dans l'URL.
2. Le template `list.html` utilise la variable `sort` pour ajuster le lien et le texte du bouton en fonction de l'ordre de tri actuel.

```python
class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'recent')
        if sort == 'recent':
            queryset = queryset.order_by('-uploaded_at')
        else:
            queryset = queryset.order_by('uploaded_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort', 'recent')
        return context
```

Dans `list.html` :

```html
<div style="text-align: right; margin-bottom: 10px;">
  {% if sort == 'recent' %}
    <a href="?sort=oldest" class="button-sort">Trier par ordre décroissant</a>
  {% else %}
    <a href="?sort=recent" class="button-sort">Trier par ordre croissant</a>
  {% endif %}
</div>
```

## Structure des Fichiers et Répertoires

- **galery/** : Répertoire principal du projet Django.
  - **photo/** : Application Django contenant les modèles, vues et templates.
    - **models.py** : Définition du modèle `Photo`.
    - **views.py** : Définition des vues `PhotoListView`, `PhotoDetailView`, `PhotoUploadView`, etc.
    - **templates/photo/** : Templates pour l'affichage de la galerie.
      - `list.html` : Affiche la liste des photos.
      - `detail.html` : Affiche le détail d'une photo.
      - `form.html` : Formulaire d'upload et de modification.
      - `confirm_delete.html` : Page de confirmation de suppression.
- **media/** : Répertoire de stockage des images uploadées.

Ce projet utilise Django et est conçu comme un exercice pour apprendre à manipuler les images, les vues basées sur des classes et le tri dynamique dans un tableau HTML.

## Communiquer avec l'API

Vous pouvez utiliser le fichier `req.rest` de l'extension REST de VS Code pour utiliser l'api après l'avoir lancé.
