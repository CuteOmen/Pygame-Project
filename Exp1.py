import pygame
pygame.init()

# Display
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first Game")

# Character
x = 220
y = 230
width = 60
height = 40
vel = 5
isJump = False
jumpCounter = 10

# Main Loop
running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
    
    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_a] and x > vel:
        x -= vel
    if Keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
    if not(isJump):
        if Keys[pygame.K_w] and y > vel: 
            y -= vel    
        if Keys[pygame.K_s] and y < 500 - height - vel:
            y += vel
        if Keys[pygame.K_SPACE]and y > vel:
            isJump = True
    else:
        neg = 1
        if jumpCounter >= -10:
            if jumpCounter < 0:
                neg = -1
            y -= (jumpCounter**2) * 0.5 * neg
            jumpCounter -= 1
        else:
            isJump = False
            jumpCounter = 10
        
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()
pygame.quit()