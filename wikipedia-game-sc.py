from queue import Queue
import wikipediaapi
import time

user_agent = "MsOrret'sWikipediaGame/1.0 (orret.deborah@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

# HELPER FUNCTION: fetch_links(page) passes in a wikipedia page and returns a list of all the pages linked from that page
def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    # FINISH THE CODE HERE

    queue = Queue()

    parent={}
   
    path = []

    queue.put(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break

        current_page = wiki_wiki.page(current_page_title)

        current_links = fetch_links(current_page)

        visited.append(current_page)

        for thing in current_links:
            if thing not in visited:
                queue.put(thing)
                parent[thing] = current_page_title
   
    child = target_page.title

    while child != start_page.title:
        path.append(child)
        child = parent[child]
    path.append(start_page.title)
    path.reverse()
        #(queue.get())

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
    return path

print(fetch_links(wiki_wiki.page('Dwayne Johnson')))

# Example usage:
start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian language')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)

