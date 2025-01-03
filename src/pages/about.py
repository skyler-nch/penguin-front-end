from nicegui import ui
from src.utils.image_injector import image_injection

def about():
    with ui.row().classes("gap-0").style("padding-top:10%"):
        with ui.column().style("padding-right:20px; width:60%"):
            with ui.row().classes("gap-0"):
                ui.html('<pageheader><number>02. </number>About</pageheader')
                ui.html("<line></line>")
            with ui.column().style("padding-top:20px;"):
                ui.label("Hi there! I'm a Computer Scientist with a penchant for making things work. My interests includes everything tech related, and I will constantly explore new things to try out").classes("normaltext")
                ui.label("Professionally I dabble with back-end development, with an expertise at dealing with high-volume data. Although I only recently left academia, I have experience and knowledge in everything under the umbrella of computer science.").classes("normaltext")
                ui.label("I mainly use python as my daily driver, and I love this language to death. Even the front-end for this website is coded and served with python. I also have professional experience in other languages, such as C# and C").classes("normaltext")
        with ui.column().style("padding-top:9%"):
            ui.image(image_injection("Portrait.jpg")).classes('w-64')