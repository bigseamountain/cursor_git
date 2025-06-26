import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 游戏设置
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
CELL_NUMBER_X = WINDOW_WIDTH // CELL_SIZE
CELL_NUMBER_Y = WINDOW_HEIGHT // CELL_SIZE

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(10, 15), (9, 15), (8, 15)]  # 初始蛇身
        self.direction = RIGHT
        self.new_block = False
        
    def draw_snake(self, screen):
        """绘制蛇身"""
        for block in self.body:
            x_pos = int(block[0] * CELL_SIZE)
            y_pos = int(block[1] * CELL_SIZE)
            rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            
    def move_snake(self):
        """移动蛇"""
        if self.new_block:
            # 如果吃到食物，不删除尾巴
            body_copy = self.body[:]
            self.new_block = False
        else:
            # 正常移动，删除尾巴
            body_copy = self.body[:-1]
        
        # 计算新的头部位置
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        body_copy.insert(0, new_head)
        self.body = body_copy[:]
        
    def add_block(self):
        """增加身体长度"""
        self.new_block = True
        
    def check_collision(self):
        """检查碰撞"""
        # 检查撞墙
        head = self.body[0]
        if (head[0] < 0 or head[0] >= CELL_NUMBER_X or 
            head[1] < 0 or head[1] >= CELL_NUMBER_Y):
            return True
            
        # 检查撞到自己
        for block in self.body[1:]:
            if head == block:
                return True
                
        return False

class Food:
    def __init__(self):
        self.randomize()
        
    def draw_food(self, screen):
        """绘制食物"""
        food_rect = pygame.Rect(int(self.pos[0] * CELL_SIZE), 
                               int(self.pos[1] * CELL_SIZE), 
                               CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
        
    def randomize(self):
        """随机生成食物位置"""
        self.x = random.randint(0, CELL_NUMBER_X - 1)
        self.y = random.randint(0, CELL_NUMBER_Y - 1)
        self.pos = (self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        
    def update(self):
        """更新游戏状态"""
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self, screen):
        """绘制游戏元素"""
        screen.fill(BLACK)
        self.food.draw_food(screen)
        self.snake.draw_snake(screen)
        self.draw_score(screen)
        
    def check_collision(self):
        """检查蛇是否吃到食物"""
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.score += 1
            
            # 确保食物不在蛇身上
            for block in self.snake.body[1:]:
                if block == self.food.pos:
                    self.food.randomize()
                    
    def check_fail(self):
        """检查游戏是否结束"""
        if self.snake.check_collision():
            self.game_over()
            
    def game_over(self):
        """游戏结束"""
        print(f"游戏结束！最终得分: {self.score}")
        pygame.quit()
        sys.exit()
        
    def draw_score(self, screen):
        """绘制分数"""
        score_text = self.font.render(f"得分: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

def main():
    """主函数"""
    # 创建游戏窗口
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("贪吃蛇游戏")
    clock = pygame.time.Clock()
    
    # 创建游戏实例
    game = Game()
    
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # 控制蛇的移动方向
                if event.key == pygame.K_UP and game.snake.direction != DOWN:
                    game.snake.direction = UP
                elif event.key == pygame.K_DOWN and game.snake.direction != UP:
                    game.snake.direction = DOWN
                elif event.key == pygame.K_RIGHT and game.snake.direction != LEFT:
                    game.snake.direction = RIGHT
                elif event.key == pygame.K_LEFT and game.snake.direction != RIGHT:
                    game.snake.direction = LEFT
        
        # 更新游戏
        game.update()
        
        # 绘制游戏
        game.draw_elements(screen)
        
        # 刷新显示
        pygame.display.update()
        clock.tick(10)  # 控制游戏速度

if __name__ == "__main__":
    main() 