import pygame
import random
import numpy as np
def main():
    # Kích thước cửa sổ và độ dày của đường
    WINDOW_WIDTH = 1024
    WINDOW_HEIGHT = 512
    CELL_SIZE = 50
    PADDING = 30  # Khoảng cách giữa các ô vuông
    LINE_WIDTH = 3
    CHARACTER_IMAGE_PATH = 'crusaders-axolotl-master/img/character_for_map/star.png'

    # Màu sắc
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Dữ liệu bản đồ
    HEIGHT = random.randint(3, 6)
    WIDTH = random.randint(3, 5)
    # make array from width and height
    map = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for h in range(HEIGHT):

        for w in range(WIDTH):
            if random.getrandbits(1):
                map[h][w] = 'X'

        if set(map[h]) == {' '}:
            for _ in range(random.randint(1, WIDTH)):
                map[h][random.randint(0, WIDTH-1)] = 'X'

    # In bản đồ
    # for row in map:
    #     print(' '.join(row))

    new_row = [' ' for _ in range(WIDTH)]
    mid_index = WIDTH // 2
    new_row[mid_index] = 'X'

    # Append the new row to the map
    map.append(new_row)
    H = len(map)
    print(map)
    arr = np.empty((H, 0)).tolist()
    # In ra danh sách hai chiều

    for h in range(H):
        for w in range(len(map[1])):
            if map[h][w] == 'X':
                arr[h].append((h, w))  # Thêm tọa độ (h, w) vào danh sách

    # In ra danh sách các tọa độ có giá trị 'X'
    print("toa do cua cac o co gia tri X:")
    for coord in arr:
        print(coord)

    arr_for_connect = []

    # Khởi tạo danh sách các địa điểm X
    X_positions = [(h, w) for h in range(len(map))
                for w in range(WIDTH) if map[h][w] == 'X']

    # Tạo danh sách các đường nối
    arr_for_connect = []


    # for i in range(len(map) - 1, -1, -1):
    #     print(i)
    #     if 'X' in map[i]:
    #         # Tìm vị trí của 'X' trong hàng
    #         index = map[i].index('X')
    #         print(f"Toạ độ của 'X' dưới cùng là: ({i}, {index})")
    #         break
    # Duyệt qua từng địa điểm X
    # nối max 3 đường, ô được nối 3 dường, min 1, ko nối chéo đường
    # for i in range(HEIGHT-1, 0, -1):
    #     print(f"ở hàng {i}")

    #     # # Chọn ngẫu nhiên một cặp toạ độ từ hàng tiếp theo
    #     # next_row_coord = random.choice(arr[i-1])
    #     if i == len(map)-1: # Vị trí đầu tiên két nối hết với 1 hàng đằng sau
    #         index = map[len(map)-1].index('X')
    #         arr_for_connect.append([(i, index), arr[i-1]])
    #     else:
    #         unconnected_points = map[i-1].copy()
    #         print(unconnected_points)
    #         print("-----------------------------")
    #         for j in range(len(map[i])):
    #             if map[i][j] == 'X':
                    
    #                 print('----')
    #                 print("vị trí", i,j)
    #                 # Chọn ngẫu nhiên một số lượng mẫu trong hàng tiếp theo
    #                 num_samples = random.randint(1, len(unconnected_points))
    #                 print("len", len(unconnected_points))
    #                 print("mẫu", num_samples)

    #                 arr_for_connect.append([(i, j), arr[i-1][:num_samples]])

    #                 # for point in arr[i-1][:num_samples]:
    #                 print(f"đã xoá {unconnected_points[:num_samples]} trong danh sách")
    #                 del unconnected_points[:num_samples]

    # ngon                 
    # for i in range(HEIGHT - 1, 0, -1):
    #     print(f"ở hàng {i}")

    #     if i == len(map) - 1:  # Vị trí đầu tiên kết nối hết với 1 hàng đằng sau
    #         index = map[len(map) - 1].index('X')
    #         arr_for_connect.append([(i, index), arr[i - 1]])
    #     else:
    #         unconnected_points = map[i - 1].copy()
    #         print(unconnected_points)
    #         print("-----------------------------")
    #         for j in range(len(map[i])):
    #             if map[i][j] == 'X':
    #                 print('----')
    #                 print("vị trí", i, j)
    #                 # Chọn số lượng mẫu là số lượng điểm kết nối
    #                 if unconnected_points:  # Kiểm tra xem danh sách không rỗng
    #                     num_samples = random.randint(1, len(unconnected_points))
    #                 else:
    #                     num_samples = 1

    #                 print("len", len(unconnected_points))
    #                 print("mẫu", num_samples)

    #                 if not unconnected_points:  # Nếu danh sách rỗng
    #                     last_point = arr[i - 1][-1]  # Lấy điểm cuối cùng của hàng trên cùng
    #                     arr_for_connect.append([(i, j), [last_point]])
    #                 else:  # Nếu danh sách không rỗng
    #                     arr_for_connect.append([(i, j), arr[i - 1][:num_samples]])
    #                     print("kết nối đến mẫu:", arr[i - 1][:num_samples])
    #                     unconnected_points = []


    for i in range(len(map) - 1, 0, -1):
        print(f"in row {i}")

        if i == len(map) - 1:  # Vị trí đầu tiên kết nối hết với 1 hàng đằng sau
            index = map[len(map) - 1].index('X')
            arr_for_connect.append([(i, index), arr[i - 1]])
        else:
            unconnected_points = [(i - 1, idx) for idx, val in enumerate(map[i - 1]) if val == 'X']  # Danh sách các điểm chưa được kết nối
            print(unconnected_points)
            print("-----------------------------")
            for j in range(len(map[i])):
                if map[i][j] == 'X':
                    print('----')
                    print("position:", i, j)
                    # Chọn số lượng mẫu là số lượng điểm kết nối
                    if unconnected_points:  # Kiểm tra xem danh sách không rỗng
                        num_samples = min(len(unconnected_points), random.randint(1, len(unconnected_points)))  # Đảm bảo số lượng mẫu không vượt quá số lượng điểm chưa được kết nối
                    else:
                        num_samples = 1

                    print("len", len(unconnected_points))
                    print("mau", num_samples)

                    if not unconnected_points:  # Nếu danh sách rỗng
                        last_point = arr[i - 1][-1]  # Lấy điểm cuối cùng của hàng trên cùng
                        arr_for_connect.append([(i, j), [last_point]])
                    else:  # Nếu danh sách không rỗng
                        samples = unconnected_points[:num_samples]  # Chọn mẫu theo thứ tự từ trái sang phải
                        arr_for_connect.append([(i, j), samples])
                        print("ket noi den mau:", samples)
                        unconnected_points = unconnected_points[num_samples:]  # Loại bỏ các mẫu đã được kết nối khỏi danh sách



    # print(arr_for_connect)


    # In ra danh sách các đường nối
    for pair in arr_for_connect:
        print(pair)


    # for i in range(len(arr_for_connect)):
    #     print(arr_for_connect[i])


    def load_character_image():
        character_image = pygame.image.load(CHARACTER_IMAGE_PATH)
        character_image = pygame.transform.scale(
            character_image, (CELL_SIZE, CELL_SIZE))
        return character_image

    # Lớp nhân vật


    class Character:
        def __init__(self, x, y):
            self.image = load_character_image()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def move_to(self, x, y):
            self.rect.x = x
            self.rect.y = y

        def draw(self, surface):
            surface.blit(self.image, self.rect)


    # Khởi tạo Pygame
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Connected Points")

    # Hàm vẽ bản đồ
    def draw_map(map_data):
        for y, row in enumerate(map_data):
            for x, cell in enumerate(row):
                if cell == 'X':
                    color = BLACK
                else:
                    color = WHITE
                rect = pygame.Rect(x * (CELL_SIZE + PADDING),
                                y * (CELL_SIZE + PADDING), CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, color, rect)

    # Hàm vẽ đường nối
    def draw_lines(arr_for_connect):
        for pair in arr_for_connect:
            start_point = pair[0]
            for end_point in pair[1]:
                start_x = start_point[1] * (CELL_SIZE + PADDING) + CELL_SIZE // 2
                start_y = start_point[0] * (CELL_SIZE + PADDING) + CELL_SIZE // 2
                end_x = end_point[1] * (CELL_SIZE + PADDING) + CELL_SIZE // 2
                end_y = end_point[0] * (CELL_SIZE + PADDING) + CELL_SIZE // 2
                pygame.draw.line(window, RED, (start_x, start_y),
                                (end_x, end_y), LINE_WIDTH)


    # Tạo đối tượng nhân vật
    for x in range(WIDTH):
        if map[len(map) - 1][x] == 'X':
            start_x = x
            start_y = len(map) - 1
            break

    # Tạo đối tượng nhân vật
    character = Character(start_x * (CELL_SIZE + PADDING),
                        start_y * (CELL_SIZE + PADDING))

    # Vòng lặp chính
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Kiểm tra nếu người chơi bấm chuột
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Tìm ô vuông mà người chơi bấm vào
                clicked_x = mouse_x // (CELL_SIZE + PADDING)
                clicked_y = mouse_y // (CELL_SIZE + PADDING)
                # Kiểm tra xem ô vuông mà người chơi bấm vào có kết nối với vị trí hiện tại của nhân vật hay không
                for pair in arr_for_connect:
                    start_point = pair[0]
                    connections = pair[1]
                    if start_point == (character.rect.y // (CELL_SIZE + PADDING), character.rect.x // (CELL_SIZE + PADDING)):
                        for end_point in connections:
                            if end_point == (clicked_y, clicked_x):
                                character.move_to(
                                    clicked_x * (CELL_SIZE + PADDING), clicked_y * (CELL_SIZE + PADDING))
                                break

        # Xóa màn hình
        window.fill(WHITE)

        # Vẽ bản đồ và đường nối
        draw_map(map)
        draw_lines(arr_for_connect)

        # Vẽ nhân vật
        character.draw(window)

        # Cập nhật màn hình
        pygame.display.flip()

    # Kết thúc Pygame
    pygame.quit()

if __name__ == "__main__":
    main()