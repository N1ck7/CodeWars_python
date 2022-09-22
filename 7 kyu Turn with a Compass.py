def direction(facing, turn):
    dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45
    start_idx = dir.index(facing)
    end_idx = (start_idx + turns) % len(dir)
    return dir[end_idx]
