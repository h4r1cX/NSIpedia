class pykemon:

    def __init__(self, t, p, c, n, a, s, h):
        self.type = t
        self.pvb = p
        self.pvc = c
        self.nom = n
        self.atk = a
        self.spd = s
        self.heal = h

    def attack(self, adv): 
        print(f"{self.nom} attaque {adv.nom} avec {self.atk}")
        adv.pv -= self.atk
        
    def heal(self, adv):
            b = 1
            m = 2
            o = 3
            r = 2
            if self.type["type"] == "feu":
                self.pvc += self.heal
                if self.pvc > self.pvb:
                     self.pvc = self.pvb
                o -=1
            elif self.type["type"] == "plante":
                 self.atk += self.heal
                 b -= 1
            elif self.type["type"] == "eau":
                adv.atk / 2 #pour un seul tour (à coder)
                m -= 1
            elif self.type["type"] == "normal":
                 ##le pokémon adverse ne peut pas attaquer pendant ce tour
                 r -= 1          

    def weakness(self, adv):
        ##à coder les faiblesses en fonction du type du pokémon

    
    def __repr__(self, adv): 
        return f"{self.nom}: {self.pvc} // {adv.nom}: {adv.pvc}"
