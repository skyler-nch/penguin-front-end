from nicegui import ui

def expertise():
    with ui.row().classes("gap-0").style("padding-top:10%"):
        ui.html('<pageheader><number>04. </number>Expertise</pageheader>')
        ui.html("<line></line>")
    with ui.splitter(value=30).classes('w-full').style("padding-top:20px;") as splitter:
        with splitter.before:
            with ui.tabs().props('vertical').classes('w-full').style("color:rgb(204,214,246);") as tabs:
                backend = ui.tab('Backend Dev')
                researcher = ui.tab('Researcher')
                roboticist = ui.tab('Roboticist')
        with splitter.after:
            with ui.tab_panels(tabs, value=backend).props('vertical').classes('w-full h-full').style("background-color:rgba(0,0,0,0);"):
                with ui.tab_panel(backend):
                    ui.html('<normaltext>Experience with common backend functionalities with <highlight>Django</highlight>, <highlight>FlaskAPI</highlight>, and <highlight>FastAPI</highlight>, such as authentication, authorization, connection pooling, caching, rate-limiting, service registries, and CRUD operations</normaltext>')
                    ui.html('<normaltext>Worked with high-throughput ETL processes, utilizing <highlight>Apache Kafka</highlight> if needed, and has worked with <highlight>MySQL</highlight>, <highlight>MongoDB</highlight>, and <highlight>RedisDB</highlight></normaltext>')
                    ui.html('<normaltext>Capable of architecting <highlight>microservice architecture</highlight> of the backend environment to serve the needs of the website</normaltext>')
                    ui.html('<normaltext>Performing data analytics of high-throughput data with minimal workload to the server with <highlight>pandas</highlight></normaltext>')
                with ui.tab_panel(researcher):
                    ui.html('<normaltext>Published Author of 3 different papers on different fields under Computer Science in IEEE and ACM</normaltext>')
                    ui.html('<normaltext>Research field touches on <highlight>Swarm Intelligence</highlight>, <highlight>Explainable AI</highlight>, and <highlight>Robotics</highlight></normaltext>')
                    ui.button("Google Scholar")
                with ui.tab_panel(roboticist):
                    ui.html('<normaltext>Worked on the <highlight>Turtlebot 2</highlight> with custom machined top for a Kinematic Arm to explore the possibility of solving object collection on a moving platform</normaltext>')
                    ui.html('<normaltext>Utilisation of <highlight>ROS</highlight> and <highlight>OpenCV</highlight> for basic operations for the robot, with specialised libraries for the kinematic operations</normaltext>')
                    ui.button("Thesis")