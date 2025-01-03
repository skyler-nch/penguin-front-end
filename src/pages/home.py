from nicegui import ui

def home():
    with ui.column().classes("gap-0"):
        ui.label("Hi, my name is").classes("smallgreen").style('padding-top:15%')
        ui.label("Skyler Ng.").classes("bigheader")
        ui.label("I build things;").classes("bigsubheader")
        ui.label("I'm a Computer Scientist, self-learning and constantly improving;").classes("normaltext")
        ui.label("I mostly do backend stuff, but constantly learns about other things as well;").classes("normaltext")
        ui.label("Masters in Computer Science, Published Author, Python Addict;").classes("normaltext")