# Deklarasi karakter
define Pangeran = Character("MC")
define c1 = Character("Harem 1")
define c2 = Character("Harem 2")
define c3 = Character("Harem 3")
define Pemburu = Character("Pemburu")
define Pemburu2 = Character("Pemburu2")
define Raja = Character("Raja")
define Ratu = Character("Ratu")
define Pengawal = Character("Pengawal")


# Game dimulai
label start:

    $ player_max_hp = 10
    $ player_hp = player_max_hp

    $ er_max_hp = 6
    $ enemy_hp = er_max_hp

    while player_hp > 0 :
        menu :
        "Attack":
            $ enemy_hp -=2
            if enemy_hp <=0:
            "Anjay Menang"
            jump simple_end
    
        "Dont Attack":
            "Kamu jelek"
    
        $ player_hp = 2
        "Aduh sakit darah [player_hp] ngurang!"

    "You died"



    # This ends the game.
    return