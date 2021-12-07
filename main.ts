namespace SpriteKind {
    export const Gas = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    darts = [
    assets.image`Dart1`,
    assets.image`Dart2`,
    img`
        . . 1 1 . . 
        . . 1 1 . . 
        5 1 1 1 1 5 
        5 5 5 5 5 5 
        . . 5 5 . . 
        . 5 . . 5 . 
        `,
    img`
        . . 1 1 . . 
        . . 1 1 . . 
        7 1 1 1 1 7 
        7 7 7 7 7 7 
        . . 7 7 . . 
        . 7 . . 7 . 
        `,
    img`
        . . 1 1 . . 
        . . 1 1 . . 
        9 1 1 1 1 9 
        9 9 9 9 9 9 
        . . 9 9 . . 
        . 9 . . 9 . 
        `,
    img`
        . . 1 1 . . 
        . . 1 1 . . 
        a 1 1 1 1 a 
        a a a a a a 
        . . a a . . 
        . a . . a . 
        `
    ]
    projectile = sprites.createProjectileFromSprite(darts._pickRandom(), mySprite, 0, -150)
    projectile.startEffect(effects.warmRadial, 100)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy(effects.disintegrate, 500)
    otherSprite.destroy()
    info.changeScoreBy(1)
    if (info.score() == 5) {
        game.showLongText("Ship Intercom: We forgot to tell you, your projectiles steal data from the ships before destroying them. And also, please don't get hit too many times, these ships are really expensive.", DialogLayout.Bottom)
    }
    if (info.score() == 10) {
        info.changeScoreBy(5)
        mySprite.sayText("+5 Level-Up Bonus", 2000, false)
        statusbar2.value = 100
        enemySpeed = 70
    } else if (info.score() == 25) {
        info.changeScoreBy(5)
        mySprite.sayText("+5 Level-Up Bonus", 2000, false)
        statusbar2.value = 100
        enemySpeed = 90
    } else if (info.score() == 40) {
        game.showLongText("Congrats soldier, you saved the galaxy. Accept this reward of $700,000,000!", DialogLayout.Bottom)
        game.splash("Please leave a suggestion at https://forms.gle/iL9fAhUxfJrnBHZ7A")
        info.changeScoreBy(700000000)
        game.over(true)
    }
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.showLongText("Ship Intercom: Come in soldier... soldier? I TOLD HIM THESE ARE EXPENSIVE!", DialogLayout.Bottom)
    game.splash("Please leave a suggestion at https://forms.gle/iL9fAhUxfJrnBHZ7A")
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite3, otherSprite3) {
    statusbar2.value += -20
    otherSprite3.destroy(effects.fire, 500)
    scene.cameraShake(4, 500)
})
scene.onHitWall(SpriteKind.Enemy, function (sprite, location) {
    statusbar.value += -20
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gas, function (sprite2, otherSprite2) {
    statusbar.value = 100
    otherSprite2.destroy()
})
statusbars.onZero(StatusBarKind.Energy, function (status2) {
    game.showLongText("Ship Intercom: *slaps face* You needed to grab the fuel. COME ON!", DialogLayout.Bottom)
    game.splash("Please leave a suggestion at https://forms.gle/iL9fAhUxfJrnBHZ7A")
    game.over(false)
})
let myEnemy: Sprite = null
let myFuel: Sprite = null
let projectile: Sprite = null
let darts: Image[] = []
let statusbar2: StatusBarSprite = null
let enemySpeed = 0
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
game.splash("You feel a strange, cold breeze, and you are suddenly awoken by the President.")
game.showLongText("Mr. President: Hello, you've been selected to fight evil in the galaxy. Complete this mission for the chance to earn $700,000,000.", DialogLayout.Bottom)
scene.setBackgroundImage(assets.image`Galaxy`)
scroller.scrollBackgroundWithSpeed(0, 10)
mySprite = sprites.create(assets.image`Rocket`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setStayInScreen(true)
animation.runImageAnimation(
mySprite,
assets.animation`Flying Rocket`,
100,
true
)
statusbar = statusbars.create(20, 4, StatusBarKind.Energy)
statusbar.attachToSprite(mySprite, -30, 0)
enemySpeed = 50
statusbar2 = statusbars.create(4, 20, StatusBarKind.Health)
statusbar2.attachToSprite(mySprite, 0, 0)
statusbar.setLabel("Gas")
statusbar2.setLabel("HP")
game.onUpdateInterval(5000, function () {
    myFuel = sprites.createProjectileFromSide(assets.image`Fuel`, 0, 80)
    myFuel.x = randint(5, 155)
    myFuel.setKind(SpriteKind.Gas)
})
game.onUpdateInterval(2000, function () {
    myEnemy = sprites.createProjectileFromSide(assets.image`Spider`, 0, enemySpeed)
    myEnemy.x = randint(5, 155)
    myEnemy.setKind(SpriteKind.Enemy)
    animation.runImageAnimation(
    myEnemy,
    assets.animation`Flying Spider`,
    100,
    true
    )
})
game.onUpdateInterval(500, function () {
    statusbar.value += -1
})
