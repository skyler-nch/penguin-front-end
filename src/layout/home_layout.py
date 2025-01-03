from nicegui import ui
from src.router_logic.router import Router
from src.utils.css_injector import css_injection
from src.utils.svg_injector import svg_injection
from src.utils.image_injector import image_injection

from src.pages.home import home
from src.pages.about import about
from src.pages.techstack import techstack
from src.pages.expertise import expertise

def main():
    #setup SPA router
    router = Router()
    ui.add_css(css_injection("home"))

    @router.add('/')
    def home_page():
        home()        

    @router.add('/about')
    def about_page():
        about()

    @router.add('/techstack')
    def techstack_page():
        techstack()

    @router.add('/expertise')
    def expertise_page():
        expertise()        

    #body modifier
    
    ui.query('body').style('background-color: #0A192F')


    #header
    with ui.header(elevated=False).style('background-color: #0A192F'):
        #row layout to organize header contents
        with ui.row().classes('w-full gap-0 items-center'):
            ui.html(svg_injection("penguin"))
            ui.space()
            
            #row layout to organize button contents
            with ui.row().classes("gap-8"):
                ui.html('<topbar><number>01. </number>Home</topbar').classes("box").on("click", lambda: router.open(home_page))
                ui.html('<topbar><number>02. </number>About</topbar').classes("box").on("click", lambda: router.open(about_page))
                ui.html('<topbar><number>03. </number>Techstack</topbar').classes("box").on("click", lambda: router.open(techstack_page))
                ui.html('<topbar><number>04. </number>Expertise</topbar').classes("box").on("click", lambda: router.open(expertise_page))
                #ui.html('<topbar>Login</topbar>').classes("box border")
                ui.space()


    with ui.row().classes("w-full justify-center"):
        ui.space()
        router.frame().classes('grow col-span-2').style("max-width:70%")
        ui.space()

    #left bottom side of whitespace
    with ui.column().classes('fixed-bottom-left gap-8'):
        ui.html(svg_injection("github"))
        ui.html(svg_injection("linkedin"))
        ui.html("<div class='vl'></div>").style("margin: 0 auto; border-left: 1px solid white; height: 90px;")

    #right bottom side of whitespace
    with ui.column().classes('fixed-bottom-right gap-24'):
        ui.html("skyler.nch@gmail.com").classes("rotatedtext")
        ui.html("<div class='vl'></div>").style("margin: 0 auto; border-left: 1px solid white; height: 90px;")

