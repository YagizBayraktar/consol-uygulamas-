def mayıntarlası():
    import random
    import os

    class Minesweeper:      
     def __init__(self):
        """Oyunu başlat ve temel ayarları yap"""
        print("=== MAYIN TARLASI OYUNU ===\n")
        self.board_size = self.get_valid_input("Oyun tahtası boyutunu girin (örn: 8): ", 4, 20)
        self.num_mines = self.get_valid_input("Mayın sayısını girin: ", 1, self.board_size**2 - 1)
        
        # Oyun tahtalarını başlat
        self.player_board = [['.' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mine_board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        self.game_won = False
        self.moves = 0
        
        # Mayınları yerleştir
        self.place_mines()

    def get_valid_input(self, prompt, min_val, max_val):
        """Geçerli kullanıcı girişi al"""
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"Lütfen {min_val} ile {max_val} arasında bir değer girin.")
            except ValueError:
                print("Geçersiz giriş! Lütfen bir sayı girin.")

    def place_mines(self):
        """Mayınları rastgele yerleştir ve komşu sayılarını hesapla"""
        mines_placed = 0
        
        while mines_placed < self.num_mines:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            
            # Eğer bu hücrede zaten mayın yoksa
            if self.mine_board[row][col] != -1:
                self.mine_board[row][col] = -1  # Mayın koy
                mines_placed += 1
                
                # Komşu hücrelerin sayılarını güncelle
                for i in range(max(0, row-1), min(self.board_size, row+2)):
                    for j in range(max(0, col-1), min(self.board_size, col+2)):
                        if self.mine_board[i][j] != -1:  # Mayın değilse
                            self.mine_board[i][j] += 1

    def display_board(self, show_mines=False):
        """Oyun tahtasını ekranda göster"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        
        print("   " + " ".join(f"{i+1:2}" for i in range(self.board_size)))
        print("   " + "---" * self.board_size)
        
        for i in range(self.board_size):
            print(f"{i+1:2}|", end=" ")
            for j in range(self.board_size):
                if show_mines and self.mine_board[i][j] == -1:
                    print(" * ", end="")  # Mayın göster
                elif self.player_board[i][j] == 'F':
                    print(" F ", end="")  # Bayrak
                elif self.player_board[i][j] == '.':
                    print(" . ", end="")  # Kapalı hücre
                elif self.player_board[i][j] == ' ':
                    print("   ", end="")  # Boş hücre
                else:
                    print(f" {self.player_board[i][j]} ", end="")  # Sayı
            print()
        print()

    def get_player_move(self):
        """Kullanıcıdan hamle al"""
        while True:
            try:
                move = input("Hamle girin (örn: '3 4' açmak için, '3 4 f' bayrak için): ").strip().lower()
                parts = move.split()
                
                if len(parts) < 2:
                    print("Geçersiz format! Örnek: '3 4' veya '3 4 f'")
                    continue
                
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                
                # Geçerli satır/sütun kontrolü
                if not (0 <= row < self.board_size and 0 <= col < self.board_size):
                    print(f"Satır ve sütun 1-{self.board_size} arasında olmalı.")
                    continue
                
                # Eylem belirleme
                action = 'flag' if len(parts) > 2 and parts[2] == 'f' else 'reveal'
                
                return row, col, action
                
            except ValueError:
                print("Geçersiz giriş! Lütfen sayıları doğru formatta girin.")

    def reveal_cell(self, row, col):
        """Hücreyi aç ve gerekirse yayılım yap"""
        # Eğer hücre zaten açıksa veya bayraklıysa
        if self.player_board[row][col] != '.':
            return
        
        # Mayına bastıysa
        if self.mine_board[row][col] == -1:
            self.game_over = True
            return
        
        # Mayın sayısını göster
        mine_count = self.mine_board[row][col]
        if mine_count > 0:
            self.player_board[row][col] = str(mine_count)
        else:
            self.player_board[row][col] = ' '  # Boş hücre
            
            # Eğer boş hücreyse, komşuları da aç (özyinelemeli)
            for i in range(max(0, row-1), min(self.board_size, row+2)):
                for j in range(max(0, col-1), min(self.board_size, col+2)):
                    if not (i == row and j == col):
                        self.reveal_cell(i, j)

    def toggle_flag(self, row, col):
        """Bayrak koy veya kaldır"""
        if self.player_board[row][col] == '.':
            self.player_board[row][col] = 'F'
            print(f"Bayrak koyuldu: ({row+1},{col+1})")
        elif self.player_board[row][col] == 'F':
            self.player_board[row][col] = '.'
            print(f"Bayrak kaldırıldı: ({row+1},{col+1})")
        else:
            print("Bu hücre zaten açık!")

    def check_win(self):
        """Kazanma durumunu kontrol et"""
        # Tüm güvenli hücreler açıldı mı?
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.mine_board[i][j] != -1 and self.player_board[i][j] in ['.', 'F']:
                    return False
        
        # Tüm mayınlar doğru bayraklanmış mı?
        correct_flags = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.player_board[i][j] == 'F' and self.mine_board[i][j] == -1:
                    correct_flags += 1
        
        return correct_flags == self.num_mines

    def play(self):
        """Ana oyun döngüsü"""
        while not self.game_over and not self.game_won:
            self.display_board()
            
            # Kullanıcıdan hamle al
            row, col, action = self.get_player_move()
            
            # Hamleyi işle
            if action == 'reveal':
                if self.player_board[row][col] == 'F':
                    print("Önce bayrağı kaldırın!")
                    continue
                    
                self.reveal_cell(row, col)
                self.moves += 1
                
                if self.game_over:
                    print("MAYINA BASTINIZ! OYUN BİTTİ.")
                    self.display_board(show_mines=True)
                    break
                    
            else:  # Bayrak işlemi
                self.toggle_flag(row, col)
            
            # Kazanma durumunu kontrol et
            if self.check_win():
                self.game_won = True
                print("TEBRİKLER! OYUNU KAZANDINIZ!")
                print(f"Toplam hamle: {self.moves}")
                self.display_board(show_mines=True)
                break

    # Oyunu başlat
    if __name__ == "__main__":
     while True:
        game = Minesweeper()
        game.play()
        
        play_again = input("\nTekrar oynamak ister misiniz? (e/h): ").strip().lower()
        if play_again not in ['e', 'evet', 'y', 'yes']:
            print("Oynadığınız için teşekkürler!")
            break