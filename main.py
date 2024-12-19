from nicegui import app, ui
from src.router_logic.router import Router
from src.layout.home_layout import home
from src.layout.dashboard_layout import dashboard 

#multi router setup to allow for a single url with multiple SPAs
#each layout is a single SPAs

@ui.page('/dashboard')
@ui.page('/dashboard/{_:path}')
def call_dashboard_layout() -> None:
    dashboard()

#root must be last as it will take precedence against other sublinks if not 
@ui.page('/')
@ui.page('/{_:path}')
def call_home_layout() -> None:
    home()

ui.run()
