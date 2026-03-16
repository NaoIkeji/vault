def show_menu():
    print("\n=== Vault Menu ===")
    print("1. データを追加")
    print("2. 集計を見る")
    print("3. 終了")

def main():
    print("Vault is ready to start!")
    while True:
        show_menu()
        choice = input("番号を選んでください: ")

        if choice == "1":
            print("データ追加機能はまだ準備中です。")
        elif choice == "2":
            print("集計機能はまだ準備中です。")
        elif choice == "3":
            print("Vault を終了します。")
            break
        else:
            print("無効な入力です。もう一度選んでください。")

if __name__ == "__main__":
    main()