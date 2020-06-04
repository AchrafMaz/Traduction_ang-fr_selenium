from selenium import webdriver

def word():
    while True:
        try :
            a = input()
            a = int(a)
            raise AssertionError
        except ValueError:
            break
        except AssertionError:
            print("C'est impossible de chercher ce mot ! \n                                    Veuillez réssayer avec un autre mot !")
            continue
    return a
def go_url(url):
    global driver
    try:
        PATH = "C:\chromedriver.exe"
        driver.get(url)
    except:
        print(f"C'est impossible de saisir ce lien : {url} en utilisant : {PATH}")

# id : ctl00_cC_translate_box
# class : translate_box0
# name : translate_box
def findelemrnt(id):
    global driver
    try:
        texte = driver.find_element_by_id(id)
        print(texte.text)
    except:
        print(f"C'est impossible de trouver cet id : {id}")
t = word()
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
def main():
    global t
    id = 'ctl00_cC_translate_box'
    url = "https://dictionnaire.reverso.net/anglais-francais/" + t
    go_url(url)
    findelemrnt(id)
    driver.close()
if __name__=='__main__':
    main()
