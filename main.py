@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_a_pressed():
    global darts, projectile
    darts = [assets.image("""
            Dart1
        """),
        assets.image("""
            Dart2
        """),
        img("""
            . . 1 1 . . 
                    . . 1 1 . . 
                    5 1 1 1 1 5 
                    5 5 5 5 5 5 
                    . . 5 5 . . 
                    . 5 . . 5 .
        """),
        img("""
            . . 1 1 . . 
                    . . 1 1 . . 
                    7 1 1 1 1 7 
                    7 7 7 7 7 7 
                    . . 7 7 . . 
                    . 7 . . 7 .
        """),
        img("""
            . . 1 1 . . 
                    . . 1 1 . . 
                    9 1 1 1 1 9 
                    9 9 9 9 9 9 
                    . . 9 9 . . 
                    . 9 . . 9 .
        """),
        img("""
            . . 1 1 . . 
                    . . 1 1 . . 
                    a 1 1 1 1 a 
                    a a a a a a 
                    . . a a . . 
                    . a . . a .
        """)]
    projectile = sprites.create_projectile_from_sprite(darts._pick_random(), mySprite, 0, -150)
    projectile.start_effect(effects.warm_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global enemySpeed
    sprite.destroy(effects.disintegrate, 500)
    otherSprite.destroy()
    info.change_score_by(1)
    if info.score() == 5:
        game.show_long_text("Ship Intercom: We forgot to tell you, your projectiles steal data from the ships before destroying them. And also, please don't get hit too many times, these ships are really expensive.",
            DialogLayout.BOTTOM)
    if info.score() == 10:
        info.change_score_by(5)
        mySprite.say_text("+5 Level-Up Bonus", 2000, False)
        statusbar2.value = 100
        enemySpeed = 70
    elif info.score() == 25:
        info.change_score_by(5)
        mySprite.say_text("+5 Level-Up Bonus", 2000, False)
        statusbar2.value = 100
        enemySpeed = 90
    elif info.score() == 40:
        game.show_long_text("Congrats soldier, you saved the galaxy. Accept this reward of $700,000,000!",
            DialogLayout.BOTTOM)
        info.change_score_by(700000000)
        game.over(True)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_zero(status):
    game.show_long_text("Ship Intercom: Come in soldier... soldier? I TOLD HIM THESE ARE EXPENSIVE AS CRAP.",
        DialogLayout.BOTTOM)
    game.over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap2(sprite2, otherSprite2):
    statusbar.value = 100
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap2)

def on_on_zero2(status2):
    game.show_long_text("Ship Intercom: *slaps face* You needed to grab the fuel. COME ON!",
        DialogLayout.BOTTOM)
    game.over(False)
statusbars.on_zero(StatusBarKind.energy, on_on_zero2)

def on_on_overlap3(sprite3, otherSprite3):
    statusbar2.value += -20
    otherSprite3.destroy(effects.fire, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
darts: List[Image] = []
statusbar2: StatusBarSprite = None
enemySpeed = 0
statusbar: StatusBarSprite = None
mySprite: Sprite = None
game.splash("You feel a strange, cold breeze, and you are suddenly awoken by the President.")
game.show_long_text("Mr. President: Hello, you've been selected to fight evil in the galaxy. Complete this mission for the chance to earn $700,000,000.",
    DialogLayout.BOTTOM)
scene.set_background_image(assets.image("""
    Galaxy
"""))
scroller.scroll_background_with_speed(0, 10)
mySprite = sprites.create(assets.image("""
    Rocket
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
animation.run_image_animation(mySprite,
    assets.animation("""
        Flying Rocket
    """),
    100,
    True)
statusbar = statusbars.create(20, 4, StatusBarKind.energy)
statusbar.attach_to_sprite(mySprite, -30, 0)
enemySpeed = 50
statusbar2 = statusbars.create(4, 20, StatusBarKind.health)
statusbar2.attach_to_sprite(mySprite, 0, 0)
statusbar.set_label("Gas")
statusbar2.set_label("HP")

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_side(assets.image("""
        Fuel
    """), 0, 80)
    myFuel.x = randint(5, 155)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        Spider
    """), 0, enemySpeed)
    myEnemy.x = randint(5, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        assets.animation("""
            Flying Spider
        """),
        100,
        True)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    statusbar.value += -1
game.on_update_interval(500, on_update_interval3)