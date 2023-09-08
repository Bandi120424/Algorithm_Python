def convert_time_to_minute(_time):
    hour, minute = map(int, _time.split(":"))
    return hour*60+minute

#새로 시작하는 과제에 우선순위 
def solution(plans):
    completed_task = []
    ordered_plans = sorted([(name, convert_time_to_minute(start), duration) 
                     for name, start, duration in plans], key = lambda x:x[1])
    
    queue = [] #해결하지 못한 과제들 
    left_time = 0 #다음 과제가 시작하기까지 남은 시간 
    
    for i in range(len(plans)):
        subj, start, duration = ordered_plans[i]
        duration = int(duration)
        
        while queue:
            pre_subj, pre_duration = queue.pop()
            if left_time >= pre_duration: #과제를 끝낼 수 있는 경우 
                left_time -= pre_duration 
                completed_task.append(pre_subj)
            else:
                queue.append((pre_subj, pre_duration - left_time))
                break 
    
        queue.append((subj, duration))
        
        if i < len(plans)-1:
            next_start = ordered_plans[i+1][1]
            left_time = next_start - start
            
    while queue:
        subj, _ = queue.pop()
        completed_task.append(subj)
                
    return completed_task