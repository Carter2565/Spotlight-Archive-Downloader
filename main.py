from playwright.sync_api import sync_playwright
import requests
import shutil
import json
import os

start_page = 1 # Starts at 1
stop_page = None # If None will download entyre set or updates current set
json_file_path = 'index.json'


# Initialize Playwright
with sync_playwright() as p:
  # Launch a browser instance
  browser = p.firefox.launch()

  # Create a new page (tab)
  site = browser.new_page()

  site.goto(f'https://windows10spotlight.com/')
  site.wait_for_timeout(1000)

  # Get the 5th element with page numbers in the container
  fifth_element = site.query_selector_all('.page-numbers')[4]

  # Extract the text from the element
  pages = fifth_element.inner_text()
  
  try:
    with open(json_file_path, 'r') as file:
      existing_data = json.load(file)
  except FileNotFoundError:
    existing_data = {}
  except json.JSONDecodeError:
    shutil.copy(json_file_path, f'./{json_file_path}.old')
    existing_data = {}
  
  current = 0
    
  for image in existing_data:
    page = existing_data[image]['page']
    if page >= current:
      current = page
  
  if stop_page:
    total_pages = stop_page
  else:
    total_pages = int(pages.replace(",", ""))


    if current < total_pages:
      total_pages -= current
      for image in existing_data:
        existing_data[image]['page'] += total_pages
      print(f'Updating! {total_pages} Pages')

    elif current == total_pages:
      print('Everything is up to date')
      exit()
    
  
# Loop from 'start_page' to the end of the range (total_pages)
  for page_num in range(start_page-1, total_pages):
    try:
      site.goto(f'https://windows10spotlight.com/page/{page_num+1}') # Range is 0 based
      site.wait_for_timeout(10)
      
      references = site.query_selector_all('.anons-thumbnail')
      images = site.query_selector_all('.thumbnail')
      dates = site.query_selector_all('.date')
      reference_links = []
      image_ids = []
      sources = []
      
      for reference in references:
        href = reference.get_property('href')
        reference_links.append(href)
      
      for image in images:
        src = image.get_property('src')
        sources.append(src)
        img = str(src).replace("-1024x576", "")
        image_url = img
        response = requests.get(image_url)
        if response.status_code == 200:         
          file_name = image_url.split('/')[-1] 
          image_ids.append(file_name.replace(".jpg", ""))       
          with open(file_name, 'wb') as file:
            file.write(response.content)
          
          print(f"Image downloaded and saved as '{file_name}'")
        else:
          print(f"Failed to download image. Status code: {response.status_code}")

      for i in range(len(image_ids)):
        data = {
          f'{image_ids[i]}':{'page':page_num+1, 'date':f'{dates[i].inner_text()}', 'source':f'{sources[i]}','reference':f'{reference_links[i]}'}
        }

        existing_data.update(data)

        with open(json_file_path, 'w') as file:
          json.dump(existing_data, file, indent=2)

      # Perform some actions in the new tab, e.g., take a screenshot
      site.screenshot(path='new_tab_screenshot.png')
    except Exception as e:
      with open('Error.txt', 'a') as file:
        # Write data to the file
        print(f'Error on page {page_num+1}, page numner logged in Error.txt\n')
        file.write(f'Error on page {page_num+1}\n')
        file.write(f'{e}\n')
      exit()
      
  # Close the new tab
  site.close()

  # Close the browser
  browser.close()
