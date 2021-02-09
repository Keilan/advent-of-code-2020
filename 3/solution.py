import sys

def toboggan_path():
    # Read in the tree map, top-left being 0,0, note that y comes first
    tree_map = sys.stdin.read().splitlines()
    pattern_height = len(tree_map)
    pattern_width = len(tree_map[0])

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    # Iterate through the pattern until we reach the end
    multiplied_result = 1
    for right, down in slopes:
        x, y = 0, 0
        tree_count = 0
        while y < pattern_height:
            # Check for tree
            if tree_map[y][x] == '#':
                tree_count += 1

            # Move to next position, using % to account for repeating width
            x = (x + right) % pattern_width
            y += down
        
        print(f'You will encounter {tree_count} trees when moving '
            f'right {right}, down {down}.')
        multiplied_result *= tree_count
    
    print(f'Each answer multiplied is {multiplied_result}')

if __name__ == '__main__':
    toboggan_path()