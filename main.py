import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("Vault")
    root.geometry("400x500")
    root.configure(bg="#f0f8f8")  # 優しい背景色

    # --- ヘッダー（ロゴ） ---
    image = Image.open("vault_logo.png")
    image = image.resize((120, 120))
    logo = ImageTk.PhotoImage(image)

    logo_label = tk.Label(root, image=logo, bg="#f0f8f8")
    logo_label.image = logo
    logo_label.pack(pady=20)

    # --- メインメニュー（ボタン） ---
    button_frame = tk.Frame(root, bg="#f0f8f8")
    button_frame.pack(pady=10)

    btn_add = tk.Button(button_frame, text="データを追加", width=20, height=2)
    btn_add.pack(pady=5)

    btn_view = tk.Button(button_frame, text="集計を見る", width=20, height=2)
    btn_view.pack(pady=5)

    btn_settings = tk.Button(button_frame, text="設定", width=20, height=2)
    btn_settings.pack(pady=5)

    btn_exit = tk.Button(button_frame, text="終了", width=20, height=2, command=root.quit)
    btn_exit.pack(pady=5)

    # --- フッター ---
    footer = tk.Label(root, text="Your data stays with you.", bg="#f0f8f8", fg="#555")
    footer.pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()