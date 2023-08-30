class Players():
    def __init__(self, players=None):
        if players==None:
            raise Exception("There is no players")
        self.players = players
        self.rank = {player: i for (i, player) in enumerate(players)}
        
    def swap(self, name: str=""):
        idx = self.rank[name]
        self.rank[name] -= 1
        self.rank[self.players[idx-1]] += 1
        self.players[idx-1], self.players[idx] = self.players[idx], self.players[idx-1]

    def update_rank(self, callings=None):
        if callings == None:
            raise Exception("There is no callings")
        for name in callings:
            self.swap(name)
        return self.players

def solution(players, callings):
    player_info = Players(players) 
    return player_info.update_rank(callings)
