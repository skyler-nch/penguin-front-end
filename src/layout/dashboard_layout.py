from nicegui import ui
from src.router_logic.router import Router


def dashboard():
    router = Router()
    ui.label("dashboard")

    @router.add('/dashboard')
    def show_one():
        ui.label("page 1")
    
    @router.add('/dashboard/two')
    def show_two():
        ui.label("page 2")

    @router.add('/dashboard/three')
    def show_three():
        ui.label("page 3")

        # adding some navigation buttons to switch between the different pages
    with ui.row():
        ui.button('One', on_click=lambda: router.open(show_one)).classes('w-32')
        ui.button('Two', on_click=lambda: router.open(show_two)).classes('w-32')
        ui.button('Three', on_click=lambda: router.open(show_three)).classes('w-32')
        ui.button('HOME', on_click=lambda: ui.navigate.to("/")).classes('w-32')

    # this places the content which should be displayed
    router.frame().classes('w-full p-4 bg-gray-100')

    
    
