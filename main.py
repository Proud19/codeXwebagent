from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tokens import ARXIV_EMAIL, ARXIV_PASSWORD, OPENAI_API_KEY
from selenium.webdriver.common.action_chains import ActionChains


from openai import OpenAI
client = OpenAI(
    api_key = OPENAI_API_KEY
)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os 
import json
driver = webdriver.Chrome()

from tracking import InteractionTracker
from userInfoApp import runUserInfoApp

# Inject Heatmap.js and interaction data
heatmap_js = """
// Load Heatmap.js library
var script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/heatmap.js@2.0.5';
script.onload = function() {
    // Create heatmap container
    var heatmapContainer = document.createElement('div');
    heatmapContainer.setAttribute('style', 'position: fixed !important; width: 100%; height: 100%;');
    document.body.appendChild(heatmapContainer);

    // Create heatmap instance
    var heatmapInstance = h337.create({
        container: heatmapContainer
    });


    // Prepare heatmap data
    var heatmapData = {
        max: 10,
        data: window.interaction_data.map(function(d) {
            return { x: d.x, y: d.y, value: 1 };
        })
    };
    heatmapContainer.style.position = "fixed" 
    console.log(heatmapContainer.style.position); 
    // Set heatmap data
    heatmapInstance.setData(heatmapData);
};
document.head.appendChild(script);
"""

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Function to generate responses using ChatGPT
def generate_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message

# Function to automate login using Selenium
def automate_login(username, password):
    
    try:
        
        
        # Wait for the page to load
        time.sleep(3)  # Adjust this delay as needed
        
        # Extract the page source (HTML content)
        html_content = driver.page_source
        
        # Create a prompt for ChatGPT to find the selectors
        prompt = f"""
        Here is the HTML content of a login page:
        {html_content}

        generate code that using functions from ActionChains module in selenium
        this code will be run via the "exec" method and should fill in the appropriate fields 
        but SHOULD NOT LOGIN. The code should simulate moving around the mouse aimlessly and trying to type into 
        any available input fields for a while  like a human would 
        before eventually successfully filling the login credentials . 

        YOUR RESPONSE SHOULD ONLY CONTAIN CODE AND NOTHING ELSE, JUST CODE. 
        

        Here are the login credentials. The username is: {username} and the password 
        is: {password}. 

        Here is some example code to illustrate the idea: 

        "username_selector = selectors['username_selector']
        password_selector = selectors['password_selector']
        login_button_selector = selectors['login_selector']
        
        # Find the elements using the selectors from ChatGPT
        username_field = driver.find_element(By.CSS_SELECTOR, username_selector)
        password_field = driver.find_element(By.CSS_SELECTOR, password_selector)
        login_button = driver.find_element(By.CSS_SELECTOR, login_button_selector)

        # Initialize ActionChains
        actions = ActionChains(driver)

        # Define a series of mouse movements and clicks
        actions.move_by_offset(100, 200)  # Move to (100, 200) from the current position
        actions.click()                # Click at the current position
        actions.pause(1)                  # Pause for 1 second

        actions.move_by_offset(50, 50)    # Move to (150, 250) from the last position
        actions.click()                   # Click at the current position
        actions.pause(1)                  # Pause for 1 second

        actions.move_by_offset(0, 500)    # Scroll down by 500 pixels
        actions.pause(1)                  # Pause for 1 second

        # Perform the actions
        actions.perform()
        " 
        YOU NEED TO DEFINE ALL THE VARIABLES FROM SCRATCH. PRETEND THAT ALL THESE VARIABLES DO NOT 
        EXIST. 

        THE CODE SHOULD NOT CLICK THE LOGIN BUTTON 

        You are only given the username, password and "driver". 
        """ 
        
        # Get the response from ChatGPT
        chatgpt_response = generate_chatgpt_response(prompt).content
        print("ChatGPT Response:", chatgpt_response)
        print("Making use of exec")
        exec("print('Executing Chat gpt**** Code')")
        exec(chatgpt_response)

    except: 
        pass    
    
    

# Main function
def main():


    user_info, login_info = {}, {}
    def on_submit(login_i, user_i): 
        login_info, user_info  = login_i, user_i

        # Navigate to the URL
        driver.get(login_info["website_url"])

        interaction_tracker = InteractionTracker(driver)
        print("Login infor is:", login_info)
        
        # Automate the login process
        automate_login(login_info["username"], login_info["password"])

        driver.execute_script("console.log(window.interaction_data);")
        print("Executing heatmap script")
        driver.execute_script(heatmap_js)
        input("Sleeping, press enter to continue ")
    
    runUserInfoApp(on_submit)


    # url = "https://arxiv.org/login"  # Replace with the actual login URL
    # username = ARXIV_EMAIL
    # password = ARXIV_PASSWORD


    

if __name__ == "__main__":
    main()

