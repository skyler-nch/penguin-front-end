from nicegui import ui

def techstack():
    with ui.row().classes("gap-0").style("padding-top:10%"):
        ui.html('<pageheader><number>03. </number>Tech Stack</pageheader>')
        ui.html("<line></line>")
    with ui.column().style("padding-top:2%"):
        ui.label("Languages").classes("normalsubheader")
        with ui.row():
            ui.label("Python").classes("bullets")
            ui.label("C#").classes("bullets")
            ui.label("HTML/CSS/Javascript").classes("bullets")
        ui.separator()
        ui.label("Web Frameworks").classes("normalsubheader")
        with ui.row():
            ui.label("Django").classes("bullets")
            ui.label("FastAPI").classes("bullets")
            ui.label("FlaskAPI").classes("bullets")
            ui.label("NiceGUI").classes("bullets")
        ui.separator()
        ui.label("Database").classes("normalsubheader")
        with ui.row():
            ui.label("MySQL").classes("bullets")
            ui.label("MongoDB").classes("bullets")
            ui.label("RedisDB").classes("bullets")
        ui.separator()
        ui.label("Robotics").classes("normalsubheader")
        with ui.row():
            ui.label("ROS").classes("bullets")
            ui.label("OpenCV").classes("bullets")
            ui.label("Pyax12").classes("bullets")
        ui.separator()
        ui.label("Miscellaneous").classes("normalsubheader")
        with ui.row():
            ui.label("Docker").classes("bullets")
            ui.label("Pytorch").classes("bullets")
            ui.label("Kafka").classes("bullets")
            ui.label("Pandas").classes("bullets")
        ui.separator()
