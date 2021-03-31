#!/usr/bin/env python
# coding: utf-8
class fuzzy():
    def __init__(self):
        self.Front = ''
        self.Left = ''
        self.Right = ''
    
    def system(self, F, L, R):
        self.setFront(F)
        self.setLeft(L)
        self.setRight(R)
        return self.returnWheel()
        
    def setFront(self, dist_F):
        if dist_F >= 0 and dist_F < 5:
            fs = 1
        elif dist_F < 10:
            fs = (10 - dist_F)/5
        else:
            fs = 0
            
        if dist_F >= 10 and dist_F < 12:
            fm = (dist_F - 10)/2
        elif dist_F >= 12 and dist_F <= 14:
            fm = 1
        elif dist_F > 14 and dist_F <= 18:  
            fm = (18 - dist_F)/4
        else:
            fm = 0
            
        if dist_F >= 20:
            fl = 1
        else:
            fl = 0
        
        self.Front = self.set_rules(fs, fm, fl)
        
    def setLeft(self, dist_L):
        if dist_L >= 0 and dist_L <= 5:
            ls = 1
        elif dist_L <= 8:
            ls = (8-dist_L)/3
        else:
            ls = 0
            
        if dist_L >= 6 and dist_L <= 8:
            lm = (dist_L-6)/2
        elif dist_L > 8 and dist_L <=10:
            lm = 1
        elif dist_L > 10 and dist_L <= 12:
            lm = (12-dist_L)/2
        else:
            lm = 0
            
        if dist_L >= 12 and dist_L < 14:
            ll = (dist_L-12)/2
        elif dist_L >= 14:
            ll = 1
        else:
            ll = 0
        
        self.Left = self.set_rules(ls, lm, ll)
        
    def setRight(self, dist_R):
        if dist_R >= 0 and dist_R <= 5:
            rs = 1
        elif dist_R <= 8:
            rs = (8 - dist_R)/3
        else:
            rs = 0
            
        if dist_R >= 6 and dist_R <= 8:
            rm = (dist_R - 6)/2
        elif dist_R > 8 and dist_R <=10:
            rm = 1
        elif dist_R > 10 and dist_R <= 12:
            rm = (12 - dist_R)/2
        else:
            rm = 0
            
        if dist_R >= 12 and dist_R < 14:
            rl = (dist_R - 12)/2
        elif dist_R >= 14:
            rl = 1
        else:
            rl = 0
            
        self.Right = self.set_rules(rs, rm, rl)
        
    def set_rules(self, s, m, l):
        M = max(s, m, l)
        if(s == M):
            return 'SMALL'
        elif(m == M):
            return 'MEDIUM'
        else:
            return 'LARGE'
        
    def returnWheel(self):
        if self.Left == 'SMALL':
            return 40
        if self.Right == 'SMALL':
            return -40
        if self.Left == 'MEDIUM' and self.Right == 'MEDIUM':
            return 0
        if self.Left == 'MEDIUM' and self.Front == 'SMALL':
            return 30
        if self.Right == 'MEDIUM' and self.Front == 'SMALL':
            return -30
        if self.Front == 'LARGE':
            return 0
        return 0

