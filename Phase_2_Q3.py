import time
import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect.",
        "To be or not to be, that is the question.",
        "In the beginning, God created the heavens and the earth."
        # Add more sentences as needed
    ]
    return random.choice(sentences)

def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def calculate_typing_speed(start_time, end_time, typed_words):
    total_time_seconds = end_time - start_time
    words_per_minute = (typed_words / total_time_seconds) * 60
    return words_per_minute

def typing_speed_test():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Typing Speed Tester")
    
    clock = pygame.time.Clock()

    print("Welcome to the Typing Speed Tester!")
    input("Press Enter when you are ready to start...")

    sentence = get_random_sentence()
    print(f"\nType the following sentence:\n\n{sentence}\n")

    start_time = time.time()
    user_input = ""
    while True:
        screen.fill(WHITE)
        draw_text(screen, "Type the following sentence:", 36, BLACK, 50, 50)
        draw_text(screen, sentence, 28, BLACK, 50, 100)
        draw_text(screen, "Your typing:", 36, BLACK, 50, 300)
        draw_text(screen, user_input, 28, BLACK, 50, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end_time = time.time()
                    typed_words = len(user_input.split())
                    typing_speed = calculate_typing_speed(start_time, end_time, typed_words)

                    # Display the result in the graphical window
                    draw_text(screen, f"Your typing speed: {typing_speed:.2f} WPM", 36, BLACK, 50, 400)
                    accuracy = (typed_words / len(sentence.split())) * 100
                    draw_text(screen, f"Accuracy: {accuracy:.2f}%", 36, BLACK, 50, 450)
                    pygame.display.flip()
                    pygame.time.wait(300000)  # Wait for 3 seconds before quitting
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    typing_speed_test()

