import time 

"""
This class is used to track what the agent is doing in a particular website. 
Has the capability to generate a heatmap of the interaction. 
"""

def initialize_console_tracking(driver): 
    init_script = """
    console.log("Initializing interaction data"); 
    window.interaction_data = []; 

    document.addEventListener('mousemove', function(event) {
                window.dispatchEvent(new CustomEvent('recordMouseMove', {
                    detail: { x: event.clientX, y: event.clientY }
                }));
            });
    window.addEventListener('recordMouseMove', function(event) {
            window.interaction_data.push(event.detail);
        });
    document.addEventListener('click', function(event) {
            window.dispatchEvent(new CustomEvent('recordClick', {
                detail: { x: event.clientX, y: event.clientY }
            }));
        });
    window.addEventListener('recordClick', function(event) {
            window.interaction_data.push(event.detail);
        }); 
    document.addEventListener('scroll', function() {
            window.dispatchEvent(new CustomEvent('recordScroll', {
                detail: { x: event.clientX, y: event.clientY }
            }));
        });
    window.addEventListener('recordScroll', function() {
            window.interaction_data.push(event.detail);
    });

    // Function to handle focus and keypress events
    function handleTyping(event) {
        var rect = event.target.getBoundingClientRect();
        var x = rect.left + event.target.offsetWidth / 2;
        var y = rect.top + event.target.offsetHeight / 2;
        window.interaction_data.push({'x': x, 'y': y})
    }

    document.addEventListener('focus', handleTyping);
    document.addEventListener('keydown', handleTyping);
    """
    driver.execute_script(init_script)

    


class InteractionTracker: 
    def __init__(self, driver): 
        self.driver = driver
        initialize_console_tracking(driver)


    def track_mouse_movement(self, event):
        x, y = event.clientX, event.clientY
        self.interaction_data.append({'type': 'mousemove', 'x': x, 'y': y, 'timestamp': time.time()})

    
    def track_click(self, event):
        x, y = event.clientX, event.clientY
        self.interaction_data.append({'type': 'click', 'x': x, 'y': y, 'timestamp': time.time()})

    def track_scroll(self):
        x, y = self.driver.execute_script('return window.scrollX;'), driver.execute_script('return window.scrollY;')
        self.interaction_data.append({'type': 'scroll', 'x': x, 'y': y, 'timestamp': time.time()})

    def save_interaction_data(self): 
        with open('interaction_data.json', 'w') as f:
            json.dump(interaction_data, f)