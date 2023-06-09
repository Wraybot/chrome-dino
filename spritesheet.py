import pygame

class spritesheet(object):
    def __init__(self, filename):
        
        self.sheet = pygame.image.load(filename).convert()
    
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        
        image = self.enlarge_image(image, colorkey)
        
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
    
    def enlarge_image(self, image, colorkey = None):
        new_image = pygame.surface.Surface((image.get_width() * 2, image.get_height() * 2))
        pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2), new_image)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = new_image.get_at((0,0))
            new_image.set_colorkey(colorkey, pygame.RLEACCEL)
        return new_image

class Get_text():

    def __init__(self):

        pygame.font.init()
        self.fonty = pygame.font.SysFont(None, 24)

    def enlarge_image(self, image, colorkey = None):
        new_image = pygame.surface.Surface((image.get_width() * 2, image.get_height() * 2))
        pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2), new_image)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = new_image.get_at((0,0))
            new_image.set_colorkey(colorkey, pygame.RLEACCEL)
        return new_image

    def prep_message(self, message, text_color = "black", bg_color = None):

        self.image = self.fonty.render(message, True, text_color, bg_color)
        return self.image    

