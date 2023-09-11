class Mine():
    def __init__(self, picks, minerals) -> None:
        self.FATIQUE_TABLE = [[1, 1, 1], [5, 1, 1], [25, 5, 1]] #다이아, 철, 돌
        self.LIMIT = 5 #하나의 곡괭이는 최대 5번 사용
        self.MINERAL_TYPE = {"diamond":0, "iron":1, "stone":2}
        self.picks = picks             
        self.total_minerals = len(minerals) 
        self.minerals = minerals


    def minimum_fatique(self):
        #self.minerals를 다섯개 단위로 나누어서 각 단위에서 어떤 곡괭이를 사용할 것인지 선정 -> 5개 단위로 산정할 시, 오류
        #다섯개 단위로 하되, 전체적으로 본 후 곡괭이를 분배해야함 
        MINIERAL_NAME = ["diamond", "iron", "stone"]
        minerals_by_parts = []
        fatigue = 0
        for i in range(min(5*sum(self.picks), self.total_minerals)):
            if i%self.LIMIT == 0:
                part = {"diamond":0, "iron": 0, "stone":0}
            part[self.minerals[i]] += 1
            
            if i%self.LIMIT == 4 or i == self.total_minerals-1:
                minerals_by_parts.append([part["diamond"], part["iron"], part["stone"]])
                
        return self.pick_mandrel(minerals_by_parts)
    
    def pick_mandrel(self, minerals_by_parts):
        fatigue = 0 
        minerals_by_parts.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)
        for dia, iron, stone in minerals_by_parts:
            for i in range(3):
                if self.picks[i]:
                    self.picks[i] -= 1
                    fatigue += dia * self.FATIQUE_TABLE[i][0] + iron * self.FATIQUE_TABLE[i][1] + stone * self.FATIQUE_TABLE[i][2]
                    break
        return fatigue

def solution(picks, minerals):    
    mind_info = Mine(picks, minerals)
    return mind_info.minimum_fatique()
        