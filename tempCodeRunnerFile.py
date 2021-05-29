    if key_pressed[pygame.K_UP]:
                
                move(zeMap.getMapPath(), mapImage, player, 0, root, player_face_loaded, player_walk_loaded)
            
            elif key_pressed[pygame.K_LEFT]:
                
                move(zeMap.getMapPath(), mapImage, player, 1, root, player_face_loaded, player_walk_loaded)


            elif key_pressed[pygame.K_RIGHT]:
                
                move(zeMap.getMapPath(), mapImage, player, 2, root, player_face_loaded, player_walk_loaded)

            if key_pressed[pygame.K_DOWN]:

                move(zeMap.getMapPath(), mapImage, player, 3, root, player_face_loaded, player_walk_loaded)