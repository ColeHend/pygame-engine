class Scene_Manager():
    config = { # config options
        "RES":[1280,720],
        "RUNNING": True,
        "FPS": 60
        }
    system = { # core module types
        "MAP",
        "TITLE",
        "EVENT"
    }
    plugins = { # plugins module types
        "EVENT"
    }
    def event_loop(self, event, pygame):
        if event.type == pygame.QUIT:
            self.config['RUNNING'] = False

    def draw(self):
        if False == True:
            print('draw')
            # self.system[state].draw()

    def update(self):
        if False == True:
            print('update')