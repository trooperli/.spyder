class pingPong:
    


    def __init__(self, rankingScores, result):
        self.rankingScores = rankingScores
        self.result = result
        
    def calculate(self):
        if len(self.rankingScores) == 2:
            rs = self.single_play(self.rankingScores,self.result)
#        elif len(self.rankingScores) == 4:
#            rs = self.double_play(self.rankingScores,self.result)
        else:
            raise Exception('Invalid number of players!')
        
        self.rankingScores = rs
            
    @staticmethod    
    def single_play(rs,r):
        if abs(rs[0]-rs[1]) >= 0 and abs(rs[0]-rs[1]) <1:
            if r[0] > r[1]:
                rs[0] = rs[0]+10
                rs[1] = rs[1]-5
            elif r[0] < r[1]:
                rs[0] = rs[0]-5
                rs[1] = rs[1]+10
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 1 and abs(rs[0]-rs[1]) <26:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+9
                    rs[1] = rs[1]-4.5
                else:
                    rs[0] = rs[0]+11
                    rs[1] = rs[1]-5.5
               
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-5.5
                    rs[1] = rs[1]+11
                else:
                    rs[0] = rs[0]-4.5
                    rs[1] = rs[1]+9
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 26 and abs(rs[0]-rs[1]) <51:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+8
                    rs[1] = rs[1]-4
                else:
                    rs[0] = rs[0]+12
                    rs[1] = rs[1]-6
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-6
                    rs[1] = rs[1]+12
                else:
                    rs[0] = rs[0]-4
                    rs[1] = rs[1]+8
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 51 and abs(rs[0]-rs[1]) <101:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+7
                    rs[1] = rs[1]-3.5
                else:
                    rs[0] = rs[0]+14
                    rs[1] = rs[1]-7
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-7
                    rs[1] = rs[1]+14
                else:
                    rs[0] = rs[0]-3.5
                    rs[1] = rs[1]+7
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 101 and abs(rs[0]-rs[1]) <151:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+6
                    rs[1] = rs[1]-3
                else:
                    rs[0] = rs[0]+16
                    rs[1] = rs[1]-8
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-8
                    rs[1] = rs[1]+16
                else:
                    rs[0] = rs[0]-3
                    rs[1] = rs[1]+6
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 151 and abs(rs[0]-rs[1]) <201:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+5
                    rs[1] = rs[1]-2.5
                else:
                    rs[0] = rs[0]+20
                    rs[1] = rs[1]-10
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-10
                    rs[1] = rs[1]+20
                else:
                    rs[0] = rs[0]-2.5
                    rs[1] = rs[1]+5
            else:
                raise Exception('Game is a game, no even game is allowed!') 
        elif abs(rs[0]-rs[1]) >= 201 and abs(rs[0]-rs[1]) <301:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+4
                    rs[1] = rs[1]-2
                else:
                    rs[0] = rs[0]+24
                    rs[1] = rs[1]-12
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-12
                    rs[1] = rs[1]+24
                else:
                    rs[0] = rs[0]-2
                    rs[1] = rs[1]+4
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 301 and abs(rs[0]-rs[1]) <401:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+3
                    rs[1] = rs[1]-1.5
                else:
                    rs[0] = rs[0]+28
                    rs[1] = rs[1]-14
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-14
                    rs[1] = rs[1]+28
                else:
                    rs[0] = rs[0]-1.5
                    rs[1] = rs[1]+3
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 401 and abs(rs[0]-rs[1]) <501:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+2
                    rs[1] = rs[1]-1
                else:
                    rs[0] = rs[0]+32
                    rs[1] = rs[1]-16
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-16
                    rs[1] = rs[1]+32
                else:
                    rs[0] = rs[0]-1
                    rs[1] = rs[1]+2
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >= 501 and abs(rs[0]-rs[1]) <751:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]+1
                    rs[1] = rs[1]-0.5
                else:
                    rs[0] = rs[0]+36
                    rs[1] = rs[1]-18
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-18
                    rs[1] = rs[1]+36
                else:
                    rs[0] = rs[0]-0.5
                    rs[1] = rs[1]+1
            else:
                raise Exception('Game is a game, no even game is allowed!')
        elif abs(rs[0]-rs[1]) >=751:
            if r[0] > r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]
                    rs[1] = rs[1]
                else:
                    rs[0] = rs[0]+40
                    rs[1] = rs[1]-20
            elif r[0] < r[1]:
                if rs[0] > rs[1]:
                    rs[0] = rs[0]-20
                    rs[1] = rs[1]+40
                else:
                    rs[0] = rs[0]
                    rs[1] = rs[1]
            else:
                raise Exception('Game is a game, no even game is allowed!')
        
         
        return rs
        
        

            
   
            
            
            
        
        

