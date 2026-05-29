def solution(genre_array, play_array):

    _dict = {}
    songs = {}
    result = []
    
    for i in range(len(genre_array)):
        _dict[genre_array[i]] = _dict.get(genre_array[i], 0) + play_array[i]
    
    sorted_dict = sorted(_dict, key = lambda x : _dict[x], reverse=True)
  
    for genre in sorted_dict:
        songs[genre] = []
        
    for i in range(len(genre_array)):
        songs[genre_array[i]].append((i, play_array[i]))
        
    for value in songs.values():
        value.sort(key = lambda x : (x[1], -x[0]), reverse = True)
    
    for genre in sorted_dict:
        if len(songs[genre]) == 1:
            result.append(songs[genre][0][0])
        else:
            result.append(songs[genre][0][0])
            result.append(songs[genre][1][0])
    
    return result

    