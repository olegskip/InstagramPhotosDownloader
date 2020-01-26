from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
options.add_argument("--headless")

driver = None
path_to_photo = "/html/body/div[1]/section/main/div/div/article/div[1]/div/div/div[1]/img"


def main():
	print("Checking for driver existing...")
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
	url = str(input("url = "))
	driver.get(url)
	image_path = driver.find_element_by_xpath(path_to_photo).get_attribute("src")
	with open('output.png', 'wb') as file:
		file.write(driver.find_element_by_xpath(path_to_photo).screenshot_as_png)

	print("Finished!")

if __name__ == '__main__':
	main()