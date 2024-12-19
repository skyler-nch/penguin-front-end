from nicegui import ui
from src.router_logic.router import Router
from src.utils.css_injector import css_injection
from src.utils.svg_injector import svg_injection
from src.utils.image_injector import image_injection

def home():
    #setup SPA router
    router = Router()
    ui.add_css(css_injection("home"))

    @router.add('/')
    def home():
        with ui.column().classes("gap-0"):
            ui.label("Hi, my name is").classes("smallgreen").style('padding-top:15%')
            ui.label("Skyler Ng.").classes("bigheader")
            ui.label("I build things for the web;").classes("bigsubheader")
            ui.label("I'm a Computer Scientist, self-learning and constantly improving;").classes("normaltext")
            ui.label("I mostly do backend stuff, but constantly learns about other things as well;").classes("normaltext")
            ui.label("Masters in Computer Science, Published Author, Python Addict;").classes("normaltext")

    
    @router.add('/about')
    def about():
        with ui.row().classes("gap-0").style("padding-top:10%"):
            with ui.column().style("padding-right:20px; width:60%"):
                with ui.row().classes("gap-0"):
                    ui.html('<pageheader><number>02. </number>About</pageheader')
                    ui.html("<line></line>")
                with ui.column().style("padding-top:20px;"):
                    ui.label("Hi there! I'm a Computer Scientist with a penchant for making things work. My interests includes everything tech related, and I will constantly explore new things to try out").classes("normaltext")
                    ui.label("Professionally I dabble with back-end development, with an expertise at dealing with high-volume data. Although I only recently left academia, I have experience and knowledge in everything under the umbrella of computer science.").classes("normaltext")
                    ui.label("I mainly use python as my main daily driver, and I love this language to death. Even the front-end for this website is coded and served with python. I also have professional experience in other languages, such as C# and C").classes("normaltext")
            with ui.column().style("padding-top:9%"):
                ui.image(image_injection("Portrait.jpg")).classes('w-64')


    @router.add('/techstack')
    def techstack():
        ui.label("page 3").classes("normaltext")
    
    @router.add('/experience')
    def experience():
        ui.label("page 4").classes("normaltext")

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
                ui.html('<topbar><number>01. </number>Home</topbar').classes("box").on("click", lambda: router.open(home))
                ui.html('<topbar><number>02. </number>About</topbar').classes("box").on("click", lambda: router.open(about))
                ui.html('<topbar><number>03. </number>Techstack</topbar').classes("box").on("click", lambda: router.open(techstack))
                ui.html('<topbar><number>04. </number>Experience</topbar').classes("box").on("click", lambda: router.open(experience))
                ui.html('<topbar>Login</topbar>').classes("box border")
                ui.space()

    #main layout of the page
    with ui.grid(columns=4).classes('w-full gap-0 h-[calc(100vh-9rem)]'):
        ui.space().classes('col-span-1')

        #window for page contents
        router.frame().classes('col-span-2')
        
        ui.space().classes('col-span-1')

    #left bottom side of whitespace
    with ui.column().classes('fixed-bottom-left gap-8'):
        ui.html(svg_injection("github"))
        ui.html(svg_injection("linkedin"))
        ui.html("<div class='vl'></div>").style("margin: 0 auto; border-left: 1px solid white; height: 90px;")

    #right bottom side of whitespace
    with ui.column().classes('fixed-bottom-right gap-24'):
        ui.html("skyler.nch@gmail.com").classes("rotatedtext")
        ui.html("<div class='vl'></div>").style("margin: 0 auto; border-left: 1px solid white; height: 90px;")

