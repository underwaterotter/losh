import pygame,os,blockdata,spritestor

mtblock_list = pygame.sprite.Group()

mtplatforms = pygame.sprite.Group()

mtall_sprites_list = pygame.sprite.Group()

def create_level(mtblock_list,mtall_sprites_list,mtplatforms):
#---LEVEL---#
    
    #bottom platform left
    for bp_x in range(50,250,50):
        bp_y = 550
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockr = blockdata.trbr(250,550)
    mtplatforms.add(transblockr)
    mtall_sprites_list.add(transblockr)

    #bottom right
    for bp_x in range(650,850,50):
        bp_y = 550
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockl = blockdata.trbl(600,550)
    mtplatforms.add(transblockl)
    mtall_sprites_list.add(transblockl)

    #middle 
    for bp_x in range(250,650,50):
        bp_y = 350
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockr = blockdata.trbr(650,350)
    mtplatforms.add(transblockr)
    mtall_sprites_list.add(transblockr)
    transblockl = blockdata.trbl(200,350)
    mtplatforms.add(transblockl)
    mtall_sprites_list.add(transblockl)


    #top platform left
    for bp_x in range(50,250,50):
        bp_y = 150
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockr = blockdata.trbr(250,150)
    mtplatforms.add(transblockr)
    mtall_sprites_list.add(transblockr)
    #top right
    for bp_x in range(650,850,50):
        bp_y = 150
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockl = blockdata.trbl(600,150)
    mtplatforms.add(transblockl)
    mtall_sprites_list.add(transblockl)
#---------------------------------------------------------------------------#      
    for g_y in range(0,600,50):
        g_x = 0
        brickblock = blockdata.brick(g_x,g_y)
        mtblock_list.add(brickblock)
        mtall_sprites_list.add(brickblock)
    for g_y in range(0,600,50):
        g_x = 850
        brickblock = blockdata.brick(g_x,g_y)
        mtblock_list.add(brickblock)
        mtall_sprites_list.add(brickblock)
#---------------------------------------------------------------------------#
spritestor.block_list.add(mtblock_list)
spritestor.platforms.add(mtplatforms)
spritestor.all_sprites_list.add(mtall_sprites_list)

