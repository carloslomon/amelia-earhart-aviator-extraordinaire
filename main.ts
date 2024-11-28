namespace SpriteKind {
    export const Screen = SpriteKind.create()
    export const Wind = SpriteKind.create()
    export const Fog = SpriteKind.create()
    export const Wave = SpriteKind.create()
    export const Obsolete = SpriteKind.create()
    export const Fuel = SpriteKind.create()
}

namespace StatusBarKind {
    export const Fuel2 = StatusBarKind.create()
}

scene.onHitWall(SpriteKind.Player, function on_hit_wall(sprite: Sprite, location: tiles.Location) {
    
    if (mySprite.isHittingTile(CollisionDirection.Right)) {
        if (takeoff) {
            end_with("You've reached the end of the runway.")
        }
        
    } else if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        if (sprites.readDataBoolean(mySprite, "Landing Gear")) {
            wind = false
            callDirection = false
            scroller.scrollBackgroundWithSpeed(-10, 0)
            if (landing) {
                mySprite.setVelocity(45, 0)
                timer.after(2500, function on_after() {
                    if (circumnavigation) {
                        if (blockSettings.readNumber("Level") < 7) {
                            blockSettings.writeNumber("Level", blockSettings.readNumber("Level") + 1)
                            end_with("A successful landing! You have " + ("" + (8 - blockSettings.readNumber("Level"))) + " more flights left in your circumnavigation trip.")
                        } else if (blockSettings.readNumber("Level") == 7) {
                            levelImages[selectedFlight] = img`
                                . . . . . . . . . . . . . . . 
                                                                . . . . . . . . . . . . . . . 
                                                                . . . . . a a a a a . . . . . 
                                                                . . . . a . . . . . a . . . . 
                                                                . . . . . . . . . . a . 7 . . 
                                                                . . . . . . . . . . a 7 7 . . 
                                                                . . . . . . . . . . 7 7 . . . 
                                                                . . . . . 5 5 5 5 7 7 . . . . 
                                                                . . . . 5 5 5 5 5 7 5 . . . . 
                                                                . . . . 7 7 5 f 7 7 5 . . . . 
                                                                . . . . 5 7 7 f 7 5 5 . . . . 
                                                                . . . . 5 5 7 7 7 5 5 . . . . 
                                                                . . . . 5 5 5 7 5 5 5 . . . . 
                                                                . . . . 5 5 5 5 5 5 5 . . . . 
                                                                . . . . . . . . . . . . . . .
                            `
                            blockSettings.writeImageArray("Levels", levelImages)
                            blockSettings.writeNumber("Level", 0)
                            end_with("Congratulations, you've made it to Howland Island and have completed what Amelia Earhart could not!")
                        }
                        
                    } else {
                        levelImages[selectedFlight] = img`
                            . . . . . . . . . . . . . . . 
                                                        . . . . . . . . . . . . . . . 
                                                        . . . . . a a a a a . . . . . 
                                                        . . . . a . . . . . a . . . . 
                                                        . . . . . . . . . . a . 7 . . 
                                                        . . . . . . . . . . a 7 7 . . 
                                                        . . . . . . . . . . 7 7 . . . 
                                                        . . . . . 5 5 5 5 7 7 . . . . 
                                                        . . . . 5 5 5 5 5 7 5 . . . . 
                                                        . . . . 7 7 5 f 7 7 5 . . . . 
                                                        . . . . 5 7 7 f 7 5 5 . . . . 
                                                        . . . . 5 5 7 7 7 5 5 . . . . 
                                                        . . . . 5 5 5 7 5 5 5 . . . . 
                                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                                        . . . . . . . . . . . . . . .
                        `
                        if (levelImages[selectedFlight + 1].equals(img`
                            . . . . . . . . . . . . . . . 
                                                        . . . . . . . . . . . . . . . 
                                                        . . . . . a a a a a . . . . . 
                                                        . . . . a . . . . . a . . . . 
                                                        . . . . a . . . . . a . . . . 
                                                        . . . . a . . . . . a . . . . 
                                                        . . . . a . . . . . a . . . . 
                                                        . . . . a 5 5 5 5 5 a . . . . 
                                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                                        . . . . . . . . . . . . . . .
                        `)) {
                            levelImages[selectedFlight + 1] = img`
                                . . . . . . . . . . . . . . . 
                                                                . . . . . . . . . . . . . . . 
                                                                . . . . . a a a a a . . . . . 
                                                                . . . . a . . . . . a . . . . 
                                                                . . . . . . . . . . a . . . . 
                                                                . . . . . . . . . . a . . . . 
                                                                . . . . . . . . . . a . . . . 
                                                                . . . . . 5 5 5 5 5 a . . . . 
                                                                . . . . 5 5 5 5 5 5 5 . . . . 
                                                                . . . . 5 5 5 f 5 5 5 . . . . 
                                                                . . . . 5 5 5 f 5 5 5 . . . . 
                                                                . . . . 5 5 5 f 5 5 5 . . . . 
                                                                . . . . 5 5 5 f 5 5 5 . . . . 
                                                                . . . . 5 5 5 5 5 5 5 . . . . 
                                                                . . . . . . . . . . . . . . .
                            `
                        }
                        
                        blockSettings.writeImageArray("Levels", levelImages)
                        end_with("A successful landing! Congratulations!")
                    }
                    
                })
            }
            
        } else if (landing) {
            scene.cameraShake(2, 500)
            timer.after(1000, function on_after2() {
                end_with("That was definitely unnecessary. Was it really that hard to deploy the landing gear???")
            })
        } else if (wind) {
            if (statusbar.value > 0) {
                scene.cameraShake(2, 500)
                mySprite.ay = 250
                timer.after(1000, function on_after3() {
                    end_with("You crash landed! I hope you had a good reason for this!")
                })
            } else {
                outOfFuelCrash()
            }
            
        }
        
    }
    
})
function loading(time: number) {
    
    blackScreen = sprites.create(image.create(160, 120), SpriteKind.Screen)
    blackScreen.setPosition(80, 60)
    blackScreen.setFlag(SpriteFlag.RelativeToCamera, true)
    blackScreen.image.fill(15)
    blackScreen.z = 100
    myTextSprite2 = fancyText.create("Loading...", 75, 1, fancyText.defaultArcade)
    myTextSprite2.z = 101
    myTextSprite2.setPosition(80, 60)
    myTextSprite2.setFlag(SpriteFlag.RelativeToCamera, true)
    pause(time)
    sprites.destroy(blackScreen)
    sprites.destroy(myTextSprite2)
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile22
    `, function on_overlap_tile(sprite2: Sprite, location2: tiles.Location) {
    tree_crash()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile13
    `, function on_overlap_tile2(sprite3: Sprite, location3: tiles.Location) {
    
    if (endless) {
        if (score > blockSettings.readNumber("High Score")) {
            blockSettings.writeNumber("High Score", score)
            timer.after(4000, function on_after4() {
                end_with("New high score!")
            })
        }
        
    }
    
    if (statusbar.value > 0) {
        if (!crashed) {
            crashed = true
            wind = false
            callDirection = false
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            scene.cameraShake(2, 500)
            tiles.placeOnTile(mySprite, location3.getNeighboringLocation(CollisionDirection.Top))
            controller.moveSprite(mySprite, 0, 0)
            mySprite.setVelocity(1, 5)
            scroller.scrollBackgroundWithSpeed(-5, 0, scroller.BackgroundLayer.Layer0)
            mySprite.startEffect(effects.fountain, 1000)
            timer.after(7500, function on_after5() {
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            })
        }
        
    } else {
        outOfFuelCrash()
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (takeoff) {
        mySprite.vx += 3
        scroll_background()
        if (mySprite.vx >= 118) {
            mySprite.vy += -6
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            animation.runImageAnimation(mySprite, [img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . 5 . . . . . . 
                                        . . a a a a a c c c c c c c c c c c f 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c c c c f c c c . . . 
                                        . . . . . . . . . . . . . . . . . . 5 . . . . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c c c c 5 c c c . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c c 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 5 c c c c . . 
                                        . . c c c c c c c c c c c c c c c c c c c c . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c c c c 5 c c c . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . .
                    `], 100, true)
            takeoff = false
            timer.after(8250, function on_after6() {
                
                callDirection = true
            })
        }
        
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile7
    `, function on_overlap_tile3(sprite4: Sprite, location4: tiles.Location) {
    
    if (endless) {
        if (score > blockSettings.readNumber("High Score")) {
            blockSettings.writeNumber("High Score", score)
            timer.after(4000, function on_after7() {
                end_with("New high score!")
            })
        }
        
    }
    
    if (statusbar.value > 0) {
        if (!crashed) {
            crashed = true
            wind = false
            callDirection = false
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            scene.cameraShake(2, 500)
            tiles.placeOnTile(mySprite, location4.getNeighboringLocation(CollisionDirection.Top))
            controller.moveSprite(mySprite, 0, 0)
            mySprite.setVelocity(1, 5)
            scroller.scrollBackgroundWithSpeed(-5, 0, scroller.BackgroundLayer.Layer0)
            mySprite.startEffect(effects.fountain, 1000)
            timer.after(7500, function on_after8() {
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            })
        }
        
    } else {
        outOfFuelCrash()
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile4
    `, function on_overlap_tile4(sprite5: Sprite, location5: tiles.Location) {
    if (!takeoff) {
        flight("Fog", timems, 0, terrain2, "Grass")
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile9
    `, function on_overlap_tile5(sprite6: Sprite, location6: tiles.Location) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(20, mySprite.tilemapLocation().row))
    scene.cameraFollowSprite(mySprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile3
    `, function on_overlap_tile6(sprite7: Sprite, location7: tiles.Location) {
    tiles.setTileAt(location7, assets.tile`
        transparency16
    `)
})
function flight(weather: string, time2: number, airfield: number, terrain: string, landingAirfield: string) {
    
    weather = weather
    mySprite.setVelocity(100, 0)
    scroller.scrollBackgroundWithSpeed(-105, 0)
    if (terrain == "Ocean") {
        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
            sky
        `))
    } else if (terrain == "Land") {
        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
            level25
        `))
    } else if (terrain == "Desert") {
        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
            level29
        `))
    } else if (terrain == "Jungle") {
        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
            level71
        `))
    }
    
    tiles.placeOnRandomTile(mySprite, assets.tile`
        start
    `)
    animation.runImageAnimation(mySprite, [img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                        . c c c c c c c c c c c c c c c c c f 6 6 6 6 . . 
                        . c c b b b c c c c c b b b b b a a 2 c c c c . . 
                        . . c b b c c c c c c c c b b b b a 2 c c c . . . 
                        . . . . . . . . . . . . . . . . . . f . . . . . . 
                        . . . . . . . . . . . . . . . . . . 5 . . . . . .
            `, img`
                . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a c c c c c c c c c c c c 6 6 6 6 . . . 
                        . c a a a a a c c c c c c c c c c c 5 6 6 6 6 . . 
                        . c c c c c c c c c c b b b b b a a 2 c c c c . . 
                        . . c b b b c c c c c c c b b b b a 2 c c c . . . 
                        . . . b b . . . . . . . . b b b b . 5 . . . . . . 
                        . . . b . . . . . . . . . . . . . . . . . . . . .
            `, img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . a a a a . . . . . . . . 
                        . . a a a a c c c c c c c c c c c c 6 6 6 6 . . . 
                        . c a a a a a c c c c c c c c c c c c 6 6 6 6 . . 
                        . c c c c c c c c c c b b b b b a a 5 c c c c . . 
                        . . c b b b c c c c c c c b b b b a 2 c c c . . . 
                        . . . b b . . . . . . . . b b b b . . . . . . . . 
                        . . . b . . . . . . . . . . c c c . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . .
            `], 100, false)
    timer.after(750, function on_after9() {
        animation.runImageAnimation(mySprite, [img`
                    .........................
                                ............aa...........
                                ...........aaaa..........
                                ...........aaaa..5.......
                                .a.........aaaaa.f.......
                                .aa.......aaaaaaa2.......
                                .aaa......aaaaaaa2.......
                                .aaaa.....aaaaaa.f.......
                                .aaaacccccccccccc6666....
                                caaaaacccccccccccc6666...
                                cccccccccccccccccccccc...
                                .cccccccccccccccc5ccc....
                                .ccc......cccccc.f.......
                                .cc.......ccccccc2.......
                                ..........ccccccc2.......
                                ..........cccccc.f.......
                                ...........ccccc.5.......
                                ...........cccc..........
                                ...........cccc..........
                                ............cc...........
                `, img`
                    .........................
                                ............aa...........
                                ...........aaaa..........
                                ...........aaaa..........
                                .a.........aaaaa.5.......
                                .aa.......aaaaaaa2.......
                                .aaa......aaaaaaa2.......
                                .aaaa.....aaaaaa.5.......
                                .aaaacccccccccccc6666....
                                caaaaacccccccccccc6666...
                                cccccccccccccccccccccc...
                                .cccccccccccccccccccc....
                                .ccc......cccccc.5.......
                                .cc.......ccccccc2.......
                                ..........ccccccc2.......
                                ..........cccccc.5.......
                                ...........ccccc.........
                                ...........cccc..........
                                ...........cccc..........
                                ............cc...........
                `, img`
                    .........................
                                .........................
                                ............aaa..........
                                .a.........aaaa..........
                                .aa........aaaaa.........
                                .aaa.......aaaaaa5.......
                                .aaaa.....aaaaaaa2.......
                                .aaaa.....aaaaaa.........
                                .aaaaaccccccccccc6666....
                                ccccccccccccccccccc666...
                                cccccccccccccccccccccc...
                                .cccccccccccccccccccc....
                                .cc.......cccccc.........
                                ..........ccccccc5.......
                                ..........ccccccc2.......
                                ...........ccccc.........
                                ...........cccc..........
                                ...........cccc..........
                                ............cc...........
                                .........................
                `, img`
                    .........................
                                .........................
                                ............aaa..........
                                .a.........aaaa..........
                                .aa........aaaaa.5.......
                                .aaa.......aaaaaa2.......
                                .aaaa.....aaaaaaa2.......
                                .aaaa.....aaaaaa.5.......
                                .aaaaaccccccccccc6666....
                                ccccccccccccccccccc666...
                                cccccccccccccccccccccc...
                                .cccccccccccccccccccc....
                                .cc.......cccccc.5.......
                                ..........ccccccc2.......
                                ..........ccccccc2.......
                                ...........ccccc.5.......
                                ...........cccc..........
                                ...........cccc..........
                                ............cc...........
                                .........................
                `], 200, true)
    })
    flying = true
    fuel_bar(250)
    controller.moveSprite(mySprite, 0, 30)
    wind = true
    if (weather == "Clouds") {
        
    } else if (weather == "Fog") {
        
    } else if (weather == "Rain") {
        
    }
    
    timer.after(time2, function on_after10() {
        
        
        if (!crashed) {
            weather = "N/A"
            fog = false
            rain = false
            waves = false
            wind = false
            flying = false
            controller.moveSprite(mySprite, 0, 0)
            sprites.destroyAllSpritesOfKind(SpriteKind.Wind)
            sprites.destroyAllSpritesOfKind(SpriteKind.Fog)
            sprites.destroyAllSpritesOfKind(SpriteKind.Wave)
            sprites.setDataBoolean(mySprite, "Landing Gear", false)
            achievements.create("You are landing. Press 'A' to deploy landing gear.")
            animation.runImageAnimation(mySprite, [img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . a a a a . . . . . . . . 
                                        . . a a a a c c c c c c c c c c c c 6 6 6 6 . . . 
                                        . c a a a a a c c c c c c c c c c c c 6 6 6 6 . . 
                                        . c c c c c c c c c c b b b b b a a 5 c c c c . . 
                                        . . c b b b c c c c c c c b b b b a 2 c c c . . . 
                                        . . . b b . . . . . . . . b b b b . . . . . . . . 
                                        . . . b . . . . . . . . . . c c c . . . . . . . . 
                                        . . . . . . . . . . . . . . . . . . . . . . . . .
                    `, img`
                        . . . . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a c c c c c c c c c c c c 6 6 6 6 . . . 
                                        . c a a a a a c c c c c c c c c c c 5 6 6 6 6 . . 
                                        . c c c c c c c c c c b b b b b a a 2 c c c c . . 
                                        . . c b b b c c c c c c c b b b b a 2 c c c . . . 
                                        . . . b b . . . . . . . . b b b b . 5 . . . . . . 
                                        . . . b . . . . . . . . . . . . . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                        . c c c c c c c c c c c c c c c c c f 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b a a 2 c c c c . . 
                                        . . c b b c c c c c c c c b b b b a 2 c c c . . . 
                                        . . . . . . . . . . . . . . . . . . f . . . . . . 
                                        . . . . . . . . . . . . . . . . . . 5 . . . . . .
                    `], 100, false)
            if (landingAirfield == "Grass") {
                tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                    level33
                `))
            }
            
            tiles.placeOnRandomTile(mySprite, assets.tile`
                myTile10
            `)
            scroller.scrollBackgroundWithSpeed(-55, 0)
            mySprite.setVelocity(50, 10)
            timer.after(300, function on_after11() {
                
                animation.runImageAnimation(mySprite, [img`
                            . . a . . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a . . . . . . . . . . . . 5 . . . . . . 
                                                . . a a a a a c c c c c c c c c c c f 6 6 6 . . . 
                                                . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                                . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                                . . c c c c c c c c c c c c c c c c f c c c . . . 
                                                . . . . . . . . . . . . . . . . . . 5 . . . . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . .
                        `, img`
                            . . a . . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                                . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                                . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                                . . c c c c c c c c c c c c c c c c 5 c c c . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . .
                        `, img`
                            . . a . . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a a c c c c c c c c c c c c 6 6 6 . . . 
                                                . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                                . c c b b b c c c c c b b b b b b a 5 c c c c . . 
                                                . . c c c c c c c c c c c c c c c c c c c c . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . .
                        `, img`
                            . . a . . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a . . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a . . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a . . . . . . . . . . . . . . . . . . . 
                                                . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                                . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                                . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                                . . c c c c c c c c c c c c c c c c 5 c c c . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . . . . . . . . . . .
                        `], 100, true)
                landing = true
            })
        }
        
    })
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile29
    `, function on_overlap_tile7(sprite8: Sprite, location8: tiles.Location) {
    tree_crash()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile17
    `, function on_overlap_tile8(sprite9: Sprite, location9: tiles.Location) {
    if (!takeoff) {
        flight("Wind", timems, 1, terrain2, "Grass")
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Fuel, function on_on_overlap(sprite10: Sprite, otherSprite: Sprite) {
    if (!crashed) {
        sprites.destroy(otherSprite)
        statusbar.value += 5
    }
    
})
function tree_crash() {
    
    if (!crashed) {
        crashed = true
        wind = false
        callDirection = false
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        scene.cameraShake(2, 500)
        controller.moveSprite(mySprite, 0, 0)
        mySprite.setVelocity(30, 40)
        mySprite.startEffect(effects.fire, 1000)
        timer.after(7500, function on_after12() {
            if (statusbar.value > 0) {
                end_with("You crashed into a tree. This probably could've been avoided.")
            } else {
                end_with("I'm going to assume you tried your best...")
            }
            
        })
    }
    
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile5
    `, function on_overlap_tile9(sprite11: Sprite, location10: tiles.Location) {
    tiles.setTileAt(location10, assets.tile`
        transparency16
    `)
})
function scroll_background() {
    scroller.scrollBackgroundWithSpeed(mySprite.vx / 2 * -1 - 5, 0, scroller.BackgroundLayer.Layer0)
}

function fuel_bar(fuel: number) {
    
    statusbar = statusbars.create(50, 6, StatusBarKind.Fuel2)
    statusbar.max = fuel
    statusbar.value = fuel
    statusbar.setColor(4, 0, 2)
    statusbar.setStatusBarFlag(StatusBarFlag.SmoothTransition, true)
    statusbar.setLabel("Fuel", 15)
    statusbar.setPosition(39, 6)
    statusbar.setFlag(SpriteFlag.RelativeToCamera, true)
}

function end_with(message: string) {
    game.setDialogFrame(img`
        b b b b b b b b b b b b b b b 
                b a b a b a b a b a b a b a b 
                b b b b b b b b b b b b b b b 
                b a b b b b b b b b b b b a b 
                b b b b b b b b b b b b b b b 
                b a b b b b b b b b b b b a b 
                b b b b b b b b b b b b b b b 
                b a b b b b b b b b b b b a b 
                b b b b b b b b b b b b b b b 
                b a b b b b b b b b b b b a b 
                b b b b b b b b b b b b b b b 
                b a b b b b b b b b b b b a b 
                b b b b b b b b b b b b b b b 
                b a b a b a b a b a b a b a b 
                b b b b b b b b b b b b b b b
    `)
    game.setDialogCursor(img`
        .........................
                ............aa...........
                ...........aaaa..........
                ...........aaaa..5.......
                .a.........aaaaa.f.......
                .aa.......aaaaaaa2.......
                .aaa......aaaaaaa2.......
                .aaaa.....aaaaaa.f.......
                .aaaacccccccccccc6666....
                caaaaacccccccccccc6666...
                cccccccccccccccccccccc...
                .cccccccccccccccc5ccc....
                .ccc......cccccc.f.......
                .cc.......ccccccc2.......
                ..........ccccccc2.......
                ..........cccccc.f.......
                ...........ccccc.5.......
                ...........cccc..........
                ...........cccc..........
                ............cc...........
    `)
    game.showLongText(message, DialogLayout.Full)
    game.reset()
}

statusbars.onStatusReached(StatusBarKind.Fuel2, statusbars.StatusComparison.EQ, statusbars.ComparisonType.Percentage, 0, function on_status_reached_comparison_eq_type_percentage(status: StatusBarSprite) {
    
    if (!crashed) {
        crashed = true
        wind = false
        controller.moveSprite(mySprite, 0, 0)
        mySprite.ay = 1
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
        timer.background(function on_background() {
            Notification.notify("You've run out of fuel... This won't end well.", 5)
        })
    }
    
})
function outOfFuelCrash() {
    
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    scene.cameraShake(2, 500)
    callDirection = false
    mySprite.setVelocity(1, 4)
    scroller.scrollBackgroundWithSpeed(-5, 0, scroller.BackgroundLayer.Layer0)
    timer.after(5000, function on_after13() {
        mySprite.setVelocity(0, 0)
        mySprite.setKind(SpriteKind.Obsolete)
        end_with("Ouch. If only you had more fuel...")
    })
}

sprites.onOverlap(SpriteKind.Wave, SpriteKind.Player, function on_on_overlap2(sprite12: Sprite, otherSprite2: Sprite) {
    
    if (endless) {
        if (score > blockSettings.readNumber("High Score")) {
            blockSettings.writeNumber("High Score", score)
            timer.after(4000, function on_after14() {
                end_with("New high score!")
            })
        }
        
    }
    
    if (statusbar.value > 0) {
        if (!crashed) {
            crashed = true
            wind = false
            callDirection = false
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            scene.cameraShake(2, 500)
            controller.moveSprite(mySprite, 0, 0)
            mySprite.setVelocity(1, 5)
            scroller.scrollBackgroundWithSpeed(-5, 0, scroller.BackgroundLayer.Layer0)
            mySprite.startEffect(effects.fountain, 1000)
            timer.after(7500, function on_after15() {
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            })
        }
        
    } else {
        outOfFuelCrash()
    }
    
})
function start(airfield2: string) {
    
    loading(randint(1000, 2500))
    story.setSoundEnabled(false)
    story.printText(airfield2, mySprite.x - 5, mySprite.y - 100, 1, 15, story.TextSpeed.Slow)
    story.printText("Spam 'A' to take off.", mySprite.x - 5, mySprite.y - 100, 1, 15, story.TextSpeed.Slow)
    mySprite.ay = 0
    takeoff = true
    animation.runImageAnimation(mySprite, [img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a . . . . . . . . . . . . 5 . . . . . . 
                        . . a a a a a c c c c c c c c c c c f 6 6 6 . . . 
                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                        . . c c c c c c c c c c c c c a c c f c c c . . . 
                        . a . . . . . . . . . . . . f f . . 5 . . . . . . 
                        f . . . . . . . . . . . . . f f . . . . . . . . .
            `, img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                        . . c c c c c c c c c c c c c a c c 5 c c c . . . 
                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                        f . . . . . . . . . . . . . f f . . . . . . . . .
            `, img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                        . . a a a a a c c c c c c c c c c c c 6 6 6 . . . 
                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                        . c c b b b c c c c c b b b b b b a 5 c c c c . . 
                        . . c c c c c c c c c c c c c a c c c c c c . . . 
                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                        f . . . . . . . . . . . . . f f . . . . . . . . .
            `, img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                        . . c c c c c c c c c c c c c a c c 5 c c c . . . 
                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                        f . . . . . . . . . . . . . f f . . . . . . . . .
            `], 100, true)
}

scene.onHitWall(SpriteKind.Wave, function on_hit_wall2(sprite13: Sprite, location11: tiles.Location) {
    sprites.destroy(sprite13)
})
function direction() {
    if (callDirection) {
        if (mySprite.vy < 0) {
            CustomLives.loseLife()
            CustomLives.setLifeImageAndMax(img`
                    . . . 2 2 . . . 
                                    . . 2 2 2 2 . . 
                                    . 2 2 2 2 2 2 . 
                                    2 2 2 2 2 2 2 2 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . .
                `, 1, 0)
            CustomLives.setLifePosition(155, 7)
            scroller.scrollBackgroundWithSpeed(-105, 10)
        } else if (mySprite.vy > 0) {
            CustomLives.loseLife()
            CustomLives.setLifeImageAndMax(img`
                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    . . 2 2 2 2 . . 
                                    2 2 2 2 2 2 2 2 
                                    . 2 2 2 2 2 2 . 
                                    . . 2 2 2 2 . . 
                                    . . . 2 2 . . .
                `, 1, 0)
            CustomLives.setLifePosition(155, 7)
            scroller.scrollBackgroundWithSpeed(-105, -10)
        } else {
            CustomLives.loseLife()
            scroller.scrollBackgroundWithSpeed(-105, 0)
        }
        
    }
    
}

scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile14
    `, function on_overlap_tile10(sprite14: Sprite, location12: tiles.Location) {
    if (!takeoff) {
        flight("Rain", timems, 1, terrain2, "Grass")
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Wind, function on_on_overlap3(sprite15: Sprite, otherSprite3: Sprite) {
    statusbar.value += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile28
    `, function on_overlap_tile11(sprite16: Sprite, location13: tiles.Location) {
    tree_crash()
})
let waveSprite : Sprite = null
let fogSprite : Sprite = null
let windSprite : Sprite = null
let waves = false
let rain = false
let fog = false
let myTextSprite2 : fancyText.TextSprite = null
let blackScreen : Sprite = null
let statusbar : StatusBarSprite = null
let myTextSprite3 : fancyText.TextSprite = null
let score = 0
let chosenFlight = 0
let landingAirfield2 = ""
let weather2 = ""
let terrain2 = ""
let timems = 0
let selectedFlight = 0
let myMenu2 : miniMenu.MenuSprite = null
let mySprite : Sprite = null
let levelImages : Image[] = []
let callDirection = false
let circumnavigation = false
let wind = false
let flying = false
let crashed = false
let endless = false
let landing = false
let takeoff = false
console.log("game started")
takeoff = false
landing = false
endless = false
crashed = false
flying = false
wind = false
circumnavigation = false
callDirection = false
if (!blockSettings.exists("High Score")) {
    blockSettings.writeNumber("High Score", 0)
}

if (!blockSettings.exists("Levels")) {
    blockSettings.writeImageArray("Levels", [img`
                . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . 
                        . . . . . a a a a a . . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . . . . . . . a . . . . 
                        . . . . . . . . . . a . . . . 
                        . . . . . . . . . . a . . . . 
                        . . . . . 5 5 5 5 5 a . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . .
            `, img`
                . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . 
                        . . . . . a a a a a . . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a 5 5 5 5 5 a . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . .
            `, img`
                . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . 
                        . . . . . a a a a a . . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a 5 5 5 5 5 a . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . .
            `, img`
                . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . 
                        . . . . . a a a a a . . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a . . . . . a . . . . 
                        . . . . a 5 5 5 5 5 a . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 f 5 5 5 . . . . 
                        . . . . 5 5 5 5 5 5 5 . . . . 
                        . . . . . . . . . . . . . . .
            `])
}

levelImages = blockSettings.readImageArray("Levels")
if (!blockSettings.exists("Level")) {
    blockSettings.writeNumber("Level", 0)
}

let myTextSprite = fancyText.create("Amelia Earhart: Aviator Extraordinaire", 200, 11, fancyText.serif_small)
myTextSprite.setPosition(105, 15)
myTextSprite = fancyText.create("Amelia Earhart: Aviator Extraordinaire", 200, 12, fancyText.serif_small)
myTextSprite.setPosition(106, 15)
scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    `)
scroller.scrollBackgroundWithSpeed(-50, 0)
mySprite = sprites.create(img`
        .........................
            ............aa...........
            ...........aaaa..........
            ...........aaaa..5.......
            .a.........aaaaa.f.......
            .aa.......aaaaaaa2.......
            .aaa......aaaaaaa2.......
            .aaaa.....aaaaaa.f.......
            .aaaacccccccccccc6666....
            caaaaacccccccccccc6666...
            cccccccccccccccccccccc...
            .cccccccccccccccc5ccc....
            .ccc......cccccc.f.......
            .cc.......ccccccc2.......
            ..........ccccccc2.......
            ..........cccccc.f.......
            ...........ccccc.5.......
            ...........cccc..........
            ...........cccc..........
            ............cc...........
    `, SpriteKind.Player)
animation.runImageAnimation(mySprite, [img`
            .........................
                ............aa...........
                ...........aaaa..........
                ...........aaaa..5.......
                .a.........aaaaa.f.......
                .aa.......aaaaaaa2.......
                .aaa......aaaaaaa2.......
                .aaaa.....aaaaaa.f.......
                .aaaacccccccccccc6666....
                caaaaacccccccccccc6666...
                cccccccccccccccccccccc...
                .cccccccccccccccc5ccc....
                .ccc......cccccc.f.......
                .cc.......ccccccc2.......
                ..........ccccccc2.......
                ..........cccccc.f.......
                ...........ccccc.5.......
                ...........cccc..........
                ...........cccc..........
                ............cc...........
        `, img`
            .........................
                ............aa...........
                ...........aaaa..........
                ...........aaaa..........
                .a.........aaaaa.5.......
                .aa.......aaaaaaa2.......
                .aaa......aaaaaaa2.......
                .aaaa.....aaaaaa.5.......
                .aaaacccccccccccc6666....
                caaaaacccccccccccc6666...
                cccccccccccccccccccccc...
                .cccccccccccccccccccc....
                .ccc......cccccc.5.......
                .cc.......ccccccc2.......
                ..........ccccccc2.......
                ..........cccccc.5.......
                ...........ccccc.........
                ...........cccc..........
                ...........cccc..........
                ............cc...........
        `, img`
            .........................
                .........................
                ............aaa..........
                .a.........aaaa..........
                .aa........aaaaa.........
                .aaa.......aaaaaa5.......
                .aaaa.....aaaaaaa2.......
                .aaaa.....aaaaaa.........
                .aaaaaccccccccccc6666....
                ccccccccccccccccccc666...
                cccccccccccccccccccccc...
                .cccccccccccccccccccc....
                .cc.......cccccc.........
                ..........ccccccc5.......
                ..........ccccccc2.......
                ...........ccccc.........
                ...........cccc..........
                ...........cccc..........
                ............cc...........
                .........................
        `, img`
            .........................
                .........................
                ............aaa..........
                .a.........aaaa..........
                .aa........aaaaa.5.......
                .aaa.......aaaaaa2.......
                .aaaa.....aaaaaaa2.......
                .aaaa.....aaaaaa.5.......
                .aaaaaccccccccccc6666....
                ccccccccccccccccccc666...
                cccccccccccccccccccccc...
                .cccccccccccccccccccc....
                .cc.......cccccc.5.......
                ..........ccccccc2.......
                ..........ccccccc2.......
                ...........ccccc.5.......
                ...........cccc..........
                ...........cccc..........
                ............cc...........
                .........................
        `], 250, true)
mySprite.setPosition(80, 50)
let myMenu = miniMenu.createMenu(miniMenu.createMenuItem("Flights"), miniMenu.createMenuItem("Endless"), miniMenu.createMenuItem("Credits"))
myMenu.setDimensions(160, 50)
myMenu.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, images.colorBlock(15))
myMenu.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Background, images.colorBlock(11))
myMenu.setStyleProperty(miniMenu.StyleKind.All, miniMenu.StyleProperty.Border, 1)
myMenu.setStyleProperty(miniMenu.StyleKind.All, miniMenu.StyleProperty.BorderColor, images.colorBlock(12))
myMenu.setPosition(80, 103)
myMenu.onButtonPressed(controller.A, function on_button_pressed(selection: any, selectedIndex: any) {
    
    if (selection == "Flights") {
        myMenu.close()
        sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
        sprites.destroyAllSpritesOfKind(myTextSprite.kind())
        myMenu2 = miniMenu.createMenu(miniMenu.createMenuItem("Harbour Grace, Newfoundland to Londonderry, Northern Ireland", levelImages[0]), miniMenu.createMenuItem("Honolulu, Hawai'i to Oakland, California", levelImages[1]), miniMenu.createMenuItem("Los Angeles, California to Mexico City, Mexico", levelImages[2]), miniMenu.createMenuItem("Circumnavigation: Flight " + ("" + (blockSettings.readNumber("Level") + 1)), levelImages[3]), miniMenu.createMenuItem("Cancel"))
        myMenu2.setTitle("Flights")
        myMenu2.setDimensions(160, 120)
        myMenu2.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, images.colorBlock(15))
        myMenu2.setStyleProperty(miniMenu.StyleKind.Default, miniMenu.StyleProperty.Background, images.colorBlock(11))
        myMenu2.setStyleProperty(miniMenu.StyleKind.DefaultAndSelected, miniMenu.StyleProperty.Border, 2)
        myMenu2.setStyleProperty(miniMenu.StyleKind.DefaultAndSelected, miniMenu.StyleProperty.BorderColor, images.colorBlock(12))
        myMenu2.setStyleProperty(miniMenu.StyleKind.Title, miniMenu.StyleProperty.BorderColor, images.colorBlock(11))
        myMenu2.setPosition(80, 60)
        myMenu2.onButtonPressed(controller.A, function on_button_pressed2(selection2: any, selectedIndex2: number) {
            
            selectedFlight = selectedIndex2
            scroller.scrollBackgroundWithSpeed(-5, 0, scroller.BackgroundLayer.Layer0)
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            mySprite.setImage(img`
                . . a . . . . . . . . . . . . . . . . . . . . . . 
                                . . a a . . . . . . . . . . . . . . . . . . . . . 
                                . . a a a . . . . . . . . . . . . . . . . . . . . 
                                . . a a a a . . . . . . . . . . . . 5 . . . . . . 
                                . . a a a a a c c c c c c c c c c c f 6 6 6 . . . 
                                . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                . . c c c c c c c c c c c c c a c c f c c c . . . 
                                . a . . . . . . . . . . . . f f . . 5 . . . . . . 
                                f . . . . . . . . . . . . . f f . . . . . . . . .
            `)
            if (selectedIndex2 == 0) {
                timer.background(function on_background2() {
                    
                    myMenu2.close()
                    sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                    tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                        harbourgrace
                    `))
                    tiles.placeOnRandomTile(mySprite, assets.tile`
                        myTile3
                    `)
                    scene.cameraFollowSprite(mySprite)
                    mySprite.ay = 500
                    scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        `)
                    timems = 90000
                    terrain2 = "Ocean"
                    weather2 = "Fog"
                    landingAirfield2 = "Grass"
                })
                start("Harbour Grace, Newfoundland")
            } else if (selectedIndex2 == 1) {
                if (levelImages[1].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . 5 5 5 5 5 a . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `) || levelImages[1].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . 7 . . 
                                        . . . . . . . . . . a 7 7 . . 
                                        . . . . . . . . . . 7 7 . . . 
                                        . . . . . 5 5 5 5 7 7 . . . . 
                                        . . . . 5 5 5 5 5 7 5 . . . . 
                                        . . . . 7 7 5 f 7 7 5 . . . . 
                                        . . . . 5 7 7 f 7 5 5 . . . . 
                                        . . . . 5 5 7 7 7 5 5 . . . . 
                                        . . . . 5 5 5 7 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `)) {
                    timer.background(function on_background3() {
                        
                        myMenu2.close()
                        sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                            level38
                        `))
                        tiles.placeOnRandomTile(mySprite, assets.tile`
                            myTile3
                        `)
                        scene.cameraFollowSprite(mySprite)
                        mySprite.ay = 500
                        scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999
                                                            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab99999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa9999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa99999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab9999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            `)
                        timems = 85000
                        terrain2 = "Ocean"
                        weather2 = "Rain"
                        landingAirfield2 = "Grass"
                    })
                    start("Honolulu, Hawai'i")
                }
                
            } else if (selectedIndex2 == 2) {
                if (levelImages[2].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . 5 5 5 5 5 a . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `) || levelImages[2].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . 7 . . 
                                        . . . . . . . . . . a 7 7 . . 
                                        . . . . . . . . . . 7 7 . . . 
                                        . . . . . 5 5 5 5 7 7 . . . . 
                                        . . . . 5 5 5 5 5 7 5 . . . . 
                                        . . . . 7 7 5 f 7 7 5 . . . . 
                                        . . . . 5 7 7 f 7 5 5 . . . . 
                                        . . . . 5 5 7 7 7 5 5 . . . . 
                                        . . . . 5 5 5 7 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `)) {
                    timer.background(function on_background4() {
                        
                        myMenu2.close()
                        sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                            level48
                        `))
                        tiles.placeOnRandomTile(mySprite, assets.tile`
                            myTile3
                        `)
                        scene.cameraFollowSprite(mySprite)
                        mySprite.ay = 500
                        scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                            `)
                        timems = 80000
                        terrain2 = "Desert"
                        weather2 = "Wind"
                        landingAirfield2 = "Desert"
                    })
                    start("Los Angeles, California")
                }
                
            } else if (selectedIndex2 == 3) {
                if (levelImages[3].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . . . . . . a . . . . 
                                        . . . . . 5 5 5 5 5 a . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 f 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `) || levelImages[3].equals(img`
                    . . . . . . . . . . . . . . . 
                                        . . . . . . . . . . . . . . . 
                                        . . . . . a a a a a . . . . . 
                                        . . . . a . . . . . a . . . . 
                                        . . . . . . . . . . a . 7 . . 
                                        . . . . . . . . . . a 7 7 . . 
                                        . . . . . . . . . . 7 7 . . . 
                                        . . . . . 5 5 5 5 7 7 . . . . 
                                        . . . . 5 5 5 5 5 7 5 . . . . 
                                        . . . . 7 7 5 f 7 7 5 . . . . 
                                        . . . . 5 7 7 f 7 5 5 . . . . 
                                        . . . . 5 5 7 7 7 5 5 . . . . 
                                        . . . . 5 5 5 7 5 5 5 . . . . 
                                        . . . . 5 5 5 5 5 5 5 . . . . 
                                        . . . . . . . . . . . . . . .
                `)) {
                    myMenu2.close()
                    sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                    circumnavigation = true
                    if (levelImages[3].equals(img`
                        . . . . . . . . . . . . . . . 
                                                . . . . . . . . . . . . . . . 
                                                . . . . . a a a a a . . . . . 
                                                . . . . a . . . . . a . . . . 
                                                . . . . . . . . . . a . 7 . . 
                                                . . . . . . . . . . a 7 7 . . 
                                                . . . . . . . . . . 7 7 . . . 
                                                . . . . . 5 5 5 5 7 7 . . . . 
                                                . . . . 5 5 5 5 5 7 5 . . . . 
                                                . . . . 7 7 5 f 7 7 5 . . . . 
                                                . . . . 5 7 7 f 7 5 5 . . . . 
                                                . . . . 5 5 7 7 7 5 5 . . . . 
                                                . . . . 5 5 5 7 5 5 5 . . . . 
                                                . . . . 5 5 5 5 5 5 5 . . . . 
                                                . . . . . . . . . . . . . . .
                    `)) {
                        chosenFlight = game.askForNumber("Which flight do you want to do? 1-8", 1)
                        if (Math.ifNumberIsBetweenInputs(chosenFlight, 0, 8)) {
                            blockSettings.writeNumber("Level", chosenFlight - 1)
                        } else {
                            end_with("Invalid flight.")
                        }
                        
                    }
                    
                    if (blockSettings.readNumber("Level") == 0) {
                        timer.background(function on_background5() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level54
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 85000
                            terrain2 = "Land"
                            weather2 = "Wind"
                            landingAirfield2 = "Grass"
                        })
                        start("Oakland, California")
                    } else if (blockSettings.readNumber("Level") == 1) {
                        timer.background(function on_background6() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level54
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 75000
                            terrain2 = "Ocean"
                            weather2 = "Fog"
                            landingAirfield2 = "Grass"
                        })
                        start("Miami, Florida")
                    } else if (blockSettings.readNumber("Level") == 2) {
                        timer.background(function on_background7() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level38
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab99999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa9999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa99999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 70000
                            terrain2 = "Jungle"
                            weather2 = "Rain"
                            landingAirfield2 = "Grass"
                        })
                        start("Caripito, Venezuela")
                    } else if (blockSettings.readNumber("Level") == 3) {
                        timer.background(function on_background8() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level38
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 80000
                            terrain2 = "Ocean"
                            weather2 = "Wind"
                            landingAirfield2 = "Desert"
                        })
                        start("Natal, Brazil")
                    } else if (blockSettings.readNumber("Level") == 4) {
                        timer.background(function on_background9() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level65
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 90000
                            terrain2 = "Desert"
                            weather2 = "Clear"
                            landingAirfield2 = "Desert"
                        })
                        start("Dakar, Senegal")
                    } else if (blockSettings.readNumber("Level") == 5) {
                        timer.background(function on_background10() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level65
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab99999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa9999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa99999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 80000
                            terrain2 = "Land"
                            weather2 = "Storm"
                            landingAirfield2 = "Grass"
                        })
                        start("Karachi, Pakistan")
                    } else if (blockSettings.readNumber("Level") == 6) {
                        timer.background(function on_background11() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level38
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baab99999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaa9999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaab999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaabaa999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa99999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa99999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999baab999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999aaaaaa99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999aaaaaaab9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999aaaaaaaabaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999aaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999aabaaaaaaaaaaaaab9aaa9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999aaaaaaaaaaaaaaaaaaaaaaa999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999baaaaaaaaaaaaaaaaaaaaaaaaaaab99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 75000
                            terrain2 = "Ocean"
                            weather2 = "Storm"
                            landingAirfield2 = "Grass"
                        })
                        start("Bangkok, Thailand")
                    } else if (blockSettings.readNumber("Level") == 7) {
                        timer.background(function on_background12() {
                            
                            myMenu2.close()
                            sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
                            tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
                                level38
                            `))
                            tiles.placeOnRandomTile(mySprite, assets.tile`
                                myTile3
                            `)
                            scene.cameraFollowSprite(mySprite)
                            mySprite.ay = 500
                            scroller.setLayerImage(scroller.BackgroundLayer.Layer0, img`
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d11d99999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111d999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111d11999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111199999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911d1111111111111d9111999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111199999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999d111111111111111111111111111d9999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999999d11d999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999911111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999999991111111d9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999999999911111111d119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999991111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    99999999999999999999999999999999999999999999999911d1111111111111d91119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999911111111111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    999999999999999999999999999999999999999999999d111111111111111111111111111d99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                `)
                            timems = 90000
                            terrain2 = "Ocean"
                            weather2 = "Wind"
                            landingAirfield2 = "Grass"
                        })
                        start("Lae, Papa New Guinea")
                    }
                    
                }
                
            } else {
                game.reset()
            }
            
        })
    } else if (selection == "Endless") {
        myMenu.close()
        sprites.destroyAllSpritesOfKind(SpriteKind.MiniMenu)
        sprites.destroyAllSpritesOfKind(myTextSprite.kind())
        game.setDialogFrame(img`
            b b b b b b b b b b b b b b b 
                        b a b a b a b a b a b a b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b a b a b a b a b a b a b 
                        b b b b b b b b b b b b b b b
        `)
        game.setDialogCursor(img`
            .........................
                        ............aa...........
                        ...........aaaa..........
                        ...........aaaa..5.......
                        .a.........aaaaa.f.......
                        .aa.......aaaaaaa2.......
                        .aaa......aaaaaaa2.......
                        .aaaa.....aaaaaa.f.......
                        .aaaacccccccccccc6666....
                        caaaaacccccccccccc6666...
                        cccccccccccccccccccccc...
                        .cccccccccccccccc5ccc....
                        .ccc......cccccc.f.......
                        .cc.......ccccccc2.......
                        ..........ccccccc2.......
                        ..........cccccc.f.......
                        ...........ccccc.5.......
                        ...........cccc..........
                        ...........cccc..........
                        ............cc...........
        `)
        game.showLongText("Collect fuel in order to stay in the air! High score: " + ("" + blockSettings.readNumber("High Score")), DialogLayout.Full)
        score = 0
        flying = true
        wind = true
        endless = true
        callDirection = true
        controller.moveSprite(mySprite, 0, 30)
        scene.cameraFollowSprite(mySprite)
        tiles.setCurrentTilemap(tileUtil.createSmallMap(tilemap`
            sky
        `))
        mySprite.setVelocity(100, 0)
        scroller.scrollBackgroundWithSpeed(-105, 0)
        fuel_bar(25)
        myTextSprite3 = fancyText.create("Score: " + ("" + score), 100, 15, fancyText.defaultArcade)
        myTextSprite3.setPosition(5, 113)
        myTextSprite3.setFlag(SpriteFlag.RelativeToCamera, true)
    } else if (selection == "Credits") {
        game.setDialogFrame(img`
            b b b b b b b b b b b b b b b 
                        b a b a b a b a b a b a b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b b b b b b b b b b b a b 
                        b b b b b b b b b b b b b b b 
                        b a b a b a b a b a b a b a b 
                        b b b b b b b b b b b b b b b
        `)
        game.setDialogCursor(img`
            .........................
                        ............aa...........
                        ...........aaaa..........
                        ...........aaaa..5.......
                        .a.........aaaaa.f.......
                        .aa.......aaaaaaa2.......
                        .aaa......aaaaaaa2.......
                        .aaaa.....aaaaaa.f.......
                        .aaaacccccccccccc6666....
                        caaaaacccccccccccc6666...
                        cccccccccccccccccccccc...
                        .cccccccccccccccc5ccc....
                        .ccc......cccccc.f.......
                        .cc.......ccccccc2.......
                        ..........ccccccc2.......
                        ..........cccccc.f.......
                        ...........ccccc.5.......
                        ...........cccc..........
                        ...........cccc..........
                        ............cc...........
        `)
        game.showLongText("Developed by Blobbey", DialogLayout.Full)
    }
    
})
game.onUpdate(function on_on_update() {
    if (landing) {
        if (controller.A.isPressed()) {
            sprites.setDataBoolean(mySprite, "Landing Gear", true)
            animation.stopAnimation(animation.AnimationTypes.All, mySprite)
            animation.runImageAnimation(mySprite, [img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . 5 . . . . . . 
                                        . . a a a a a c c c c c c c c c c c f 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c a c c f c c c . . . 
                                        . a . . . . . . . . . . . . f f . . 5 . . . . . . 
                                        f . . . . . . . . . . . . . f f . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c a c c 5 c c c . . . 
                                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                                        f . . . . . . . . . . . . . f f . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c c 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 5 c c c c . . 
                                        . . c c c c c c c c c c c c c a c c c c c c . . . 
                                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                                        f . . . . . . . . . . . . . f f . . . . . . . . .
                    `, img`
                        . . a . . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a . . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a . . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a . . . . . . . . . . . . . . . . . . . 
                                        . . a a a a a c c c c c c c c c c c 5 6 6 6 . . . 
                                        . c c c c c c c c c c c c b b b a a 2 6 6 6 6 . . 
                                        . c c b b b c c c c c b b b b b b a 2 c c c c . . 
                                        . . c c c c c c c c c c c c c a c c 5 c c c . . . 
                                        . a . . . . . . . . . . . . f f . . . . . . . . . 
                                        f . . . . . . . . . . . . . f f . . . . . . . . .
                    `], 100, true)
        }
        
    }
    
    direction()
})
game.onUpdateInterval(1000, function on_update_interval() {
    
    if (flying) {
        statusbar.value += -1
        if (endless) {
            if (!crashed) {
                score += 1
                fancyText.setText(myTextSprite3, "Score: " + ("" + score))
            }
            
        }
        
    }
    
})
game.onUpdateInterval(randint(500, 1500), function on_update_interval2() {
    
    for (let value of tiles.getTilesByType(assets.tile`
        myTile7
    `)) {
        if (Math.percentChance(75)) {
            tiles.setTileAt(value, assets.tile`
                myTile13
            `)
        }
        
    }
    for (let value2 of tiles.getTilesByType(assets.tile`
        myTile13
    `)) {
        if (Math.percentChance(75)) {
            tiles.setTileAt(value2, assets.tile`
                myTile7
            `)
        }
        
    }
    if (wind) {
        if (endless) {
            windSprite = sprites.create(img`
                    . . . . . . . . . . 
                                    . a a a . 2 2 2 . . 
                                    . . . . a . . . 2 . 
                                    . . . . a 2 2 2 2 . 
                                    . . . . 2 2 2 2 2 . 
                                    . . . . 2 f f f 2 . 
                                    . . . . 2 f 2 2 2 . 
                                    . . . . 2 f f 2 2 . 
                                    . . . . 2 f 2 2 2 . 
                                    . . . . 2 2 2 2 2 .
                `, SpriteKind.Fuel)
            windSprite.vx = -50
        } else {
            if (Math.percentChance(50)) {
                windSprite = sprites.create(img`
                    b b b b b b b b b b
                `, SpriteKind.Wind)
            } else {
                windSprite = sprites.create(img`
                    1 1 1 1 1 1 1 1 1 1
                `, SpriteKind.Wind)
            }
            
            windSprite.vx = -75
        }
        
        tiles.placeOnRandomTile(windSprite, assets.tile`
            myTile9
        `)
        windSprite.lifespan = 55000
        if (weather2 == "Wind") {
            if (Math.percentChance(75)) {
                windSprite = sprites.create(img`
                        bbbbbbbbbb............................................................................................................................................
                                            ...............................................bbbbbbbbbb.............................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ...........................................................................................................1111111111.................................
                                            ......................................................................................................................................................
                                            ..........................................................................bbbbbbbbbb..................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ..................................................................................................................................bbbbbbbbbb..........
                                            ......................................................................................................................................................
                                            ................1111111111............................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                                            ......................................................................................................................................................
                    `, SpriteKind.Wind)
                tiles.placeOnRandomTile(windSprite, assets.tile`
                    myTile9
                `)
                windSprite.lifespan = 15000
                windSprite.vx = -75
            }
            
        }
        
    }
    
})
game.onUpdateInterval(30000, function on_update_interval3() {
    
    console.log("30000 game update")
    if (endless) {
        weather2 = ["Fog", "Rain", "Wind", "Clear"]._pickRandom()
    }
    
    if (wind) {
        if (weather2 == "Fog") {
            if (Math.percentChance(75)) {
                fog = true
                console.log("fog")
            } else {
                fog = false
            }
            
        }
        
        if (fog) {
            if (spriteutils.isDestroyed(fogSprite)) {
                achievements.create("You've flown into dense fog.")
                fogSprite = sprites.create(img`
                        . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . . 
                                            . . . . . . . . . . . . . . . .
                    `, SpriteKind.Fog)
                animation.runImageAnimation(fogSprite, [img`
                            b b b b b b b b b b b b b . . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b b . 
                                                b b b b b b b b b b b b b b b . 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b . . b 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b . . . 
                                                b b b b b b b b b b b b b . . . 
                                                b b b b b b b b b b b b b . . . 
                                                b b b b b b b b b b b b b . . . 
                                                b b b b b b b b b b b b b . . b 
                                                b b b b b b b b b b b b . . . . 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b . . . . b b b b b b b b . . b 
                                                . . . b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b . . . . . b b b b b b
                        `, img`
                            b . . . b b b b b b b b b b b b 
                                                . . . b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b . . b b b 
                                                b b b b b b b b b b b . . . b b 
                                                b b b b b b b b b b b . . . . b 
                                                b b b b b b b b b b b . . b b b 
                                                b b b b b b b b b b b . b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . b b b b b b b b b 
                                                b b b b b . . b b b b b b b b b
                        `, img`
                            b . b b b b b b b b b b b . . . 
                                                . b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b . . b b b 
                                                b b b b b b b b . . . . b b b b 
                                                b b b b b b b b . . . . b b b b 
                                                b b b b b b b b b . . b b b b b 
                                                . b b b b b b b b b b b b b b b 
                                                . b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b . b b 
                                                b b b b b b b b b b . . . . . b 
                                                b b b b b b b b b b b . . b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b . . b b b b b b 
                                                b b b b b b b b . b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b . . . b b b b b 
                                                b b b b b b b b . . b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b . b b b b b b b 
                                                b b b b b . . . . b b b b b b b 
                                                b b b b b . . . b b b b b b b b 
                                                b b b b b b b b b b b b b b b . 
                                                b b b b b b b b b b . . . . . . 
                                                b b b b b b b b b . . . . . . .
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b . b b b b b b b b 
                                                b b b b b b b b . b b b b b b b 
                                                b b b b b b b b . b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b . b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b . . . . . . . b b b 
                                                b b b b b b b . . . . . . . b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b . b b b b b b b b b b b b b 
                                                b b b . b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b b . . . b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b . . . . . . 
                                                b b b b b b b b b . . . . . . . 
                                                b b b b b b b b b . . . . . . b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b . b b b b b b b b b b b b b 
                                                b b b . b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b b . . . b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b . . . . . . 
                                                b b b b b b b b b . . . . . . . 
                                                b b b b b b b b b . . . . . . b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                . b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b . b b b b b b b b b 
                                                b b b b b b . b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b . . b b b b 
                                                b b b b b b b b b . . . b b b b 
                                                b b b b b b b b b . . . . . b b 
                                                b b b b b b . . . . . b b b b b 
                                                b b b b b . . . . b b b b b b b 
                                                . b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b . . b b b b b b b b 
                                                b b b b b b . b b b b b b b b b 
                                                b b b b b b . b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b . b b b b b b 
                                                b b b b b b b b b . . b b b b b 
                                                b b b b b . . . . . . b b b b b 
                                                b b b b . . . . . b b b b b b b 
                                                b b b b . . . . b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b . . . . b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b . . b b b b b b b b b b b 
                                                b b . . . . . b b b b b b b b b 
                                                b . . . . . b b b b b b b b b b 
                                                b b b b . . b b b b b b b b b b 
                                                b b b . b b b b b b b b b b b b 
                                                b b b b . b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b . . 
                                                b b b b b b b b b b b b b b . b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b . . b b b b b b b b b b b b 
                                                b . . . . . b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b . . b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b . . b 
                                                b b b b b b b b b b b b b b b b 
                                                . b b b b b b b b b b b b b b b 
                                                . . . b b b b b b b b b b b b b 
                                                b . . b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `, img`
                            b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b . b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b 
                                                b b b b b b b b b b b b b b b b
                        `], 200, true)
                fogSprite.changeScale(10, ScaleAnchor.Middle)
                fogSprite.z = 50
                fogSprite.setFlag(SpriteFlag.RelativeToCamera, true)
            }
            
        } else if (!spriteutils.isDestroyed(fogSprite)) {
            sprites.destroy(fogSprite)
        }
        
        if (weather2 == "Rain") {
            if (Math.percentChance(75)) {
                rain = true
                waves = true
                console.log("rain")
            } else {
                rain = false
                waves = false
            }
            
        }
        
        if (rain) {
            achievements.create("You've flown into a storm!")
            scroller.setLayerImage(scroller.BackgroundLayer.Layer1, img`
                    .................................................................................................................6................6.............................
                                    ..................................................................................................6..............6................6..........6..................
                                    .............6................6.......................6...................6.......................6..............6.......6........6..........6..................
                                    .............6................6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.........6..
                                    .............6.......6........6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.........6..
                                    ........6....6.......6........6..........6.....6......6.......6...........6....6..................6.........6............6.............6.....6.....6.........6..
                                    ........6....6.......6........6..........6.....6......6.......6...........6....6..........6.......6.........6............6.............6...........6.........6..
                                    ........6............6.............6.....6.....6......6.......6.......6........6..........6..........6......6............6.............6...........6.........6..
                                    ........6............6.............6...........6.........6....6.......6........6..........6.....6....6......6..................6.......6...........6.........6..
                                    .6......6............6.............6...........6.........6....6.......6........6..........6.....6....6..............6..........6.............................6..
                                    .6......6..................6.......6...........6.........6............6.............6.....6.....6....6..............6..........6.......................6........
                                    .6..............6..........6.............................6............6.............6...........6....6..............6..........6.......................6........
                                    .6..............6..........6......................6......6............6.............6...........6....6..............6..........6.......................6........
                                    .6..............6..........6......................6......6..................6.......6...........6...................6..................................6........
                                    .6..............6..........6......................6..............6..........6..........................................................................6........
                                    ................6.................................6..............6..........6.................................6............6.........6......6..........6........
                                    ..................................................6..............6..........6.................................6............6.........6......6..........6........
                                    ..........6............6.........6......6.........6..............6..........6.................................6............6.........6......6..........6........
                                    ..........6............6.........6......6........................6......................................6.....6............6.........6......6.....6....6....6...
                                    ..........6............6.........6......6...............................................................6.....6.............................6.....6.........6...
                                    ....6.....6............6.........6......6.....6............6............6.........6......6..............6...................................6.....6.........6...
                                    ....6.....6.............................6.....6............6............6.........6......6..............6...............6..........6..............6.........6...
                                    ....6...................................6.....6............6............6.........6......6..............6.......6.......6..........6..............6.........6...
                                    ....6...............6..........6..............6......6.....6............6.........6......6.....6........6.......6.......6..........6..............6.............
                                    ....6.......6.......6..........6..............6......6.....6.............................6.....6........6.......6.......6..........6............................
                                    ....6.......6.......6..........6..............6......6...................................6.....6................6.......6..........6............................
                                    ....6.......6.......6..........6.....................6...............6..........6..............6................6.......6.......................................
                                    ............6.......6..........6.....................6.......6.......6..........6..............6................6...............................................
                                    ............6.......6................................6.......6.......6..........6..............6.............................................6..................
                                    ............6........................................6.......6.......6..........6............................................................6............6.....
                                    ........................................6....................6.......6..........6............................................................6............6.....
                                    ........................................6....................6.......6.......................................................................6............6.....
                                    ........................................6....................6..........................................6................6...................6............6.....
                                    ........................................6................................................6..............6................6..........6.....................6.....
                                    ....6................6..................6....6...................6.......................6..............6.......6........6..........6.....................6.....
                                    ....6................6..........6.......6....6...................6.......................6.........6....6.......6........6..........6.....6.........6...........
                                    ....6.......6........6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.........6...........
                                    ....6.......6........6..........6.....6......6.......6...........6....6..................6.........6............6.............6.....6.....6.........6...........
                                    ....6.......6........6..........6.....6......6.......6...........6....6..........6.......6.........6............6.............6...........6.........6...........
                                    ............6.............6.....6.....6......6.......6.......6........6..........6..........6......6............6.............6...........6.........6...........
                                    ............6.............6...........6.........6....6.......6........6..........6.....6....6......6..................6.......6...........6.........6...........
                                    ............6.............6...........6.........6....6.......6........6..........6.....6....6..............6..........6.............................6...........
                                    ..................6.......6...........6.........6............6.............6.....6.....6....6..............6..........6.......................6.................
                                    .......6..........6.............................6............6.............6...........6....6..............6..........6.......................6.............6...
                                    .......6..........6......................6......6............6.............6...........6....6..............6..........6.......................6.............6...
                                    .......6..........6......................6......6..................6.......6...........6...................6..................................6.............6...
                                    .......6..........6......................6..............6..........6..........................................................................6.............6...
                                    .......6.................................6..............6..........6.................................6............6.........6......6..........6.............6...
                                    .........................................6..............6..........6.................................6............6.........6......6..........6.............6...
                                    .6............6.........6......6.........6..............6..........6.................................6............6.........6......6..........6.................
                                    .6............6.........6......6........................6......................................6.....6............6.........6......6.....6....6....6............
                                    .6............6.........6......6...............................................................6.....6.............................6.....6.........6............
                                    .6............6.........6......6.....6............6............6.........6......6..............6...................................6.....6.........6............
                                    .6.............................6.....6............6............6.........6......6..............6...............6..........6..............6.........6............
                                    ...............................6.....6............6............6.........6......6..............6.......6.......6..........6..............6.........6............
                                    ...........6..........6..............6......6.....6............6.........6......6.....6........6.......6.......6..........6..............6......................
                                    ...6.......6..........6..............6......6.....6.............................6.....6........6.......6.......6..........6.....................................
                                    ...6.......6..........6..............6......6...................................6.....6................6.......6..........6....6................................
                                    ...6.......6..........6.....................6...............6..........6..............6................6.......6...............6................6........6......
                                    ...6.......6..........6.....................6.......6.......6..........6..............6................6.......................6................6........6......
                                    ...6.......6...............6................6.......6.......6..........6..............6.....6..................................6................6........6......
                                    ...6.......................6................6.......6.......6..........6....................6..................................6................6........6......
                                    ...........................6........................6.......6..........6....................6..................................6................6........6......
                                    ...........................6........................6.......6...............................6..................................6................6........6......
                                    ...........................6........................6.......................................6.....................6................6.....................6......
                                    ...........................6.......................................................................6..............6................6..........6.................
                                    ..............6............6...6.......................6...................6.......................6..............6.......6........6..........6.................
                                    ..............6................6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.........6.
                                    ..............6.......6........6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.........6.
                                    .........6....6.......6........6..........6.....6......6.......6...........6....6..................6.........6............6.............6.....6.....6.........6.
                                    .........6....6.......6........6..........6.....6......6.......6...........6....6..........6.......6.........6............6.............6...........6.........6.
                                    .........6............6.............6.....6.....6......6.......6.......6........6..........6..........6......6............6.............6...........6.........6.
                                    .........6............6.............6...........6.........6....6.......6........6..........6.....6....6......6..................6.......6...........6.........6.
                                    ..6......6............6.............6...........6.........6....6.......6........6..........6.....6....6..............6..........6.............................6.
                                    ..6......6..................6.......6...........6.........6............6.............6.....6.....6....6..............6..........6.......................6.......
                                    ..6..............6..........6.............................6............6.............6...........6....6..............6..........6.......................6.......
                                    ..6..............6..........6......................6......6............6.............6...........6....6..............6..........6.......................6.......
                                    ..6..............6..........6......................6......6..................6.......6...........6...................6..................................6.......
                                    ..6..............6..........6......................6..............6..........6..........................................................................6.......
                                    .................6.................................6..............6..........6.................................6............6.........6......6..........6.......
                                    ...................................................6..............6..........6.................................6............6.........6......6..........6.......
                                    ...........6............6.........6......6.........6..............6..........6.................................6............6.........6......6..........6.......
                                    ...........6............6.........6......6........................6......................................6.....6............6.........6......6.....6....6....6..
                                    ...........6............6.........6......6...............................................................6.....6.............................6.....6.........6..
                                    .....6.....6............6.........6......6.....6............6............6.........6......6..............6...................................6.....6.........6..
                                    .....6.....6.............................6.....6............6............6.........6......6..............6...............6..........6..............6.........6..
                                    .....6...................................6.....6............6............6.........6......6..............6.......6.......6..........6..............6.........6..
                                    .....6...............6..........6..............6......6.....6............6.........6......6.....6........6.......6.......6..........6..............6............
                                    .....6.......6.......6..........6..............6......6.....6.............................6.....6........6.......6.......6..........6...........................
                                    .....6.......6.......6..........6..............6......6...................................6.....6................6.......6..........6...........................
                                    .....6.......6.......6..........6.....................6...............6..........6..............6................6.......6......................................
                                    .............6.......6..........6.....................6.......6.......6..........6..............6................6.........................6....................
                                    .............6.......6................................6.......6.......6..........6..............6..........................................6....................
                                    6............6........................................6.......6.......6..........6.........................................................6....................
                                    6.............................................................6.......6..........6.........................................................6..................6.
                                    6.............................................................6.......6....................................................................6..................6.
                                    6.............................................................6.....................................................6................6........................6.
                                    6....................................................................................................6..............6................6..........6.............6.
                                    6...............6................6.......................6...................6.......................6..............6.......6........6..........6.............6.
                                    ................6................6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.......6.
                                    ................6.......6........6..........6............6...................6.......................6.........6....6.......6........6..........6.....6.......6.
                                    ...........6....6.......6........6..........6.....6......6.......6...........6....6..................6.........6............6.............6.....6.....6.........
                                    ...........6....6.......6........6..........6.....6......6.......6...........6....6..........6.......6.........6............6.............6...........6.........
                                    ...........6............6.............6.....6.....6......6.......6.......6........6..........6..........6......6............6.............6...........6.........
                                    ...........6............6.............6...........6.........6....6.......6........6..........6.....6....6......6..................6.......6...........6.........
                                    ....6......6............6.............6...........6.........6....6.......6........6..........6.....6....6..............6..........6.............................
                                    ....6......6..................6.......6...........6.........6............6.............6.....6.....6....6..............6..........6.......................6.....
                                    ....6..............6..........6.............................6............6.............6...........6....6..............6..........6.......................6.....
                                    ....6..............6..........6......................6......6............6.............6...........6....6..............6..........6.......................6.....
                                    ....6..............6..........6......................6......6..................6.......6...........6...................6..................................6.....
                                    ....6..............6..........6......................6..............6..........6..........................................................................6.....
                                    ...................6.................................6..............6..........6.................................6............6.........6......6..........6.....
                                    .....................................................6..............6..........6.................................6............6.........6......6..........6.....
                                    .............6............6.........6......6.........6..............6..........6.................................6............6.........6......6..........6.....
                                    .............6............6.........6......6........................6......................................6.....6............6.........6......6.....6....6....6
                                    .............6............6.........6......6...............................................................6.....6.............................6.....6.........6
                                    .......6.....6............6.........6......6.....6............6............6.........6......6..............6...................................6.....6.........6
                                    .......6.....6.............................6.....6............6............6.........6......6..............6...............6..........6..............6.........6
                                    .......6...................................6.....6............6............6.........6......6..............6...............6..........6..............6.........6
                                    .......6.........................................6............6............6.........6......6..............6...............6..........6..............6..........
                `)
            scroller.scrollBackgroundWithSpeed(0, 75, scroller.BackgroundLayer.Layer1)
            mySprite.ay = 5
        } else {
            scroller.setLayerImage(scroller.BackgroundLayer.Layer1, img`
                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                                    ................................................................................................................................................................
                `)
            mySprite.ay = 0
        }
        
        if (weather2 == "Wind") {
            waves = true
            console.log("wind")
        }
        
    }
    
})
game.onUpdateInterval(randint(3000, 4000), function on_update_interval4() {
    
    if (waves) {
        if (tiles.getTilesByType(assets.tile`
            myTile15
        `).length == 1) {
            waveSprite = sprites.create(img`
                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    .........8119...........
                                    .......8889998..........
                                    ......88998811..........
                                    .....8998888818.........
                                    .....9968888811.........
                                    ....996889888811........
                                    ....9688988888818.......
                                    ...996898888888888......
                                    ..89699888888888888.....
                                    ..898988888888888888....
                                    .86898888888888888888...
                                    .6889888888888888888888.
                                    888888888888888888888888
                `, SpriteKind.Wave)
            tiles.placeOnRandomTile(waveSprite, assets.tile`
                myTile15
            `)
            waveSprite.vx = -75
        }
        
    }
    
})
