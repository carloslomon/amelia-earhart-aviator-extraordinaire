@namespace
class SpriteKind:
    Screen = SpriteKind.create()
    Wind = SpriteKind.create()
    Fog = SpriteKind.create()
    Wave = SpriteKind.create()
    Obsolete = SpriteKind.create()
    Fuel = SpriteKind.create()
@namespace
class StatusBarKind:
    Fuel2 = StatusBarKind.create()

def on_hit_wall(sprite, location):
    global wind, callDirection
    if mySprite.is_hitting_tile(CollisionDirection.RIGHT):
        if takeoff:
            end_with("You've reached the end of the runway.")
    elif mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        if sprites.read_data_boolean(mySprite, "Landing Gear"):
            wind = False
            callDirection = False
            scroller.scroll_background_with_speed(-10, 0)
            if landing:
                mySprite.set_velocity(45, 0)
                
                def on_after():
                    if circumnavigation:
                        if blockSettings.read_number("Level") < 7:
                            blockSettings.write_number("Level", blockSettings.read_number("Level") + 1)
                            end_with("A successful landing! You have " + str((8 - blockSettings.read_number("Level"))) + " more flights left in your circumnavigation trip.")
                        elif blockSettings.read_number("Level") == 7:
                            levelImages[selectedFlight] = img("""
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
                            """)
                            blockSettings.write_image_array("Levels", levelImages)
                            blockSettings.write_number("Level", 0)
                            end_with("Congratulations, you've made it to Howland Island and have completed what Amelia Earhart could not!")
                    else:
                        levelImages[selectedFlight] = img("""
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
                        """)
                        if levelImages[selectedFlight + 1].equals(img("""
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
                        """)):
                            levelImages[selectedFlight + 1] = img("""
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
                            """)
                        blockSettings.write_image_array("Levels", levelImages)
                        end_with("A successful landing! Congratulations!")
                timer.after(2500, on_after)
                
        else:
            if landing:
                scene.camera_shake(2, 500)
                
                def on_after2():
                    end_with("That was definitely unnecessary. Was it really that hard to deploy the landing gear???")
                timer.after(1000, on_after2)
                
            else:
                if wind:
                    if statusbar.value > 0:
                        scene.camera_shake(2, 500)
                        mySprite.ay = 250
                        
                        def on_after3():
                            end_with("You crash landed! I hope you had a good reason for this!")
                        timer.after(1000, on_after3)
                        
                    else:
                        outOfFuelCrash()
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def loading(time: number):
    global blackScreen, myTextSprite2
    blackScreen = sprites.create(image.create(160, 120), SpriteKind.Screen)
    blackScreen.set_position(80, 60)
    blackScreen.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    blackScreen.image.fill(15)
    blackScreen.z = 100
    myTextSprite2 = fancyText.create("Loading...", 75, 1, fancyText.default_arcade)
    myTextSprite2.z = 101
    myTextSprite2.set_position(80, 60)
    myTextSprite2.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    pause(time)
    sprites.destroy(blackScreen)
    sprites.destroy(myTextSprite2)

def on_overlap_tile(sprite2, location2):
    tree_crash()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile22
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite3, location3):
    global crashed, wind, callDirection
    if endless:
        if score > blockSettings.read_number("High Score"):
            blockSettings.write_number("High Score", score)
            
            def on_after4():
                end_with("New high score!")
            timer.after(4000, on_after4)
            
    if statusbar.value > 0:
        if not (crashed):
            crashed = True
            wind = False
            callDirection = False
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            scene.camera_shake(2, 500)
            tiles.place_on_tile(mySprite,
                location3.get_neighboring_location(CollisionDirection.TOP))
            controller.move_sprite(mySprite, 0, 0)
            mySprite.set_velocity(1, 5)
            scroller.scroll_background_with_speed(-5, 0, scroller.BackgroundLayer.LAYER0)
            mySprite.start_effect(effects.fountain, 1000)
            
            def on_after5():
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            timer.after(7500, on_after5)
            
    else:
        outOfFuelCrash()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile13
    """),
    on_overlap_tile2)

def on_a_pressed():
    global takeoff
    if takeoff:
        mySprite.vx += 3
        scroll_background()
        if mySprite.vx >= 118:
            mySprite.vy += -6
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            animation.run_image_animation(mySprite,
                [img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """)],
                100,
                True)
            takeoff = False
            
            def on_after6():
                global callDirection
                callDirection = True
            timer.after(8250, on_after6)
            
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite4, location4):
    global crashed, wind, callDirection
    if endless:
        if score > blockSettings.read_number("High Score"):
            blockSettings.write_number("High Score", score)
            
            def on_after7():
                end_with("New high score!")
            timer.after(4000, on_after7)
            
    if statusbar.value > 0:
        if not (crashed):
            crashed = True
            wind = False
            callDirection = False
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            scene.camera_shake(2, 500)
            tiles.place_on_tile(mySprite,
                location4.get_neighboring_location(CollisionDirection.TOP))
            controller.move_sprite(mySprite, 0, 0)
            mySprite.set_velocity(1, 5)
            scroller.scroll_background_with_speed(-5, 0, scroller.BackgroundLayer.LAYER0)
            mySprite.start_effect(effects.fountain, 1000)
            
            def on_after8():
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            timer.after(7500, on_after8)
            
    else:
        outOfFuelCrash()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile7
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite5, location5):
    if not (takeoff):
        flight("Fog", timems, 0, terrain2, "Grass")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite6, location6):
    tiles.place_on_tile(mySprite,
        tiles.get_tile_location(20, mySprite.tilemap_location().row))
    scene.camera_follow_sprite(mySprite)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite7, location7):
    tiles.set_tile_at(location7, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile6)

def flight(weather: str, time2: number, airfield: number, terrain: str, landingAirfield: str):
    global flying, wind
    weather = weather
    mySprite.set_velocity(100, 0)
    scroller.scroll_background_with_speed(-105, 0)
    if terrain == "Ocean":
        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
            sky
        """)))
    elif terrain == "Land":
        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
            level25
        """)))
    elif terrain == "Desert":
        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
            level29
        """)))
    elif terrain == "Jungle":
        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
            level71
        """)))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        start
    """))
    animation.run_image_animation(mySprite,
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)],
        100,
        False)
    
    def on_after9():
        animation.run_image_animation(mySprite,
            [img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """),
                img("""
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
                """)],
            200,
            True)
    timer.after(750, on_after9)
    
    flying = True
    fuel_bar(250)
    controller.move_sprite(mySprite, 0, 30)
    wind = True
    if weather == "Clouds":
        pass
    elif weather == "Fog":
        pass
    elif weather == "Rain":
        pass
    
    def on_after10():
        nonlocal weather
        global fog, rain, waves, wind, flying
        if not (crashed):
            weather = "N/A"
            fog = False
            rain = False
            waves = False
            wind = False
            flying = False
            controller.move_sprite(mySprite, 0, 0)
            sprites.destroy_all_sprites_of_kind(SpriteKind.Wind)
            sprites.destroy_all_sprites_of_kind(SpriteKind.Fog)
            sprites.destroy_all_sprites_of_kind(SpriteKind.Wave)
            sprites.set_data_boolean(mySprite, "Landing Gear", False)
            achievements.create("You are landing. Press 'A' to deploy landing gear.")
            animation.run_image_animation(mySprite,
                [img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """)],
                100,
                False)
            if landingAirfield == "Grass":
                tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                    level33
                """)))
            tiles.place_on_random_tile(mySprite, assets.tile("""
                myTile10
            """))
            scroller.scroll_background_with_speed(-55, 0)
            mySprite.set_velocity(50, 10)
            
            def on_after11():
                global landing
                animation.run_image_animation(mySprite,
                    [img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """)],
                    100,
                    True)
                landing = True
            timer.after(300, on_after11)
            
    timer.after(time2, on_after10)
    

def on_overlap_tile7(sprite8, location8):
    tree_crash()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile29
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite9, location9):
    if not (takeoff):
        flight("Wind", timems, 1, terrain2, "Grass")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile17
    """),
    on_overlap_tile8)

def on_on_overlap(sprite10, otherSprite):
    if not (crashed):
        sprites.destroy(otherSprite)
        statusbar.value += 5
sprites.on_overlap(SpriteKind.player, SpriteKind.Fuel, on_on_overlap)

def tree_crash():
    global crashed, wind, callDirection
    if not (crashed):
        crashed = True
        wind = False
        callDirection = False
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
        scene.camera_shake(2, 500)
        controller.move_sprite(mySprite, 0, 0)
        mySprite.set_velocity(30, 40)
        mySprite.start_effect(effects.fire, 1000)
        
        def on_after12():
            if statusbar.value > 0:
                end_with("You crashed into a tree. This probably could've been avoided.")
            else:
                end_with("I'm going to assume you tried your best...")
        timer.after(7500, on_after12)
        

def on_overlap_tile9(sprite11, location10):
    tiles.set_tile_at(location10, assets.tile("""
        transparency16
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile9)

def scroll_background():
    scroller.scroll_background_with_speed(mySprite.vx / 2 * -1 - 5, 0, scroller.BackgroundLayer.LAYER0)
def fuel_bar(fuel: number):
    global statusbar
    statusbar = statusbars.create(50, 6, StatusBarKind.Fuel2)
    statusbar.max = fuel
    statusbar.value = fuel
    statusbar.set_color(4, 0, 2)
    statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    statusbar.set_label("Fuel", 15)
    statusbar.set_position(39, 6)
    statusbar.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
def end_with(message: str):
    game.set_dialog_frame(img("""
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
    """))
    game.set_dialog_cursor(img("""
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
    """))
    game.show_long_text(message, DialogLayout.FULL)
    game.reset()

def on_status_reached_comparison_eq_type_percentage(status):
    global crashed, wind
    if not (crashed):
        crashed = True
        wind = False
        controller.move_sprite(mySprite, 0, 0)
        mySprite.ay = 1
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
        
        def on_background():
            Notification.notify("You've run out of fuel... This won't end well.", 5)
        timer.background(on_background)
        
statusbars.on_status_reached(StatusBarKind.Fuel2,
    statusbars.StatusComparison.EQ,
    statusbars.ComparisonType.PERCENTAGE,
    0,
    on_status_reached_comparison_eq_type_percentage)

def outOfFuelCrash():
    global callDirection
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    scene.camera_shake(2, 500)
    callDirection = False
    mySprite.set_velocity(1, 4)
    scroller.scroll_background_with_speed(-5, 0, scroller.BackgroundLayer.LAYER0)
    
    def on_after13():
        mySprite.set_velocity(0, 0)
        mySprite.set_kind(SpriteKind.Obsolete)
        end_with("Ouch. If only you had more fuel...")
    timer.after(5000, on_after13)
    

def on_on_overlap2(sprite12, otherSprite2):
    global crashed, wind, callDirection
    if endless:
        if score > blockSettings.read_number("High Score"):
            blockSettings.write_number("High Score", score)
            
            def on_after14():
                end_with("New high score!")
            timer.after(4000, on_after14)
            
    if statusbar.value > 0:
        if not (crashed):
            crashed = True
            wind = False
            callDirection = False
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            scene.camera_shake(2, 500)
            controller.move_sprite(mySprite, 0, 0)
            mySprite.set_velocity(1, 5)
            scroller.scroll_background_with_speed(-5, 0, scroller.BackgroundLayer.LAYER0)
            mySprite.start_effect(effects.fountain, 1000)
            
            def on_after15():
                end_with("You've crash landed in the ocean. I hope this wasn't on purpose!")
            timer.after(7500, on_after15)
            
    else:
        outOfFuelCrash()
sprites.on_overlap(SpriteKind.Wave, SpriteKind.player, on_on_overlap2)

def start(airfield2: str):
    global takeoff
    loading(randint(1000, 2500))
    story.set_sound_enabled(False)
    story.print_text(airfield2,
        mySprite.x - 5,
        mySprite.y - 100,
        1,
        15,
        story.TextSpeed.SLOW)
    story.print_text("Spam 'A' to take off.",
        mySprite.x - 5,
        mySprite.y - 100,
        1,
        15,
        story.TextSpeed.SLOW)
    mySprite.ay = 0
    takeoff = True
    animation.run_image_animation(mySprite,
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)],
        100,
        True)

def on_hit_wall2(sprite13, location11):
    sprites.destroy(sprite13)
scene.on_hit_wall(SpriteKind.Wave, on_hit_wall2)

def direction():
    if callDirection:
        if mySprite.vy < 0:
            CustomLives.lose_life()
            CustomLives.set_life_image_and_max(img("""
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
                """),
                1,
                0)
            CustomLives.set_life_position(155, 7)
            scroller.scroll_background_with_speed(-105, 10)
        elif mySprite.vy > 0:
            CustomLives.lose_life()
            CustomLives.set_life_image_and_max(img("""
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
                """),
                1,
                0)
            CustomLives.set_life_position(155, 7)
            scroller.scroll_background_with_speed(-105, -10)
        else:
            CustomLives.lose_life()
            scroller.scroll_background_with_speed(-105, 0)

def on_overlap_tile10(sprite14, location12):
    if not (takeoff):
        flight("Rain", timems, 1, terrain2, "Grass")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile14
    """),
    on_overlap_tile10)

def on_on_overlap3(sprite15, otherSprite3):
    statusbar.value += -1
sprites.on_overlap(SpriteKind.player, SpriteKind.Wind, on_on_overlap3)

def on_overlap_tile11(sprite16, location13):
    tree_crash()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile28
    """),
    on_overlap_tile11)

waveSprite: Sprite = None
fogSprite: Sprite = None
windSprite: Sprite = None
waves = False
rain = False
fog = False
myTextSprite2: fancyText.TextSprite = None
blackScreen: Sprite = None
statusbar: StatusBarSprite = None
myTextSprite3: fancyText.TextSprite = None
score = 0
chosenFlight = 0
landingAirfield2 = ""
weather2 = ""
terrain2 = ""
timems = 0
selectedFlight = 0
myMenu2: miniMenu.MenuSprite = None
mySprite: Sprite = None
levelImages: List[Image] = []
callDirection = False
circumnavigation = False
wind = False
flying = False
crashed = False
endless = False
landing = False
takeoff = False
print("game started")
takeoff = False
landing = False
endless = False
crashed = False
flying = False
wind = False
circumnavigation = False
callDirection = False
if not (blockSettings.exists("High Score")):
    blockSettings.write_number("High Score", 0)
if not (blockSettings.exists("Levels")):
    blockSettings.write_image_array("Levels",
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)])
levelImages = blockSettings.read_image_array("Levels")
if not (blockSettings.exists("Level")):
    blockSettings.write_number("Level", 0)
myTextSprite = fancyText.create("Amelia Earhart: Aviator Extraordinaire",
    200,
    11,
    fancyText.serif_small)
myTextSprite.set_position(105, 15)
myTextSprite = fancyText.create("Amelia Earhart: Aviator Extraordinaire",
    200,
    12,
    fancyText.serif_small)
myTextSprite.set_position(106, 15)
scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
    img("""
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
    """))
scroller.scroll_background_with_speed(-50, 0)
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
animation.run_image_animation(mySprite,
    [img("""
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
        """),
        img("""
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
        """),
        img("""
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
        """),
        img("""
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
        """)],
    250,
    True)
mySprite.set_position(80, 50)
myMenu = miniMenu.create_menu(miniMenu.create_menu_item("Flights"),
    miniMenu.create_menu_item("Endless"),
    miniMenu.create_menu_item("Credits"))
myMenu.set_dimensions(160, 50)
myMenu.set_style_property(miniMenu.StyleKind.SELECTED,
    miniMenu.StyleProperty.BACKGROUND,
    images.color_block(15))
myMenu.set_style_property(miniMenu.StyleKind.DEFAULT,
    miniMenu.StyleProperty.BACKGROUND,
    images.color_block(11))
myMenu.set_style_property(miniMenu.StyleKind.ALL, miniMenu.StyleProperty.BORDER, 1)
myMenu.set_style_property(miniMenu.StyleKind.ALL,
    miniMenu.StyleProperty.BORDER_COLOR,
    images.color_block(12))
myMenu.set_position(80, 103)

def on_button_pressed(selection, selectedIndex):
    global myMenu2, score, flying, wind, endless, callDirection, myTextSprite3
    if selection == "Flights":
        myMenu.close()
        sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
        sprites.destroy_all_sprites_of_kind(myTextSprite.kind())
        myMenu2 = miniMenu.create_menu(miniMenu.create_menu_item("Harbour Grace, Newfoundland to Londonderry, Northern Ireland",
                levelImages[0]),
            miniMenu.create_menu_item("Honolulu, Hawai'i to Oakland, California", levelImages[1]),
            miniMenu.create_menu_item("Los Angeles, California to Mexico City, Mexico",
                levelImages[2]),
            miniMenu.create_menu_item("Circumnavigation: Flight " + str((blockSettings.read_number("Level") + 1)),
                levelImages[3]),
            miniMenu.create_menu_item("Cancel"))
        myMenu2.set_title("Flights")
        myMenu2.set_dimensions(160, 120)
        myMenu2.set_style_property(miniMenu.StyleKind.SELECTED,
            miniMenu.StyleProperty.BACKGROUND,
            images.color_block(15))
        myMenu2.set_style_property(miniMenu.StyleKind.DEFAULT,
            miniMenu.StyleProperty.BACKGROUND,
            images.color_block(11))
        myMenu2.set_style_property(miniMenu.StyleKind.DEFAULT_AND_SELECTED,
            miniMenu.StyleProperty.BORDER,
            2)
        myMenu2.set_style_property(miniMenu.StyleKind.DEFAULT_AND_SELECTED,
            miniMenu.StyleProperty.BORDER_COLOR,
            images.color_block(12))
        myMenu2.set_style_property(miniMenu.StyleKind.TITLE,
            miniMenu.StyleProperty.BORDER_COLOR,
            images.color_block(11))
        myMenu2.set_position(80, 60)
        
        def on_button_pressed2(selection2, selectedIndex2):
            global selectedFlight, circumnavigation, chosenFlight
            selectedFlight = selectedIndex2
            scroller.scroll_background_with_speed(-5, 0, scroller.BackgroundLayer.LAYER0)
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            mySprite.set_image(img("""
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
            """))
            if selectedIndex2 == 0:
                
                def on_background2():
                    global timems, terrain2, weather2, landingAirfield2
                    myMenu2.close()
                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                    tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                        harbourgrace
                    """)))
                    tiles.place_on_random_tile(mySprite, assets.tile("""
                        myTile3
                    """))
                    scene.camera_follow_sprite(mySprite)
                    mySprite.ay = 500
                    scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                        img("""
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
                        """))
                    timems = 90000
                    terrain2 = "Ocean"
                    weather2 = "Fog"
                    landingAirfield2 = "Grass"
                timer.background(on_background2)
                
                start("Harbour Grace, Newfoundland")
            elif selectedIndex2 == 1:
                if levelImages[1].equals(img("""
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
                """)) or levelImages[1].equals(img("""
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
                """)):
                    
                    def on_background3():
                        global timems, terrain2, weather2, landingAirfield2
                        myMenu2.close()
                        sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                            level38
                        """)))
                        tiles.place_on_random_tile(mySprite, assets.tile("""
                            myTile3
                        """))
                        scene.camera_follow_sprite(mySprite)
                        mySprite.ay = 500
                        scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                            img("""
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
                            """))
                        timems = 85000
                        terrain2 = "Ocean"
                        weather2 = "Rain"
                        landingAirfield2 = "Grass"
                    timer.background(on_background3)
                    
                    start("Honolulu, Hawai'i")
            elif selectedIndex2 == 2:
                if levelImages[2].equals(img("""
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
                """)) or levelImages[2].equals(img("""
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
                """)):
                    
                    def on_background4():
                        global timems, terrain2, weather2, landingAirfield2
                        myMenu2.close()
                        sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                            level48
                        """)))
                        tiles.place_on_random_tile(mySprite, assets.tile("""
                            myTile3
                        """))
                        scene.camera_follow_sprite(mySprite)
                        mySprite.ay = 500
                        scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                            img("""
                                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
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
                            """))
                        timems = 80000
                        terrain2 = "Desert"
                        weather2 = "Wind"
                        landingAirfield2 = "Desert"
                    timer.background(on_background4)
                    
                    start("Los Angeles, California")
            elif selectedIndex2 == 3:
                if levelImages[3].equals(img("""
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
                """)) or levelImages[3].equals(img("""
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
                """)):
                    myMenu2.close()
                    sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                    circumnavigation = True
                    if levelImages[3].equals(img("""
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
                    """)):
                        chosenFlight = game.ask_for_number("Which flight do you want to do? 1-8", 1)
                        if Math.if_number_is_between_inputs(chosenFlight, 0, 8):
                            blockSettings.write_number("Level", chosenFlight - 1)
                        else:
                            end_with("Invalid flight.")
                    if blockSettings.read_number("Level") == 0:
                        
                        def on_background5():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level54
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 85000
                            terrain2 = "Land"
                            weather2 = "Wind"
                            landingAirfield2 = "Grass"
                        timer.background(on_background5)
                        
                        start("Oakland, California")
                    elif blockSettings.read_number("Level") == 1:
                        
                        def on_background6():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level54
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 75000
                            terrain2 = "Ocean"
                            weather2 = "Fog"
                            landingAirfield2 = "Grass"
                        timer.background(on_background6)
                        
                        start("Miami, Florida")
                    elif blockSettings.read_number("Level") == 2:
                        
                        def on_background7():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level38
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 70000
                            terrain2 = "Jungle"
                            weather2 = "Rain"
                            landingAirfield2 = "Grass"
                        timer.background(on_background7)
                        
                        start("Caripito, Venezuela")
                    elif blockSettings.read_number("Level") == 3:
                        
                        def on_background8():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level38
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 80000
                            terrain2 = "Ocean"
                            weather2 = "Wind"
                            landingAirfield2 = "Desert"
                        timer.background(on_background8)
                        
                        start("Natal, Brazil")
                    elif blockSettings.read_number("Level") == 4:
                        
                        def on_background9():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level65
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                                                                    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
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
                                """))
                            timems = 90000
                            terrain2 = "Desert"
                            weather2 = "Clear"
                            landingAirfield2 = "Desert"
                        timer.background(on_background9)
                        
                        start("Dakar, Senegal")
                    elif blockSettings.read_number("Level") == 5:
                        
                        def on_background10():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level65
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 80000
                            terrain2 = "Land"
                            weather2 = "Storm"
                            landingAirfield2 = "Grass"
                        timer.background(on_background10)
                        
                        start("Karachi, Pakistan")
                    elif blockSettings.read_number("Level") == 6:
                        
                        def on_background11():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level38
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 75000
                            terrain2 = "Ocean"
                            weather2 = "Storm"
                            landingAirfield2 = "Grass"
                        timer.background(on_background11)
                        
                        start("Bangkok, Thailand")
                    elif blockSettings.read_number("Level") == 7:
                        
                        def on_background12():
                            global timems, terrain2, weather2, landingAirfield2
                            myMenu2.close()
                            sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
                            tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
                                level38
                            """)))
                            tiles.place_on_random_tile(mySprite, assets.tile("""
                                myTile3
                            """))
                            scene.camera_follow_sprite(mySprite)
                            mySprite.ay = 500
                            scroller.set_layer_image(scroller.BackgroundLayer.LAYER0,
                                img("""
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
                                """))
                            timems = 90000
                            terrain2 = "Ocean"
                            weather2 = "Wind"
                            landingAirfield2 = "Grass"
                        timer.background(on_background12)
                        
                        start("Lae, Papa New Guinea")
            else:
                game.reset()
        myMenu2.on_button_pressed(controller.A, on_button_pressed2)
        
    elif selection == "Endless":
        myMenu.close()
        sprites.destroy_all_sprites_of_kind(SpriteKind.mini_menu)
        sprites.destroy_all_sprites_of_kind(myTextSprite.kind())
        game.set_dialog_frame(img("""
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
        """))
        game.set_dialog_cursor(img("""
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
        """))
        game.show_long_text("Collect fuel in order to stay in the air! High score: " + str(blockSettings.read_number("High Score")),
            DialogLayout.FULL)
        score = 0
        flying = True
        wind = True
        endless = True
        callDirection = True
        controller.move_sprite(mySprite, 0, 30)
        scene.camera_follow_sprite(mySprite)
        tiles.set_current_tilemap(tileUtil.create_small_map(tilemap("""
            sky
        """)))
        mySprite.set_velocity(100, 0)
        scroller.scroll_background_with_speed(-105, 0)
        fuel_bar(25)
        myTextSprite3 = fancyText.create("Score: " + str(score), 100, 15, fancyText.default_arcade)
        myTextSprite3.set_position(5, 113)
        myTextSprite3.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    elif selection == "Credits":
        game.set_dialog_frame(img("""
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
        """))
        game.set_dialog_cursor(img("""
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
        """))
        game.show_long_text("Developed by Blobbey", DialogLayout.FULL)
myMenu.on_button_pressed(controller.A, on_button_pressed)

def on_on_update():
    if landing:
        if controller.A.is_pressed():
            sprites.set_data_boolean(mySprite, "Landing Gear", True)
            animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
            animation.run_image_animation(mySprite,
                [img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """),
                    img("""
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
                    """)],
                100,
                True)
    direction()
game.on_update(on_on_update)

def on_update_interval():
    global score
    if flying:
        statusbar.value += -1
        if endless:
            if not (crashed):
                score += 1
                fancyText.set_text(myTextSprite3, "Score: " + str(score))
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global windSprite
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile7
    """)):
        if Math.percent_chance(75):
            tiles.set_tile_at(value, assets.tile("""
                myTile13
            """))
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile13
    """)):
        if Math.percent_chance(75):
            tiles.set_tile_at(value2, assets.tile("""
                myTile7
            """))
    if wind:
        if endless:
            windSprite = sprites.create(img("""
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
                """),
                SpriteKind.Fuel)
            windSprite.vx = -50
        else:
            if Math.percent_chance(50):
                windSprite = sprites.create(img("""
                    b b b b b b b b b b
                """), SpriteKind.Wind)
            else:
                windSprite = sprites.create(img("""
                    1 1 1 1 1 1 1 1 1 1
                """), SpriteKind.Wind)
            windSprite.vx = -75
        tiles.place_on_random_tile(windSprite, assets.tile("""
            myTile9
        """))
        windSprite.lifespan = 55000
        if weather2 == "Wind":
            if Math.percent_chance(75):
                windSprite = sprites.create(img("""
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
                    """),
                    SpriteKind.Wind)
                tiles.place_on_random_tile(windSprite, assets.tile("""
                    myTile9
                """))
                windSprite.lifespan = 15000
                windSprite.vx = -75
game.on_update_interval(randint(500, 1500), on_update_interval2)

def on_update_interval3():
    global weather2, fog, fogSprite, rain, waves
    print("30000 game update")
    if endless:
        weather2 = ["Fog", "Rain", "Wind", "Clear"]._pick_random()
    if wind:
        if weather2 == "Fog":
            if Math.percent_chance(75):
                fog = True
                print("fog")
            else:
                fog = False
        if fog:
            if spriteutils.is_destroyed(fogSprite):
                achievements.create("You've flown into dense fog.")
                fogSprite = sprites.create(img("""
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
                    """),
                    SpriteKind.Fog)
                animation.run_image_animation(fogSprite,
                    [img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """),
                        img("""
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
                        """)],
                    200,
                    True)
                fogSprite.change_scale(10, ScaleAnchor.MIDDLE)
                fogSprite.z = 50
                fogSprite.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
        else:
            if not (spriteutils.is_destroyed(fogSprite)):
                sprites.destroy(fogSprite)
        if weather2 == "Rain":
            if Math.percent_chance(75):
                rain = True
                waves = True
                print("rain")
            else:
                rain = False
                waves = False
        if rain:
            achievements.create("You've flown into a storm!")
            scroller.set_layer_image(scroller.BackgroundLayer.LAYER1,
                img("""
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
                """))
            scroller.scroll_background_with_speed(0, 75, scroller.BackgroundLayer.LAYER1)
            mySprite.ay = 5
        else:
            scroller.set_layer_image(scroller.BackgroundLayer.LAYER1,
                img("""
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
                """))
            mySprite.ay = 0
        if weather2 == "Wind":
            waves = True
            print("wind")
game.on_update_interval(30000, on_update_interval3)

def on_update_interval4():
    global waveSprite
    if waves:
        if len(tiles.get_tiles_by_type(assets.tile("""
            myTile15
        """))) == 1:
            waveSprite = sprites.create(img("""
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
                """),
                SpriteKind.Wave)
            tiles.place_on_random_tile(waveSprite, assets.tile("""
                myTile15
            """))
            waveSprite.vx = -75
game.on_update_interval(randint(3000, 4000), on_update_interval4)
