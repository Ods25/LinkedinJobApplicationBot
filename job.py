from helium import *
import random
import time

def sign_in():
    start_firefox('linkedin.com');w8("starting firefox")
    w8()
    usr = input("Please input your username: ")
    pw = input("Please input your password: ")
    write(usr,into="Email or phone")
    write(pw,into="Password") 
    w8()
    click("Sign in")
    time.sleep(30)
    w8()
    string = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords="+search+"&location="+location+"&start="+str(start)
    go_to(string)
    #click(S(".occludable-update"))
def init():
    click(S(".job-card-search__location.artdeco-entity-lockup__caption.ember-view")) #We must click the first job in the list because linkedin appears to refresh when that happens.
    w8()
    press(SHIFT+TAB) #shifttab in order to get out of the box and into the previous selection (what the mouse just clicked)
    w8()
    for i in range(4):
        press(PAGE_DOWN)
        w8()
    for i in range(4):
        press(PAGE_UP)
        w8()
def app():
    path = 0;
    if(find_all(S(".artdeco-inline-feedback__message")) == []):
        try:
            print(path)
            path+=1
            click(S(".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view"))
            print(path)
            path+=1
            buttons = find_all(S(".artdeco-button.artdeco-button--2.artdeco-button--primary"));w8()
            print(path)
            path+=1
            overlays = find_all(S(".artdeco-modal-overlay.artdeco-modal-overlay--layer-default.artdeco-modal-overlay--is-top-layer.ember-view"))
            print(path)
            path+=1
            while(len(buttons) >= 1 and len(overlays) >= 1):
                print(path)
                path+=1
                try:
                    click(S(".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view"));w8()
                except:
                    click(S(".js-message-apply-submit.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view"));w8()
                print(path)
                path+=1
                buttons = find_all(S(".artdeco-button.artdeco-button--2.artdeco-button--primary"))
                print(path)
                path+=1
                overlays = find_all(S(".artdeco-modal-overlay.artdeco-modal-overlay--layer-default.artdeco-modal-overlay--is-top-layer.ember-view"))
                print(path)
                path+=1
        except:
            print("Failed to apply with application procedure 1")
def w8(inp="blank"): #This waits.
    x = random.uniform(5.0 , 15.0)
    print(str(inp), "...Waiting for ", x, " seconds.")
    time.sleep(x) #0.5 gets ya banned, 2.3-10.2 is slow as fuck but it's faster than not applying for jobs.

start = int(input("What application number do you want to start on: "))
search = str(input("What search criteria are we doing: "))
location = str(input("What location do you want?"))
fail = 0;w8("set fail ==0" )
applied = 0;w8("set applied ==0" )
sign_in()
print("Sleeping for 15 seconds...")
time.sleep(15)
w8()
while(True):
    while(applied <24):
        try:
            init()
        except:
            init()
        joblist = find_all(S(".job-card-search__location.artdeco-entity-lockup__caption.ember-view"))
        if(len(joblist) < 7):
            init()
            joblist = find_all(S(".job-card-search__location.artdeco-entity-lockup__caption.ember-view"))
        for job in joblist:
            w8()
            click(job)
            app()
            print("applied for on this page: ", applied, "total need to apply for: ", len(joblist)-1)
            applied += 1
    applied = 0
    start += 25
    string = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords="+search+"&location="+location+"&start="+str(start)
    go_to(string)
    print("Sleeping for 15 seconds...")
    time.sleep(15)
