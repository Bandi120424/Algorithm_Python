from itertools import combinations

def init_data(places: list = None):
    places_arr = [[[p for p in row] for row in room] for room in places]
    return places_arr

def find_applicants(room: list = None):
    height = width = len(room)
    applicants_pos = []
    
    for i in range(height):
        for j in range(width):
            if room[i][j] == 'P':
                applicants_pos.append([i, j])
    
    return applicants_pos
            
def manhatton_distance(pos1: list = None, pos2: list = None):
    r1, c1 = pos1
    r2, c2 = pos2
    d = abs(r1-r2) + abs(c1-c2)
    return d

def distance_check(pos1: None, pos2: None, room: None):
    r1, c1 = pos1
    r2, c2 = pos2
    distance = manhatton_distance(pos1, pos2)

    if distance > 2:
            return True
    
    if distance == 1:
        if r1 == r2 or c1 == c2:
            return False
	
    for i in range(min(r1, r2), max(r1, r2)+1):
        for j in range(min(c1, c2), max(c1, c2)+1):
            if ([i, j] == pos1) or ([i, j] == pos2):
                continue
            if room[i][j] == 'O':
                return False
            
    return True
            
def room_check(room: list = None):
    
    applicants_pos = find_applicants(room)

    for pos1, pos2 in combinations(applicants_pos, 2):
        if pos1 == pos2:
            continue
        if not distance_check(pos1, pos2, room):
            return 0
    return 1
    
def solution(places):
    answer = []
    place_arr = init_data(places)
    
    for room in place_arr:
        answer.append(room_check(room))
                     
    return answer
