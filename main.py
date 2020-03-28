from repository import Repository
from service import Service
from ui import UI


path = r"C:\Users\Andreea\Desktop\Facultate\Anul_II\Sem2\AI\GA_TSP\data\berlin.in"
repo = Repository(path)
service = Service(repo)
ui = UI(service)
ui.main()

