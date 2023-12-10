import random
import tkinter as tk

def get_computer_choice():
    return random.choice(["taş", "kağıt", "makas"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Berabere"
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!"
    else:
        return "Bilgisayar kazandı!"

def play_game():
    user_choice = user_choice_var.get().lower()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Sonuç: {result}")

# TKinter arayüzü oluşturma
root = tk.Tk()
root.title("Taş-Kağıt-Makas Oyunu")

# Kullanıcı seçimi için giriş alanı
user_choice_var = tk.StringVar()
user_choice_label = tk.Label(root, text="Seçiminiz (Taş, Kağıt, Makas):")
user_choice_entry = tk.Entry(root, textvariable=user_choice_var)
user_choice_label.pack()
user_choice_entry.pack()

# Oyunu başlatan düğme
play_button = tk.Button(root, text="Oyna", command=play_game)
play_button.pack()

# Oyun sonucunu gösteren etiket
result_label = tk.Label(root, text="Sonuç:")
result_label.pack()

# Arayüzü başlatma
root.mainloop()
