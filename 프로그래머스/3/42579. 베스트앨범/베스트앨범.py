def solution(genre_array, play_array):
    # 우선순위 정렬
    genre = {}
    for i in range(len(genre_array)):
        if not genre.get(genre_array[i]):
            genre[genre_array[i]] = play_array[i]
        else:
            genre[genre_array[i]] += play_array[i]

    genre_sorted_array = sorted(genre.items(), key=lambda item:item[1], reverse=True)

    # key(장르) : value((고유번호, 횟수))
    album = {}
    for i in range(len(genre_sorted_array)):
        album[genre_sorted_array[i][0]] = []

    for i in range(len(genre_array)):
            album[genre_array[i]].append((i, play_array[i]))

    for key in album.keys():
        album[key] = sorted(album.get(key), key = lambda x:x[1], reverse=True)

    result = []

    for key in album.keys():
        if len(album.get(key)) == 1:
            result.append(album.get(key)[0][0])

        else:
            result.append(album.get(key)[0][0])
            result.append(album.get(key)[1][0])


    return result