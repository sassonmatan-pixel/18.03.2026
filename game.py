import pygame
import random
import sys
import math

# ── Init ──────────────────────────────────────────────────────────────────────
pygame.init()
W, H = 620, 760
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("SLOT MACHINE")
clock = pygame.time.Clock()

# ── Colors ────────────────────────────────────────────────────────────────────
BG1    = (10,  0, 20)
BG2    = (26, 10, 48)
PURPLE = (155, 93, 229)
PINK   = (241, 91, 181)
YELLOW = (254, 228, 64)
CYAN   = (0, 187, 249)
RED    = (255, 77, 109)
GREEN  = (0, 230, 118)
WHITE  = (255, 255, 255)
GRAY   = (150, 150, 150)
DARK   = (13,  0, 26)

# ── Fonts ─────────────────────────────────────────────────────────────────────
font_title = pygame.font.SysFont("arial", 34, bold=True)
font_med   = pygame.font.SysFont("arial", 26, bold=True)
font_sm    = pygame.font.SysFont("arial", 20, bold=True)
font_xs    = pygame.font.SysFont("arial", 15)

# ── Symbol definitions ────────────────────────────────────────────────────────
SYMBOL_NAMES = ["Cherry", "Lemon", "Star", "Bell", "Diamond"]
RATES        = [2, 3, 9, 7, 11]
STARTING     = 50

# ── Draw symbol functions ─────────────────────────────────────────────────────
def draw_cherry(surface, cx, cy, size):
    r = max(6, size // 5)
    pygame.draw.line(surface, (34, 139, 34), (cx - r, cy - r), (cx, cy - size // 2 + 4), 3)
    pygame.draw.line(surface, (34, 139, 34), (cx + r, cy - r), (cx, cy - size // 2 + 4), 3)
    pygame.draw.circle(surface, (220, 30, 60),  (cx - r, cy), r)
    pygame.draw.circle(surface, (180,  0, 40),  (cx - r, cy), r, 1)
    pygame.draw.circle(surface, (220, 30, 60),  (cx + r, cy), r)
    pygame.draw.circle(surface, (180,  0, 40),  (cx + r, cy), r, 1)
    pygame.draw.circle(surface, (255, 150, 160),(cx - r - 2, cy - 3), max(2, r // 3))
    pygame.draw.circle(surface, (255, 150, 160),(cx + r - 2, cy - 3), max(2, r // 3))

def draw_lemon(surface, cx, cy, size):
    r = max(8, size // 3)
    color = (255, 220, 0)
    rect = pygame.Rect(cx - r, cy - int(r * 0.75), r * 2, int(r * 1.5))
    pygame.draw.ellipse(surface, color, rect)
    pygame.draw.ellipse(surface, (200, 170, 0), rect, 2)
    pygame.draw.circle(surface, color, (cx, cy - int(r * 0.75)), 5)
    pygame.draw.circle(surface, color, (cx, cy + int(r * 0.75)), 5)
    pygame.draw.ellipse(surface, (255, 255, 180),
                        pygame.Rect(cx - r // 2, cy - int(r * 0.5), r // 2, int(r * 0.4)))

def draw_star(surface, cx, cy, size):
    r_outer = max(8, size // 2 - 2)
    r_inner = max(4, r_outer // 2)
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        r = r_outer if i % 2 == 0 else r_inner
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    pygame.draw.polygon(surface, YELLOW, points)
    pygame.draw.polygon(surface, (200, 170, 0), points, 2)
    pygame.draw.circle(surface, (255, 255, 200), (cx - 3, cy - 3), max(2, r_outer // 5))

def draw_bell(surface, cx, cy, size):
    r = max(8, size // 2 - 4)
    color = (255, 200, 0)
    body = [(cx - r,     cy + r // 2),
            (cx - r + 4, cy - r // 3),
            (cx,         cy - r),
            (cx + r - 4, cy - r // 3),
            (cx + r,     cy + r // 2)]
    pygame.draw.polygon(surface, color, body)
    pygame.draw.polygon(surface, (180, 140, 0), body, 2)
    pygame.draw.rect(surface, color, (cx - r, cy + r // 2 - 3, r * 2, 8), border_radius=4)
    pygame.draw.circle(surface, (180, 130, 0), (cx, cy + r // 2 + 6), max(3, r // 5))
    pygame.draw.ellipse(surface, (255, 240, 150),
                        pygame.Rect(cx - r // 2, cy - r + 4, r // 2, max(4, r // 3)))

def draw_diamond(surface, cx, cy, size):
    r = max(8, size // 2 - 4)
    color = (100, 220, 255)
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    pygame.draw.polygon(surface, color, pts)
    pygame.draw.line(surface, (200, 240, 255), (cx, cy - r), (cx + r, cy), 1)
    pygame.draw.line(surface, (200, 240, 255), (cx, cy - r), (cx - r, cy), 1)
    pygame.draw.line(surface, (0, 150, 200),   (cx - r, cy), (cx, cy + r), 1)
    pygame.draw.line(surface, (0, 150, 200),   (cx + r, cy), (cx, cy + r), 1)
    pygame.draw.polygon(surface, (0, 150, 200), pts, 2)
    pygame.draw.polygon(surface, (220, 245, 255),
                        [(cx, cy - r), (cx + r//3, cy - r//3), (cx - r//3, cy - r//3)])

DRAW_FUNCS = [draw_cherry, draw_lemon, draw_star, draw_bell, draw_diamond]

def draw_symbol(surface, idx, cx, cy, size=60):
    DRAW_FUNCS[idx](surface, cx, cy, size)

# ── Helpers ───────────────────────────────────────────────────────────────────
def check_win(slots):
    if slots[0] == slots[1] == slots[2]:
        return "triple"
    for s in slots:
        if slots.count(s) == 2:
            return "double"
    return "lose"

def matching_idx(slots, kind):
    if kind == "triple":
        return slots[0]
    for s in slots:
        if slots.count(s) == 2:
            return s
    return None

def draw_rounded_rect(surface, color, rect, radius=14, border=0, border_color=None):
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    if border and border_color:
        pygame.draw.rect(surface, border_color, rect, border, border_radius=radius)

def draw_text_centered(surface, text, font, color, cx, cy):
    surf = font.render(text, True, color)
    surface.blit(surf, (cx - surf.get_width() // 2, cy - surf.get_height() // 2))

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# ── Particle ──────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, x, y):
        self.x = x + random.randint(-80, 80)
        self.y = y + random.randint(-40, 40)
        angle  = random.uniform(0, math.tau)
        speed  = random.uniform(2, 7)
        self.vx    = math.cos(angle) * speed
        self.vy    = math.sin(angle) * speed - 3
        self.color = random.choice([YELLOW, PINK, CYAN, GREEN, PURPLE])
        self.life  = 1.0
        self.size  = random.randint(4, 9)

    def update(self):
        self.x  += self.vx
        self.y  += self.vy
        self.vy += 0.15
        self.life -= 0.025
        return self.life > 0

    def draw(self, surface):
        c = lerp_color(self.color, BG1, 1 - self.life)
        r = max(1, int(self.size * self.life))
        pygame.draw.circle(surface, c, (int(self.x), int(self.y)), r)

# ── Button ────────────────────────────────────────────────────────────────────
class Button:
    def __init__(self, x, y, w, h, label, color=PURPLE, text_color=WHITE, radius=12):
        self.rect       = pygame.Rect(x, y, w, h)
        self.label      = label
        self.color      = color
        self.text_color = text_color
        self.radius     = radius
        self.hovered    = False
        self.disabled   = False

    def draw(self, surface):
        c = lerp_color(self.color, WHITE, 0.15) if self.hovered and not self.disabled else self.color
        if self.disabled:
            c = (60, 60, 60)
        draw_rounded_rect(surface, c, self.rect, self.radius)
        tc = self.text_color if not self.disabled else GRAY
        draw_text_centered(surface, self.label, font_sm, tc,
                           self.rect.centerx, self.rect.centery)

    def check(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and not self.disabled:
                return True
        return False

# ── Reel ──────────────────────────────────────────────────────────────────────
class Reel:
    def __init__(self, x, y):
        self.x             = x
        self.y             = y
        self.size          = 110
        self.sym_idx       = -1
        self.spinning      = False
        self.spin_timer    = 0
        self.spin_duration = 0
        self.final_idx     = 0
        self.wobble        = 0

    def start(self, final_idx, duration):
        self.final_idx     = final_idx
        self.spin_duration = duration
        self.spin_timer    = 0
        self.spinning      = True

    def update(self, dt):
        if self.spinning:
            self.spin_timer += dt
            if self.spin_timer < self.spin_duration:
                self.sym_idx = int(self.spin_timer * 12) % len(SYMBOL_NAMES)
                self.wobble  = math.sin(self.spin_timer * 22) * 5
            else:
                self.sym_idx  = self.final_idx
                self.spinning = False
                self.wobble   = 0

    def draw(self, surface, highlight=None):
        s  = self.size
        bx = self.x - s // 2
        by = self.y - s // 2 + int(self.wobble)
        draw_rounded_rect(surface, DARK, (bx, by, s, s), 14)
        border_col = YELLOW if highlight == "triple" else PURPLE if highlight == "double" else (60, 25, 90)
        draw_rounded_rect(surface, (0,0,0), (bx, by, s, s), 14, 3, border_col)
        cx, cy = self.x, self.y + int(self.wobble)
        if self.sym_idx < 0:
            draw_text_centered(surface, "?", font_title, PURPLE, cx, cy - 8)
        else:
            draw_symbol(surface, self.sym_idx, cx, cy - 8, size=70)
            lbl = font_xs.render(SYMBOL_NAMES[self.sym_idx], True, GRAY)
            surface.blit(lbl, (cx - lbl.get_width() // 2, by + s - 20))

# ── Game ──────────────────────────────────────────────────────────────────────
class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.money     = STARTING
        self.bet       = 1
        self.reels     = [Reel(145, 345), Reel(310, 345), Reel(475, 345)]
        self.spinning  = False
        self.result    = None
        self.win_amt   = 0
        self.particles = []
        self.history   = []
        self.game_over = False
        self.msg       = ""
        self.msg_color = WHITE
        self.show_rules= False
        self.tick      = 0
        self._pbet     = 1
        self.stars     = [(random.randint(0,W), random.randint(0,H),
                           random.uniform(0.3,1.0), random.uniform(0,6.28))
                          for _ in range(40)]

    def spin(self):
        if self.spinning or self.game_over:
            return
        finals = [random.randrange(len(SYMBOL_NAMES)) for _ in range(3)]
        for i, reel in enumerate(self.reels):
            reel.start(finals[i], 0.55 + i * 0.38)
        self.spinning = True
        self.result   = None
        self.msg      = ""
        self.money   -= self.bet
        self._pbet    = self.bet

    def update(self, dt):
        self.tick += dt
        for r in self.reels:
            r.update(dt)
        self.particles = [p for p in self.particles if p.update()]

        if self.spinning and not any(r.spinning for r in self.reels):
            self.spinning = False
            slots = [r.sym_idx for r in self.reels]
            kind  = check_win(slots)
            sym   = matching_idx(slots, kind)
            rate  = RATES[sym] if sym is not None else 0

            if kind == "triple":
                self.win_amt   = self._pbet * 777 * rate
                self.money    += self.win_amt
                self.result    = "triple"
                self.msg       = f"*** JACKPOT! +{self.win_amt} ***"
                self.msg_color = YELLOW
                for _ in range(70):
                    self.particles.append(Particle(W // 2, 345))
            elif kind == "double":
                self.win_amt   = self._pbet * rate
                self.money    += self.win_amt
                self.result    = "double"
                self.msg       = f"WIN!  +{self.win_amt}"
                self.msg_color = CYAN
                for _ in range(30):
                    self.particles.append(Particle(W // 2, 345))
            else:
                self.win_amt   = 0
                self.result    = "lose"
                self.msg       = f"No match  -{self._pbet}"
                self.msg_color = RED

            self.history.insert(0, (slots[:], kind, self.win_amt, self._pbet))
            self.history = self.history[:5]
            if self.money <= 0:
                self.game_over = True

    def draw_bg(self, surface):
        for row in range(0, H, 4):
            c = lerp_color(BG1, BG2, row / H)
            pygame.draw.rect(surface, c, (0, row, W, 4))
        for sx, sy, br, phase in self.stars:
            pulse = 0.5 + 0.5 * math.sin(self.tick * 1.5 + phase)
            r = max(1, int(2 * br * pulse))
            pygame.draw.circle(surface, (int(255*br*pulse),)*3, (sx, sy), r)

    def draw(self, surface):
        self.draw_bg(surface)

        # title
        tc = lerp_color(PINK, YELLOW, (math.sin(self.tick * 2) + 1) / 2)
        draw_text_centered(surface, "=== SLOT  MACHINE ===", font_title, tc, W // 2, 35)

        # balance
        draw_rounded_rect(surface, (20,0,40), (25, 75, 260, 58), 12, 2, PURPLE)
        surface.blit(font_xs.render("BALANCE", True, GRAY), (45, 82))
        surface.blit(font_sm.render(f"$ {self.money}", True, RED if self.money<=10 else YELLOW), (45,100))

        # bet
        draw_rounded_rect(surface, (20,0,40), (335, 75, 260, 58), 12, 2, PURPLE)
        surface.blit(font_xs.render("BET", True, GRAY), (355, 82))
        surface.blit(font_sm.render(f"Bet: {self.bet}", True, WHITE), (355, 100))

        # reel frame
        draw_rounded_rect(surface, (18,5,35), (20, 280, 580, 140), 18, 2, (80,40,120))
        hl = self.result if self.result in ("triple","double") else None
        for r in self.reels:
            r.draw(surface, hl)

        # result
        if self.msg:
            draw_text_centered(surface, self.msg, font_med, self.msg_color, W//2, 458)

        # particles
        for p in self.particles:
            p.draw(surface)

        # history - icon + name side by side, no overlap
        surface.blit(font_xs.render("RECENT SPINS", True, (80,80,80)), (25, 490))
        for i, (sl, kd, wa, bt) in enumerate(self.history):
            y    = 508 + i * 32
            fade = max(80, 220 - i * 35)
            draw_rounded_rect(surface, (22, 8, 42), (25, y, 490, 28), 7)
            for j, sidx in enumerate(sl):
                cell_cx = 55 + j * 110
                draw_symbol(surface, sidx, cell_cx, y + 14, size=20)
                nm = font_xs.render(SYMBOL_NAMES[sidx], True, (fade, fade, fade))
                surface.blit(nm, (cell_cx + 14, y + 7))
            amt_c = GREEN if kd != "lose" else RED
            amt_s = font_sm.render(f"+{wa}" if kd != "lose" else f"-{bt}", True, amt_c)
            surface.blit(amt_s, (450, y + 5))

        # rules
        if self.show_rules:
            draw_rounded_rect(surface, (15,5,30), (25,148,570,128), 12, 1, PURPLE)
            surface.blit(font_xs.render("Symbol rates:", True, PURPLE), (45,155))
            for idx in range(len(SYMBOL_NAMES)):
                cx = 55 + idx*110
                draw_symbol(surface, idx, cx, 185, size=30)
                lbl = font_xs.render(f"x{RATES[idx]}", True, WHITE)
                surface.blit(lbl, (cx - lbl.get_width()//2, 204))
            surface.blit(font_xs.render("2 of a kind  ->  bet x rate",       True, CYAN),   (45,224))
            surface.blit(font_xs.render("3 of a kind  ->  bet x 777 x rate", True, YELLOW), (45,242))
            surface.blit(font_xs.render("All different  ->  lose bet",        True, RED),    (45,260))

        # game over
        if self.game_over:
            ov = pygame.Surface((W, H), pygame.SRCALPHA)
            ov.fill((0,0,0,190))
            surface.blit(ov, (0,0))
            draw_text_centered(surface, "GAME  OVER",          font_title, RED,  W//2, H//2-50)
            draw_text_centered(surface, "You ran out of coins!",font_sm,   GRAY, W//2, H//2)
            draw_text_centered(surface, "Press R to restart",   font_xs,   GRAY, W//2, H//2+30)


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    game = Game()

    btn_spin    = Button(25,  668, 200, 52, "SPIN",    PURPLE)
    btn_minus   = Button(240, 668,  46, 52, "-",       (60,20,90))
    btn_plus    = Button(292, 668,  46, 52, "+",       (60,20,90))
    btn_half    = Button(346, 668,  70, 52, "1/2 BET", (40,15,70), radius=10)
    btn_max     = Button(424, 668,  60, 52, "MAX",     (40,15,70), radius=10)
    btn_rules   = Button(492, 668,  65, 52, "Rules",   (30,10,60), radius=10)
    btn_restart = Button(565, 668,  40, 52, "R",       (30,10,60), radius=10)

    buttons = [btn_spin, btn_minus, btn_plus, btn_half, btn_max, btn_rules, btn_restart]

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:             game.spin()
                if event.key == pygame.K_LEFT:              game.bet = max(1, game.bet - 1)
                if event.key == pygame.K_RIGHT:             game.bet = min(game.money, game.bet + 1)
                if event.key == pygame.K_r:                 game.reset()

            for btn in buttons:
                if btn.check(event):
                    if   btn is btn_spin:    game.spin()
                    elif btn is btn_minus:   game.bet = max(1, game.bet - 1)
                    elif btn is btn_plus:    game.bet = min(game.money, game.bet + 1)
                    elif btn is btn_half:    game.bet = max(1, game.money // 2)
                    elif btn is btn_max:     game.bet = game.money
                    elif btn is btn_rules:   game.show_rules = not game.show_rules
                    elif btn is btn_restart: game.reset()

        btn_spin.disabled  = game.spinning or game.game_over
        btn_minus.disabled = game.spinning or game.bet <= 1
        btn_plus.disabled  = game.spinning or game.bet >= game.money
        btn_half.disabled  = game.spinning
        btn_max.disabled   = game.spinning

        game.update(dt)
        game.draw(screen)
        for btn in buttons:
            btn.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
