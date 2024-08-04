import tkinter as tk


def update_result(*args):
    try:
        taxe_vendeur = taxe_slider.get() / 100  # Convertit en pourcentage
        cout_km_client = float(km_client_entry.get())
        cout_kg_client = float(kg_client_entry.get())
        nb_kilometres = float(nb_km_entry.get())
        cout_fixe = float(cout_fixe_entry.get())
        cout_km_concu = float(cout_km_concu_entry.get())

        result = 10 * taxe_vendeur + cout_km_client * nb_kilometres + cout_kg_client
        required = cout_fixe + cout_km_concu * nb_kilometres
        benefit = result - required

        result_label.config(text=f"Résultat : {result:.2f}")
        required_label.config(text=f"Valeur requise : {required:.2f}")
        benefit_label.config(text=f"Bénéfice possible : {benefit:.2f}")
    except ValueError:
        result_label.config(text="Résultat : N/A")
        required_label.config(text="Valeur requise : N/A")
        benefit_label.config(text="Bénéfice possible : N/A")


def update_km_client_from_slider(val):
    km_client_entry.delete(0, tk.END)
    km_client_entry.insert(0, val)
    update_result()


def update_kg_client_from_slider(val):
    kg_client_entry.delete(0, tk.END)
    kg_client_entry.insert(0, val)
    update_result()


def update_nb_km_from_entry(*args):
    update_result()


# Crée la fenêtre principale
root = tk.Tk()
root.title("Calculateur interactif")

# Crée les curseurs
taxe_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Taxe Vendeur (%)")
taxe_slider.pack()
taxe_slider.bind("<Motion>", lambda event: update_result())

km_client_slider = tk.Scale(root, from_=0, to=10, orient="horizontal", label="Coût KM Client")
km_client_slider.pack()
km_client_slider.bind("<Motion>", lambda event: update_km_client_from_slider(km_client_slider.get()))

kg_client_slider = tk.Scale(root, from_=0, to=10, orient="horizontal", label="Coût KG Client")
kg_client_slider.pack()
kg_client_slider.bind("<Motion>", lambda event: update_kg_client_from_slider(kg_client_slider.get()))

# Crée les entrées pour les coûts fixes, les valeurs et le nombre de kilomètres
tk.Label(root, text="Coût Fixe:").pack()
cout_fixe_entry = tk.Entry(root)
cout_fixe_entry.pack()
cout_fixe_entry.bind("<KeyRelease>", update_result)

tk.Label(root, text="Coût KM Concu:").pack()
cout_km_concu_entry = tk.Entry(root)
cout_km_concu_entry.pack()
cout_km_concu_entry.bind("<KeyRelease>", update_result)

tk.Label(root, text="Coût KM Client:").pack()
km_client_entry = tk.Entry(root)
km_client_entry.pack()
km_client_entry.insert(0, km_client_slider.get())
km_client_entry.bind("<KeyRelease>", update_result)

tk.Label(root, text="Coût KG Client:").pack()
kg_client_entry = tk.Entry(root)
kg_client_entry.pack()
kg_client_entry.insert(0, kg_client_slider.get())
kg_client_entry.bind("<KeyRelease>", update_result)

tk.Label(root, text="Nombre de Kilomètres:").pack()
nb_km_entry = tk.Entry(root)
nb_km_entry.pack()
nb_km_entry.bind("<KeyRelease>", update_nb_km_from_entry)

# Crée les labels pour afficher les résultats
result_label = tk.Label(root, text="Résultat : ")
result_label.pack()

required_label = tk.Label(root, text="Valeur requise : ")
required_label.pack()

benefit_label = tk.Label(root, text="Bénéfice possible : ")
benefit_label.pack()

# Lance l'application
root.mainloop()
